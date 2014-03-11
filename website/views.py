from django.shortcuts import render
from django.conf import settings
from django.core.mail import EmailMessage
from website.forms import ContactForm


def index(request):
    return render(request, 'website/page-home.html', dict(
        logo_version='light'
    ))


def product(request):
    return render(request, 'website/page-product.html', dict(
        logo_version='dark'
    ))


def about(request):
    return render(request, 'website/page-about.html', dict(
        logo_version='light'
    ))


def contact(request):
    if request.method == 'POST':  # if the form has been submitted
        form = ContactForm(request.POST)
        if form.is_valid():
            form_status = 'valid'

            # send the email to victoria's email

            sender = form.cleaned_data['fullname']
            email = form.cleaned_data['email']
            message = ''.join([
                form.cleaned_data['message'],
                "\n\n\n",
                sender, "\n",
                email
            ])

            email_title = settings.CONTACT_EMAIL_TITLE
            victoria_email = settings.CONTACT_RECIPIENT_EMAIL

            mail = EmailMessage(
                email_title,
                message,
                to=[victoria_email],
                headers={'Reply-To': email}
            )
            mail.send(fail_silently=False)

        else:
            form_status = 'invalid'
    else:
        form_status = 'unsent'
        form = ContactForm()  # an unbound form


    return render(request, 'website/page-contact.html', dict(
        logo_version='light',
        form=form,
        form_status=form_status
    ))