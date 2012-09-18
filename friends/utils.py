import datetime

def get_datetime_now():
    """
    Returns datetime object with current point in time.

    In Django 1.4+ it uses Django's django.utils.timezone.now() which returns
    an aware or naive datetime that represents the current point in time
    when ``USE_TZ`` in project's settings is True or False respectively.
    In older versions of Django it uses datetime.datetime.now().

    """
    try:
        from django.utils import timezone
        return timezone.now()
    except ImportError:
        return datetime.datetime.now()

def make_friends(user1, user2):
    if not Friendship.objects().are_friends(user1, user2):
        if user1 != user2:
            friendship = Friendship(from_user=user1, to_user=user2)
            friendship.save()
            return true
    else:
        return false

def invite(user1, user2):
    if user1 == user2:
        raise ValueError(_(u"You can't request friendship with yourself."))
    if Friendship.objects.are_friends(user1, user2):
        raise  ValueError(_(u"You are already friends with %(username)s.") % {'username': user2.username})
    blocking = Blocking.objects.filter(from_user=user2, to_user=user1)
    if blocking.count() > 0:
        raise ValueError(_(u"You can't invite %(username)s to friends.") % {'username': user2.username})
    if FriendshipInvitation.objects().is_invited(user1, user2):
        raise ValueError(_(u"Already requested friendship with %(username)s.") % {'username': user2.username})
    invitation = FriendshipInvitation(from_user=user1, to_user=user2)
    invitation.save()
    return true