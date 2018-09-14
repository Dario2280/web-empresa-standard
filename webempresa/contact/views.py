from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm
# Create your views here.

def contact(request):
    contact_form = ContactForm()
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            #enviamos el correo y redireccionamos el contenido
            email = EmailMessage(
                "La Caffetiera : Nuevo Mensaje de contacto",
                "De {} <{}>\n\nEscribio: \n\n {}".format(name, email, content),
                "no-contestar@inbox.mailtrap.io",
                ["dario2280@hotmail.com"],
                reply_to=[email]
            )

            try:
                email.send()
                #si todo va biene soto debe pasar
                return redirect(reverse('contact')+"?ok")
            except:       
                #si algo anda mal eso debe suceder
                return redirect(reverse('contact')+"?fail")

    return render(request, "contact/contact.html",{'form':contact_form}) 

