from channels.generic.websocket import AsyncJsonWebsocketConsumer


class NotificationConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        if self.scope["user"].is_authenticated:
            await self.accept()
            await self.channel_layer.group_add("alluser", self.channel_name)
            await self.channel_layer.group_add(
                str(self.scope["user"].id), self.channel_name
            )

            print(
                f"""Added {self.channel_name} channel to alluser and {self.scope["user"].id}"""
            )

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("alluser", self.channel_name)
        await self.channel_layer.group_discard(
            str(self.scope["user"].id), self.channel_name
        )
        print(
            f"""Removed {self.channel_name} channel to all-users and {self.scope["user"].id}"""
        )

    async def to_user(self, event):
        await self.send_json(event)
        print(f"Got message {event} at {self.channel_name}")
