from astrbot.api.event import AstrMessageEvent, filter
from astrbot.api.star import Context, Star, register
from .core.converter.event_converter import EventConverter


class MaiBot(Star):
    def __init__(self, context: Context):
        super().__init__(context)

    # 注意现在只适配 aiocqhttp
    @filter.platform_adapter_type(filter.PlatformAdapterType.AIOCQHTTP)
    async def handle_astrbot_event(self, event: AstrMessageEvent):
        pass

    async def terminate(self):
        pass
