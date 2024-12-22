from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Notification

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_notifications(request):
    notifications = Notification.objects.filter(recipient=request.user, read=False).order_by('-timestamp')
    
    # Mark notifications as read when retrieved
    notifications.update(read=True)
    
    # Serialize the notifications
    notification_data = [{
        "actor": notification.actor.username,
        "verb": notification.verb,
        "target": str(notification.target),  # Could be post title, or other related content
        "timestamp": notification.timestamp,
        "read": notification.read
    } for notification in notifications]

    return Response(notification_data, status=status.HTTP_200_OK)
