from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView
from django.views.generic.edit import DeleteView, UpdateView
from .forms import JobForm, TagForm, ApplyForm
from .models import Tag, Job
from django.urls import reverse_lazy
from django.db.models import Q
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .custom_decorators import creator_only, creator_and_super_user_only, super_user_only
from .helpers import send_application, pagination


def index_view(request):
    return render(request, 'jobs/index.html', {'jobs': Job.objects.all().order_by('-id')[:3]})


def jobs_list(request):
    text = request.GET.get('text') if request.GET.get('text') else ''
    if text:
        jobs = []
        query = Job.objects.filter(
            Q(title__icontains=text) |
            Q(company__icontains=text) |
            Q(tags__name__icontains=text) |
            Q(custom_tags__icontains=text) |
            Q(location__icontains=text)
        ).all().order_by('-id')
        for item in query:  # izbacivanje duplikata u pretrazi
            if item not in jobs:
                jobs.append(item)
    else:
        jobs = Job.objects.all().order_by('-id')

    for job in jobs:
        job.custom_tags = job.custom_tags.split(',')

    page_obj, page_range, items_per_page = pagination(request, jobs)
    context = {
        'text': text,
        'page_obj': page_obj,
        'page_range': page_range,
        'items_per_page': items_per_page
    }
    return render(request, 'jobs/jobs_list.html', context)


def job_detail(request, pk):
    job = Job.objects.get(pk=pk)
    job.custom_tags = job.custom_tags.split(',')
    form = ApplyForm(initial={
        'job_name': job.title,
        'job_email': job.email
    })
    if request.method == 'POST':
        form = ApplyForm(request.POST, request.FILES)
        if form.is_valid():
            send_application(request, form)
            return redirect('jobs:index')
    return render(request, 'jobs/job_detail.html', {'job': job, 'form': form, 'visitor': True})


@login_required(login_url="login")
def create_job(request):
    form = JobForm(initial={'user': request.user})

    if request.method == 'POST':
        form = JobForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save()
            return redirect('jobs:index')

    return render(request, 'jobs/create_job.html', {'form': form})


@login_required(login_url="login")
def my_jobs(request):
    return render(request, 'jobs/my_jobs.html')


@login_required(login_url="login")
def my_jobs_ajax(request):
    jobs = Job.objects.filter(user_id=request.user)
    response = render_to_string(
        'jobs/my_jobs_list.html', {'jobs': jobs}, request)
    return HttpResponse(response, status=200)


@creator_only
def my_job_detail(request, pk):
    job = Job.objects.get(pk=pk)
    job.custom_tags = job.custom_tags.split(',')
    response = render_to_string(
        'jobs/my_job_detail.html', {'job': job, 'visitor': False})
    return HttpResponse(response, status=200)


@method_decorator(creator_only, name='dispatch')
class JobUpdateView(UpdateView):
    model = Job
    template_name_suffix = '_update'
    form_class = JobForm
    success_url = reverse_lazy('jobs:my_jobs')


@method_decorator(creator_and_super_user_only, name='dispatch')
class JobDeleteView(DeleteView):
    model = Job
    success_url = reverse_lazy('jobs:jobs_list')


@method_decorator(super_user_only, name='dispatch')
class TagTemplateView(TemplateView):
    template_name = 'jobs/tags.html'


@super_user_only
def tags_list_ajax(request):
    tags = Tag.objects.all()
    response = render_to_string('jobs/tags_list.html', {'tags': tags}, request)
    return HttpResponse(response, status=200)


@method_decorator(super_user_only, name='dispatch')
class TagCreateView(CreateView):
    model = Tag
    form_class = TagForm
    template_name = 'jobs/create_tag.html'
    success_url = reverse_lazy('jobs:create_tag')


@method_decorator(super_user_only, name='dispatch')
class TagDeleteView(DeleteView):
    model = Tag
    success_url = reverse_lazy('jobs:list_tags')
