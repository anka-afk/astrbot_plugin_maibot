"""
MaiBot 端处理器
接受: 已转换后的 MaiBot 事件, 进行处理
"""

from ...MaiBot.src.chat.message_receive.bot import chat_bot
from ...MaiBot.src.plugin_system.apis import send_api


class MaiBotProcessor:
    def __init__(self):
        pass

    async def handle_maibot_event(self, event):
        pass
