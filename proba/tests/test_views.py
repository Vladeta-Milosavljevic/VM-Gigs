from django.test import TestCase
from django.urls import reverse
from jobs.models import Job, Tag
from django.contrib.auth.models import User


class JobViewsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_jobs = 15
        for test_jobs_id in range(test_jobs):
            job = Job.objects.create(title=f'Test title {test_jobs_id}', company=f'Test company {test_jobs_id}', location=f'Test location {test_jobs_id}', email=f'testemail{test_jobs_id}@test.com',
                                     website=f'www.testwebsite{test_jobs_id}.com', description=f'Test description {test_jobs_id}', custom_tags='tag1, tag2, tag3')

    # test index view

    def test_index_view_url_exists_at_location(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_index_view_url_accessible_by_name(self):
        response = self.client.get(reverse('jobs:index'))
        self.assertEqual(response.status_code, 200)

    def test_index_view_uses_correct_template(self):
        response = self.client.get(reverse('jobs:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'jobs/index.html')

    # test jobList view

    def test_jobList_view_url_exists_at_location(self):
        response = self.client.get('/jobs_list/')
        self.assertEqual(response.status_code, 200)

    def test_jobList_view_url_accessible_by_name(self):
        response = self.client.get(reverse('jobs:jobs_list'))
        self.assertEqual(response.status_code, 200)

    def test_jobList_view_uses_correct_template(self):
        response = self.client.get(reverse('jobs:jobs_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'jobs/jobs_list.html')

    def test_pagination_is_two(self):
        response = self.client.get(reverse('jobs:jobs_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('page_obj' in response.context)
        self.assertEqual(response.context['items_per_page'], 2)

    # test job_detail view

    def test_job_detail_view_url_exists_at_location(self):
        job = Job.objects.all()[1]
        response = self.client.get(f'/job_detail/{job.id}/')
        self.assertEqual(response.status_code, 200)

    def test_job_detail_view_url_accessible_by_name(self):
        job = Job.objects.all()[1]
        response = self.client.get(
            reverse('jobs:job_detail', args=[str(job.id)]))
        self.assertEqual(response.status_code, 200)

    def test_job_detail_view_uses_correct_template(self):
        job = Job.objects.all()[1]
        response = self.client.get(
            reverse('jobs:job_detail', args=[str(job.id)]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'jobs/job_detail.html')


# test loging required views

class JobAndTagTest(TestCase):
    def setUp(self):
        # ordinary users
        test_user1 = User.objects.create_user(
            username='testuser1', password='1X<ISRUkw+7HedYtuK')

        test_user1.save()
        
        test_user2 = User.objects.create_user(
            username='testuser2', password='2X<ISRUkw+7HedYtuK')

        test_user2.save()

        # super user
        test_super_user = User.objects.create_user(
            username='testSuperuser', password='superX<ISRUkw+7HedYtuK', is_superuser=True)
        
        test_super_user.save()
     

    # job not logged in test

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('jobs:create_job'))
        self.assertRedirects(
            response, '/user/login/?next=/create_job/')

    # job user logged in test
    def test_logged_in_uses_correct_template(self):
        login = self.client.login(
            username='testuser1', password='1X<ISRUkw+7HedYtuK')
        response = self.client.get(reverse('jobs:create_job'))

        # user logged in check
        self.assertEqual(str(response.context['user']), 'testuser1')
        # Response "success" check
        self.assertEqual(response.status_code, 200)

        # Correct template check
        self.assertTemplateUsed(
            response, 'jobs/create_job.html')

    # super user not logged in test
    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('jobs:create_tag'))
        self.assertRedirects(
            response, '/')

    # super user logged in test
    def test_logged_in_uses_correct_template(self):
        login = self.client.login(
            username='testSuperuser', password='superX<ISRUkw+7HedYtuK')
        response = self.client.get(reverse('jobs:create_tag'))

        # user logged in check
        self.assertEqual(str(response.context['user']), 'testSuperuser')
        # Response "success" check
        self.assertEqual(response.status_code, 200)

        # Correct template check
        self.assertTemplateUsed(
            response, 'jobs/create_tag.html')

    # user is not a super user test
    def test_logged_in_uses_correct_template(self):
        login = self.client.login(
            username='testuser1', password='1X<ISRUkw+7HedYtuK')
        response = self.client.get(reverse('jobs:create_tag'))
        self.assertRedirects(
            response, '/')

    # super user logged in, delete tag test
    def test_tag_delete_super_user(self):
        login = self.client.login(
            username='testSuperuser', password='superX<ISRUkw+7HedYtuK')
        tag = Tag.objects.create(name='test tag')
        self.assertEqual(tag.name, 'test tag')
        response = self.client.post(
            reverse('jobs:delete_tag', args=[str(tag.id)]))
        self.assertRedirects(
            response, reverse('jobs:list_tags'))
        self.assertEqual(response.status_code, 302)
        no_tag = Tag.objects.all().values()
        self.assertFalse(no_tag)

    # user not logged in, delete tag test
    def test_tag_delete_no_user(self):
        tag = Tag.objects.create(name='test tag')
        self.assertEqual(tag.name, 'test tag')
        response = self.client.post(
            reverse('jobs:delete_tag', args=[str(tag.id)]))
        self.assertRedirects(
            response, '/')

    # user logged in, user is not a super user, delete tag test
    def test_tag_delete_not_super_user(self):
        login = self.client.login(
            username='testuser1', password='1X<ISRUkw+7HedYtuK')
        tag = Tag.objects.create(name='test tag')
        self.assertEqual(tag.name, 'test tag')
        response = self.client.post(
            reverse('jobs:delete_tag', args=[str(tag.id)]))
        self.assertRedirects(
            response, '/')
        yes_tag = Tag.objects.all().values()
        self.assertTrue(yes_tag)

    # delete job test, correct user logged in
    def test_job_delete_correct_user(self):
        login = self.client.login(
            username='testuser1', password='1X<ISRUkw+7HedYtuK')
        job = Job.objects.create(title='Test title', company='Test company', location='Test location', email='testemail@test.com',
                                 website='www.testwebsite.com', description='Test description', custom_tags='tag1, tag2, tag3')
        job.user_id = login
        job.save()
        self.assertEqual(job.title, 'Test title')
        response = self.client.post(
            reverse('jobs:delete_job', args=[str(job.id)]))
        self.assertRedirects(
            response, reverse('jobs:jobs_list'))
        self.assertEqual(response.status_code, 302)
        no_job = Job.objects.all().values()
        self.assertFalse(no_job)

    # delete job test, incorrect user logged in
    def test_job_delete_incorrect_user(self):
        user=User.objects.first()
        job = Job.objects.create(title='Test title', company='Test company', location='Test location', email='testemail@test.com',
                                 website='www.testwebsite.com', description='Test description', custom_tags='tag1, tag2, tag3', user_id=user.id)

        self.assertEqual(job.title, 'Test title')
        login = self.client.login(
            username='testuser2', password='2X<ISRUkw+7HedYtuK')
        response = self.client.post(
            reverse('jobs:delete_job', args=[str(job.id)]))
        self.assertRedirects(
            response, '/')
        self.assertEqual(response.status_code, 302)
        yes_job = Job.objects.all().values()
        self.assertTrue(yes_job)

    # update job, correct user
    def test_job_update_correct_user(self):
        user=User.objects.first()
        job = Job.objects.create(title='Test title', company='Test company', location='Test location', email='testemail@test.com',
                                 website='www.testwebsite.com', description='Test description', custom_tags='tag1, tag2, tag3', user_id=user.id)
        self.assertEqual(job.title, 'Test title')
        login = self.client.login(
            username='testuser1', password='1X<ISRUkw+7HedYtuK')
        response = self.client.post(
            reverse('jobs:update_job', args=[str(job.id)]), {'title': 'Test title updated'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test title updated')

 
