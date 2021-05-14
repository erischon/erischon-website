from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import render_to_string
from .forms import ContactForm


def home(request):
    return redirect('portfolio-hp')

def contactView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        subject = "Message venant de erischon.dev"
        email_template_name = "website/email/contact_email.txt"
        
        if form.is_valid():
            content = {
                'from_email': form.cleaned_data['from_email'],
                'message': form.cleaned_data['message'],
            }
            
            email = render_to_string(email_template_name, {'content': content})

            try:
                send_mail(subject, email, 'contact@erischon.dev', ['contact@erischon.dev'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('home')
    return render(request, 'home', {'form': form})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')
    # return render(request, "website/email.html", {'form': form})
