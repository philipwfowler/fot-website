from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from .forms import ContactForm
from .pricing import get_pricing
from .services import get_additional_services
from .standards import get_standards
def home(request):
    return render(request, "home.html", {"pricing": get_pricing(), "additional_services": get_additional_services(), "standards": get_standards()})
def contact(request):
    sent = False
    form = ContactForm(request.POST or None)
    if request.method == "POST" and form.is_valid() and not form.cleaned_data["website"]:
        data = form.cleaned_data
        send_mail(f"Website enquiry from {data['name']}", f"From: {data['email']}\\n\\n{data['message']}", settings.DEFAULT_FROM_EMAIL, [settings.CONTACT_EMAIL], reply_to=[data["email"]])
        sent = True
        form = ContactForm()
    return render(request, "contact.html", {"form": form, "sent": sent})
