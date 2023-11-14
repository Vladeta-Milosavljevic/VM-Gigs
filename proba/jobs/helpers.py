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
    except:
        items_per_page = 2
      
    if items_per_page is 0 | items_per_page >6:
            items_per_page = 2 
             
    paginator = Paginator(jobs, items_per_page)

    try:
        page_obj = paginator.page(page)
    except InvalidPage:
        page_obj = paginator.page(1)
        page=1

    # # ako se rucno ubaci string
    # try:
    #     items_per_page = int(items_per_page)
    # except:
    #     items_per_page = 2

    # # ako se rucno ubaci preveliki broj poslova po stranici
    # if items_per_page > 6 or items_per_page == 0:
    #     items_per_page = 2
    # paginator = Paginator(jobs, items_per_page)
    # page = request.GET.get('page', 1)

    # # ako se rucno ubaci string
    # try:
    #     page = int(page)
    # except:
    #     page = 1

    # # ako se rucno ubaci nepostojeca stranica
    # if len(jobs) % 2 == 0:
    #     if page > int(len(jobs)/items_per_page) or page == 0:
    #         page = 1
    # else:
    #     if page > int(len(jobs)/items_per_page)+1 or page == 0:
    #         page = 1

    # page_obj = paginator.get_page(page)
    page_range = paginator.get_elided_page_range(
        number=page, on_each_side=1, on_ends=1)

    return page_obj, page_range, items_per_page
