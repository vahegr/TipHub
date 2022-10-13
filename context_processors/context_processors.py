from videos.models import Category, Notification
from home.models import ContactInfo


def categories(request):
    category = Category.objects.all()

    return {
        'categories': category,

    }


def contact_info(request):
    contact = ContactInfo.objects.all().first()

    return{
        'contact_info': contact,
    }


def notifications_exist(request):
    if request.user.is_authenticated:
        unread_notifs = Notification.objects.get_notification_count(request.user)
        f = len(unread_notifs)

        status = True if f > 0 else False
        return {
            'status': status,
            'notif_count': f,
            'unread_notifs': unread_notifs,
        }
    else:
        status = False

    return {'status': status}
