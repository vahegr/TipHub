from videos.models import Category
from home.models import ContactInfo


def categories(request):
    category = Category.objects.all()
    contact_info = ContactInfo.objects.get(allowing=True)

    return {
        'categories': category,
        'contact_info': contact_info,
    }
