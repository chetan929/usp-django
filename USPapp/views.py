from django.shortcuts import render
from .forms import ContactForm
from django.contrib import messages
from django.shortcuts import redirect
from django.conf import settings



def index(request):
    return render(request, 'USPapp/index.html')


def about(request):
    return render(request, 'USPapp/About.html')


def faq(request):
    return render(request, 'USPapp/FAQ.html')


def it_solutions(request):
    return render(request, 'USPapp/IT-solutions.html')


def overview(request):
    return render(request, 'USPapp/overview.html')


def privacy_policy(request):
    return render(request, 'USPapp/privacy-policy.html')


def contact_view(request):
    return render(request, 'USPapp/contact-us.html')


from django.core.mail import send_mail
from django.shortcuts import render
from .forms import ContactForm
from django.contrib import messages


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            sms_consent = form.cleaned_data['smsConsent']

            subject = f"New Contact Message from {name}"
            email_message = f"""
Name: {name}
Email: {email}
Consent: {'Yes' if sms_consent else 'No'}

Message:
{message}
            """

            try:
                # ✅ use your Gmail (EMAIL_HOST_USER) as sender
                send_mail(
                    subject,
                    email_message,
                    settings.EMAIL_HOST_USER,  # ✅ not hardcoded
                    ['prajapatiayush1222@gmail.com'],  # receiver
                    fail_silently=False,
                )
                messages.success(request, "Thank you! Your message has been sent successfully.")
            except Exception as e:
                messages.error(request, "There was an error sending your message.")
                print(f"Email send error: {e}")

            return redirect('contact')  # ✅ ensures only one message shows on refresh
    else:
        form = ContactForm()

    return render(request, 'USPapp/contact-us.html', {'form': form})
