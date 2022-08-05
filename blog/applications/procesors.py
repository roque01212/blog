from .home.models import Home

#procesor para recuprar telefon y correo del registro Home

def home_contact(request):
    home=Home.objects.latest('created')

    return{
        'phone':home.phone,
        'correo':home.contact_email,
    }