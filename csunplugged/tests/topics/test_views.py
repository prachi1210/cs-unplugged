from tests.BaseTest import BaseTest
from django.urls import reverse
from topics.models import Topic


class IndexViewTest(BaseTest):

    def __init__(self, *args, **kwargs):
        BaseTest.__init__(self, *args, **kwargs)

    def test_index_with_no_topics(self):
        url = reverse('topics:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_index_with_one_topic(self):
        new_topic = Topic(
            slug='binary-numbers',
            name='Binary Numbers',
            content='content',
            other_resources='content',
            icon='icon'
        )
        new_topic.save()
        url = reverse('topics:index')
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        self.assertQuerysetEqual(
            response.context['all_topics'],
            ['<Topic: Binary Numbers>']
        )
