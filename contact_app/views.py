from django.shortcuts import render, redirect, HttpResponse
from .forms import ContactForm
from django.core.mail import EmailMessage

# Create your views here.


def ContactView(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            EmailMessage(
                'Contact Form Submission form {}'.format(name),
                message,
                'sandbox.smtp.mailtrap.io',
                ['example_email@example.com'],
                [],
                reply_to=[email]).send()
            return redirect('success')
    else:
        form = ContactForm()
    return render(request, 'contact/contact.html', {
        'form': form
    })

def ContactSuccessView(request):
    return render(request, 'contact/success/contact_success.html')