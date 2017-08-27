import os
import channels.asgi

os.environ["DJANGO_SETTINGS_MODULE"] = "config.settings.chat_local"
channel_layer = channels.asgi.get_channel_layer()
