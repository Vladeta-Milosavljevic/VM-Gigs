from django.test import TestCase
from jobs.models import Tag, Job


class TestJobModels(TestCase):
    def test_model(self):
        title = Job.objects.create(title='Django Test Title')
        self.assertEqual(str(title), 'Django Test Title')


class TestTagModels(TestCase):
    def test_model(self):
        name = Tag.objects.create(name='Django Test Name')
        self.assertEqual(str(name), 'Django Test Name')


class TestJobTag(TestCase):
    def test_many_to_many(self):
        test_job = Job.objects.create(title='Django Test')
        test_tag1 = Tag.objects.create(name='Test Tag 1')
        test_tag2 = Tag.objects.create(name='Test Tag 2')
        test_tag3 = Tag.objects.create(name='Test Tag 3')
        test_job.tags.set([test_tag1.pk, test_tag2.pk, test_tag3.pk])
        self.assertEqual(test_job.tags.count(), 3)


class JobModelTestInput(TestCase):
    @classmethod
    def setUpTestData(cls):
        Job.objects.create(title='Test title', company='Test company', location='Test location', email='testemail@test.com',
                           website='www.testwebsite.com', description='Test description', custom_tags='tag1, tag2, tag3')

    def test_job_valid_input(self):
        job = Job.objects.get(pk=1)
        self.assertEqual(job.title, 'Test title')
        self.assertEqual(job.company, 'Test company')
        self.assertEqual(job.location, 'Test location')
        self.assertEqual(job.email, 'testemail@test.com')
        self.assertEqual(job.website, 'www.testwebsite.com')
        self.assertEqual(job.description, 'Test description')
        self.assertEqual(job.custom_tags,
                         'tag1, tag2, tag3')

    def test_job_labels(self):
        job = Job.objects.get(id=1)

        title_label = job._meta.get_field('title').verbose_name
        self.assertEqual(title_label, 'title')

        company_label = job._meta.get_field('company').verbose_name
        self.assertEqual(company_label, 'company')

        location_label = job._meta.get_field('location').verbose_name
        self.assertEqual(location_label, 'location')

        email_label = job._meta.get_field('email').verbose_name
        self.assertEqual(email_label, 'email')

        website_label = job._meta.get_field('website').verbose_name
        self.assertEqual(website_label, 'website')

        description_label = job._meta.get_field('description').verbose_name
        self.assertEqual(description_label, 'description')

        custom_tags_label = job._meta.get_field('custom_tags').verbose_name
        self.assertEqual(custom_tags_label, 'custom tags')

        description_label = job._meta.get_field('description').verbose_name
        self.assertEqual(description_label, 'description')

