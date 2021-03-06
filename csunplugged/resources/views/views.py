"""Views for the resource application."""

from django.conf import settings
from django.contrib.staticfiles import finders
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render
from django.template.loader import render_to_string
from django.views import generic
from resources.models import Resource
from resources.utils.resource_pdf_cache import resource_pdf_cache
from utils.group_lessons_by_age import group_lessons_by_age
from resources.utils.get_resource_generator import get_resource_generator
from resources.utils.generate_resource_copy import generate_resource_copy
from utils.errors.QueryParameterMissingError import QueryParameterMissingError
from utils.errors.QueryParameterInvalidError import QueryParameterInvalidError

RESPONSE_CONTENT_DISPOSITION = 'attachment; filename="{filename}.pdf"'


class IndexView(generic.ListView):
    """View for the resource application homepage."""

    template_name = "resources/index.html"
    context_object_name = "all_resources"

    def get_queryset(self):
        """Get queryset of all resources.

        Returns:
            Queryset of all resources ordered by name.
        """
        return Resource.objects.order_by("name")


def resource(request, resource_slug):
    """View for a specific resource in the resources application.

    Args:
        request: HttpRequest object.
        resource_slug: The slug of the requested resource.

    Returns:
        HTML response of webpage, 404 if not found.
    """
    resource = get_object_or_404(Resource, slug=resource_slug)
    context = dict()
    context["resource"] = resource
    context["debug"] = settings.DEBUG
    context["resource_thumbnail_base"] = "{}img/resources/{}/thumbnails/".format(settings.STATIC_URL, resource.slug)
    context["grouped_lessons"] = group_lessons_by_age(resource.lessons.all())
    if resource.thumbnail_static_path:
        context["thumbnail"] = resource.thumbnail_static_path
    return render(request, resource.webpage_template, context)


def generate_resource(request, resource_slug):
    """View for generated PDF of a specific resource.

    Args:
        request: HttpRequest object.
        resource_slug: The slug of the requested resource.

    Returns:
        HTML response containing PDF of resource, 404 if not found.
    """
    resource = get_object_or_404(Resource, slug=resource_slug)
    if not request.GET:
        raise Http404("No parameters given for resource generation.")
    try:
        generator = get_resource_generator(resource.generator_module, request.GET)
    except QueryParameterMissingError as e:
        raise Http404(e) from e
    except QueryParameterInvalidError as e:
        raise Http404(e) from e

    # TODO: Weasyprint handling in production
    # TODO: Add creation of PDF as job to job queue
    if settings.DJANGO_PRODUCTION:
        # Return cached static PDF file of resource.
        # Currently developing system for dynamically rendering
        # custom PDFs on request (https://github.com/uccser/render).
        return resource_pdf_cache(resource.name, generator)
    else:
        (pdf_file, filename) = generate_resource_pdf(resource.name, generator)
        response = HttpResponse(pdf_file, content_type="application/pdf")
        response["Content-Disposition"] = RESPONSE_CONTENT_DISPOSITION.format(filename=filename)
        return response


def generate_resource_pdf(name, generator):
    """Return a response containing a generated PDF resource.

    Args:
        name: Name of resource to be created (str).
        generator: Instance of specific resource generator class.

    Returns:
        Tuple of PDF file of generated resource and filename.
    """
    from weasyprint import HTML, CSS

    context = dict()
    context["resource"] = name
    context["header_text"] = generator.requested_options.get("header_text", "")
    context["paper_size"] = generator.requested_options["paper_size"]

    num_copies = range(0, int(generator.requested_options.get("copies", 1)))
    context["all_data"] = []
    for copy in num_copies:
        context["all_data"].append(
            generate_resource_copy(generator)
        )

    filename = "{} ({})".format(name, generator.subtitle)
    context["filename"] = filename

    pdf_html = render_to_string("resources/base-resource-pdf.html", context)
    html = HTML(string=pdf_html, base_url=settings.BUILD_ROOT)
    css_file = finders.find("css/print-resource-pdf.css")
    css_string = open(css_file, encoding="UTF-8").read()
    base_css = CSS(string=css_string)
    return (html.write_pdf(stylesheets=[base_css]), filename)
