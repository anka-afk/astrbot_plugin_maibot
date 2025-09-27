from astrbot.api.event import AstrMessageEvent, filter
from astrbot.api.star import Context, Star, register


class MaiBot(Star):
    def __init__(self, context: Context):
        super().__init__(context)

    async def terminate(self):
        pass
