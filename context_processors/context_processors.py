from videos.models import Category
from home.models import ContactInfo


def categories(request):
    category = Category.objects.all()

    return {
        'categories': category,

    }


def contact_info(request):
    contact = ContactInfo.objects.get(id=1)

    return{
        'contact_info': contact,
    }
