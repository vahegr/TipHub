from videos.models import Category
from home.models import ContactInfo


def categories(request):
    category = Category.objects.all()

    return {
        'categories': category,

    }


def contact_info(request):
    contact = ContactInfo.objects.get(allowing=True)

    return{
        'contact_info': contact,
    }
