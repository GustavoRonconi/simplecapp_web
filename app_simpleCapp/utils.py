from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


def send_notifications(message, all_user=False, specific_user=None):
    """Function to send notifications to alluser or specific user group channel"""
    channel_layer = get_channel_layer()
    group = specific_user
    if all_user and not (specific_user):
        group = "alluser"

    async_to_sync(channel_layer.group_send)(
        group, {"type": "to.user", "event": f"{message}"},
    )
