from django.urls import path

from . import views


app_name = "jobs"
urlpatterns = [
    path("", views.index_view, name="index"),
    path("list_tags/", views.TagTemplateView.as_view(), name="list_tags"),
    path("tags_ajax/", views.tags_list_ajax, name="tags_ajax"),
    path("create_tag/", views.TagCreateView.as_view(), name="create_tag"),
    path("delete_tag/<int:pk>", views.TagDeleteView.as_view(), name="delete_tag"),
    
    
    path("create_job/", views.create_job, name="create_job"),
    path("my_jobs/", views.my_jobs, name="my_jobs"),
    path("my_jobs_ajax/", views.my_jobs_ajax, name="my_jobs_ajax"),
    path("my_job_detail/<int:pk>/",
         views.my_job_detail, name="my_job_detail"),
    path("update_job/<int:pk>", views.JobUpdateView.as_view(), name="update_job"),
    path("delete_job/<int:pk>", views.JobDeleteView.as_view(), name="delete_job"),
    path("jobs_list/", views.jobs_list, name="jobs_list"),
    path("job_detail/<int:pk>/",
         views.job_detail, name="job_detail"),
]
