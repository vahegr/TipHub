import videos.models
from django.db import models
from django.utils import timezone


class NotificationManager(models.Manager):
    def get_notification_count(self, user):
        # Gets the comments data grouped by (post_id, receiver, category) which are not read
        #notifs_count = (Notification.objects.filter(is_read=False, receiver=user).values('receiver', 'category', 'post_id').annotate(dcount=Count('id')))
        notifs_count = videos.models.Notification.objects.filter(
            is_read=False, receiver=user).order_by('-notification_date')

        # List to store the required data as dictionary.
        notif_data = list()

        for item in notifs_count:
            n_post_id = item.post_id
            if n_post_id != -1:
                n_slug = videos.models.Video.objects.values('slug').filter(id=n_post_id).first()['slug']
            else:
                n_slug = None
            n_count = item.n_count
            n_sender = item.sender
            n_timestamp = item.notification_date
            n_jalali_date = item.jalali_created

            # Appending the above data as dictionary to notif_data list
            notif_data.append({'n_post_id': n_post_id, 'n_count': n_count, 'n_sender': n_sender,
                               'n_timestamp': n_timestamp, 'jalali_created': n_jalali_date, 'n_slug': n_slug})

        return notif_data

    def add_notification(self, sender, receiver, category, post_id):
        existing = videos.models.Notification.objects.filter(
            receiver=receiver, category=category, is_read=False, post_id=post_id)
        if existing.exists():
            upd_existing = existing.first()
            upd_existing.sender = sender
            upd_existing.notification_date = timezone.now()
            upd_existing.n_count += 1
            upd_existing.save()
        else:
            new_notif = videos.models.Notification(
                sender=sender, receiver=receiver, is_read=False, category=category, post_id=post_id)
            new_notif.save()

    def remove_notification(self, sender, receiver, category, post_id):
        notif = videos.models.Notification.objects.filter(
            receiver=receiver, category=category, post_id=post_id, is_read=False).first()
        if notif:
            if notif.n_count == 0:
                notif.delete()
            else:
                notif.n_count -= 1
                notif.save()
