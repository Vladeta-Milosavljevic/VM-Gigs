from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.core.paginator import Paginator, InvalidPage


def send_application(request, form):
    email_title = str(form.cleaned_data.get('job_name')) + \
        ' - application for Mr/Ms ' + str(form.cleaned_data.get('name'))
    body = render_to_string('jobs/components/email.html', {
        'name': form.cleaned_data.get('name'),
        'intro': form.cleaned_data.get('intro')
    })
    job_email = form.cleaned_data.get('job_email')
    files = request.FILES.getlist('files')
    email = EmailMessage(
        email_title,
        body,
        'admin@proba.com',
        [job_email]
    )
    for file in files:
        email.attach(file.name, file.read(), file.content_type)
    email.send()


def pagination(request, jobs):
    page = request.GET.get('page', 1)

    # izbacivanje netacnih podataka
    try:
        items_per_page = int(request.GET.get('items_per_page', 2))
        items_per_page = 2 if items_per_page == 0 or items_per_page > 6 else items_per_page
    except:
        items_per_page = 2

    paginator = Paginator(jobs, items_per_page)
    
    try:
        page = int(request.GET.get('page', 1))
        page = 1 if page==0 or page > paginator.num_pages else page    
    except:
        page=1
    try:
        page_obj = paginator.page(page)
    except InvalidPage:
        page_obj = paginator.page(1)
        page = 1
   
    page_range = paginator.get_elided_page_range(
        number=page, on_each_side=1, on_ends=1)

    return page_obj, page_range, items_per_page
