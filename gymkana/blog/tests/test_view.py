from django.test import TestCase, Client
from blog.models import New, Event
from blog.forms import NewNews
import datetime
from django.shortcuts import reverse
from django.http import Http404
from django.shortcuts import get_object_or_404


class ViewTest(TestCase):

    def setUp(self):
        New.objects.create(title="title1", subtitle="subtitle1", body="body1")
        New.objects.create(title="title2", subtitle="subtitle2", body="body2")
        New.objects.create(title="title3", subtitle="subtitle3", body="body3")
        New.objects.create(title="title4", subtitle="subtitle4", body="body4")

        Event.objects.create(title="title1", subtitle="subtitle1", body="body1", start_date=datetime.date.today(), end_date=datetime.date.today() + datetime.timedelta(days=1))
        Event.objects.create(title="title2", subtitle="subtitle2", body="body2", start_date=datetime.date.today(), end_date=datetime.date.today() + datetime.timedelta(days=1))
        Event.objects.create(title="title3", subtitle="subtitle3", body="body3", start_date=datetime.date.today(), end_date=datetime.date.today() + datetime.timedelta(days=1))
        Event.objects.create(title="title4", subtitle="subtitle4", body="body4", start_date=datetime.date.today(), end_date=datetime.date.today() + datetime.timedelta(days=1))

        self.client = Client()

    def test_index_page(self):
        url = reverse('index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/index.html')
        self.assertContains(response, 'Blog')

    def test_news_listed_properly(self):
        self.assertQuerysetEqual(New.objects.order_by('-id')[:3], ["<New: title2>", "<New: title3>", "<New: title4>"], ordered=False)

    def test_events_listed_properly(self):
        self.assertQuerysetEqual(Event.objects.order_by('-id')[:3], ["<Event: title2>", "<Event: title3>", "<Event: title4>"], ordered=False)


class NewCreateTest(TestCase):

    def setUp(self):
        self.form = NewNews()
        self.client = Client()

    def test_create_page_get(self):
        url = reverse('news_create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_create.html')
        self.assertContains(response, 'Blog')

    def test_create_page_post(self):
        url = reverse('news_create')
        dic_post = {'title': 'title1', 'subtitle': 'subtitle1', 'body': 'body1'}
        response = self.client.post(url, dic_post)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_create.html')
        self.assertContains(response, 'Blog')

    def test_news_form_created_properly(self):
        self.assertFalse(self.form.is_valid())


class NewViewTest(TestCase):

    def setUp(self):
        New.objects.create(title="title1", subtitle="subtitle1", body="body1")
        New.objects.create(title="title2", subtitle="subtitle2", body="body2")
        New.objects.create(title="title3", subtitle="subtitle3", body="body3")
        New.objects.create(title="title4", subtitle="subtitle4", body="body4")

        Event.objects.create(title="title1", subtitle="subtitle1", body="body1", start_date=datetime.date.today(), end_date=datetime.date.today() + datetime.timedelta(days=1))
        Event.objects.create(title="title2", subtitle="subtitle2", body="body2", start_date=datetime.date.today(), end_date=datetime.date.today() + datetime.timedelta(days=1))
        Event.objects.create(title="title3", subtitle="subtitle3", body="body3", start_date=datetime.date.today(), end_date=datetime.date.today() + datetime.timedelta(days=1))
        Event.objects.create(title="title4", subtitle="subtitle4", body="body4", start_date=datetime.date.today(), end_date=datetime.date.today() + datetime.timedelta(days=1))

        self.client = Client()

    def test_news_list_properly_all(self):
        self.assertQuerysetEqual(New.objects.all(), ["<New: title1>", "<New: title2>", "<New: title3>", "<New: title4>"], ordered=False)

    def test_events_list_properly_all(self):
        self.assertQuerysetEqual(Event.objects.all(), ["<Event: title1>", "<Event: title2>", "<Event: title3>", "<Event: title4>"], ordered=False)

    def test_view_page_get(self):
        url = reverse('news_view')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/news_view.html')
        self.assertContains(response, 'Blog')


class NewViewDetailTest(TestCase):

    def setUp(self):
        self.news_1 = New.objects.create(title="title1", subtitle="subtitle1", body="body1")
        self.news_2 = New.objects.create(title="title2", subtitle="subtitle2", body="body2")

    def test_get_object_or_404(self):
        # No Events yet, so we should get a Http404 error.
        with self.assertRaises(Http404):
            get_object_or_404(Event, title="Foo")

        # get_object_or_404 can be passed a Model to query.
        self.assertEqual(get_object_or_404(New, title__contains="1"), self.news_1)

        self.assertNotEqual(self.news_1, self.news_2)

    def test_view_detail_page_get(self):
        url = reverse('news_view_detail', kwargs={'news_id': 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/news_view_detail.html')
        self.assertContains(response, 'Blog')


class NewEditTest(TestCase):

    def setUp(self):
        self.news_1 = New.objects.create(title="title1", subtitle="subtitle1", body="body1")
        self.news_2 = New.objects.create(title="title2", subtitle="subtitle2", body="body2")

    def test_get_object_or_404(self):
        # No Events yet, so we should get a Http404 error.
        with self.assertRaises(Http404):
            get_object_or_404(Event, title="Foo")

        # get_object_or_404 can be passed a Model to query.
        self.assertEqual(get_object_or_404(New, title__contains="1"), self.news_1)

        self.assertNotEqual(self.news_1, self.news_2)

    def test_edit_page_get(self):
        url = reverse('news_edit', kwargs={'news_id': 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/news_edit.html')
        self.assertContains(response, 'Blog')

    def test_edit_page_post(self):
        url = reverse('news_edit', kwargs={'news_id': 1})
        dic_post = {'title': 'title1', 'subtitle': 'subtitle1', 'body': 'body1'}
        response = self.client.post(url, dic_post)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/news_edit.html')
        self.assertContains(response, 'Blog')


class NewDeleteTest(TestCase):

    def setUp(self):
        self.news_1 = New.objects.create(title="title1", subtitle="subtitle1", body="body1")
        self.news_2 = New.objects.create(title="title2", subtitle="subtitle2", body="body2")

    def test_get_object_or_404(self):
        # No Events yet, so we should get a Http404 error.
        with self.assertRaises(Http404):
            get_object_or_404(Event, title="Foo")

        # get_object_or_404 can be passed a Model to query.
        self.assertEqual(get_object_or_404(New, title__contains="1"), self.news_1)

        self.assertNotEqual(self.news_1, self.news_2)

    def test_delete_page_get(self):
        url = reverse('news_delete', kwargs={'news_id': 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/news_delete.html')
        self.assertContains(response, 'Blog')

    def test_delete_page_post(self):
        url = reverse('news_view')
        response = self.client.post(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/news_view.html')
        self.assertContains(response, 'Blog')


class NewViewClassTest(TestCase):

    def setUp(self):
        New.objects.create(title="title1", subtitle="subtitle1", body="body1")
        New.objects.create(title="title2", subtitle="subtitle2", body="body2")
        New.objects.create(title="title3", subtitle="subtitle3", body="body3")
        New.objects.create(title="title4", subtitle="subtitle4", body="body4")

        Event.objects.create(title="title1", subtitle="subtitle1", body="body1", start_date=datetime.date.today(), end_date=datetime.date.today() + datetime.timedelta(days=1))
        Event.objects.create(title="title2", subtitle="subtitle2", body="body2", start_date=datetime.date.today(), end_date=datetime.date.today() + datetime.timedelta(days=1))
        Event.objects.create(title="title3", subtitle="subtitle3", body="body3", start_date=datetime.date.today(), end_date=datetime.date.today() + datetime.timedelta(days=1))
        Event.objects.create(title="title4", subtitle="subtitle4", body="body4", start_date=datetime.date.today(), end_date=datetime.date.today() + datetime.timedelta(days=1))

        self.client = Client()

    def test_news_list_properly_all(self):
        self.assertQuerysetEqual(New.objects.all(), ["<New: title1>", "<New: title2>", "<New: title3>", "<New: title4>"], ordered=False)

    def test_events_list_properly_all(self):
        self.assertQuerysetEqual(Event.objects.all(), ["<Event: title1>", "<Event: title2>", "<Event: title3>", "<Event: title4>"], ordered=False)

    def test_view_page_get(self):
        url = reverse('news_view_class')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/news_view.html')
        self.assertContains(response, 'Blog')


class NewsViewDetailClass(TestCase):

    def setUp(self):
        self.news_1 = New.objects.create(title="title1", subtitle="subtitle1", body="body1")
        self.news_2 = New.objects.create(title="title2", subtitle="subtitle2", body="body2")

    def test_get_context(self):
        response = self.client.get(reverse('news_view_detail_class', kwargs={'news_id': 1}))
        self.assertContains(response, 'subtitle1')


class EventViewClass(TestCase):

    def setUp(self):
        New.objects.create(title="title1", subtitle="subtitle1", body="body1")
        New.objects.create(title="title2", subtitle="subtitle2", body="body2")
        New.objects.create(title="title3", subtitle="subtitle3", body="body3")
        New.objects.create(title="title4", subtitle="subtitle4", body="body4")

        Event.objects.create(title="title1", subtitle="subtitle1", body="body1", start_date=datetime.date.today(), end_date=datetime.date.today() + datetime.timedelta(days=1))
        Event.objects.create(title="title2", subtitle="subtitle2", body="body2", start_date=datetime.date.today(), end_date=datetime.date.today() + datetime.timedelta(days=1))
        Event.objects.create(title="title3", subtitle="subtitle3", body="body3", start_date=datetime.date.today(), end_date=datetime.date.today() + datetime.timedelta(days=1))
        Event.objects.create(title="title4", subtitle="subtitle4", body="body4", start_date=datetime.date.today(), end_date=datetime.date.today() + datetime.timedelta(days=1))

        self.client = Client()

    def test_events_list_properly_all(self):
        self.assertQuerysetEqual(Event.objects.all(), ["<Event: title1>", "<Event: title2>", "<Event: title3>", "<Event: title4>"], ordered=False)

    def test_view_page_get(self):
        url = reverse('events_view_class')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/events_view.html')
        self.assertContains(response, 'Blog')
