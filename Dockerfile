# This Dockerfile is based off the Google App Engine Python runtime image
# https://github.com/GoogleCloudPlatform/python-runtime
FROM uccser/django:1.11.5

# Add metadata to Docker image
LABEL maintainer="csse-education-research@canterbury.ac.nz"

# Set terminal to be noninteractive
ARG DEBIAN_FRONTEND=noninteractive
ENV DJANGO_PRODUCTION=True

EXPOSE 8080
RUN mkdir /csunplugged
WORKDIR /csunplugged

# Copy and install Python dependencies
COPY requirements /requirements
RUN /docker_venv/bin/pip3 install -r /requirements/production.txt

ADD ./csunplugged /csunplugged/
CMD /docker_venv/bin/gunicorn -c gunicorn.conf.py -b :8080 config.wsgi
