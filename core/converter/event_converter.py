"""
事件转换器
静态类，负责转换事件格式
两个方向: AstrBot 事件 <-> MaiBot 事件
"""

from astrbot.api.event import AstrMessageEvent


class EventConverter:
    def __init__(self):
        pass

    @classmethod
    def convert_to_maibot_event(cls, event: AstrMessageEvent):
        maibot_message_data = {
            "message_info": {
                "platform": "astrbot_platform",
                "message_id": event.message_obj.raw_message.get("message_id", ""),
                "time": event.message_obj.timestamp,
                "user_info": {
                    "user_id": event.message_obj.sender.user_id,
                    "user_nickname": event.message_obj.sender.nickname,
                    "user_cardname": astrbot_message.get("user_cardname", ""),
                    "platform": "astrbot_platform",
                },
                "group_info": (
                    {
                        "group_id": (
                            str(astrbot_message["group_id"])
                            if astrbot_message.get("group_id")
                            else None
                        ),
                        "group_name": astrbot_message.get("group_name", ""),
                        "platform": "astrbot_platform",
                    }
                    if astrbot_message.get("group_id")
                    else None
                ),
                "additional_config": None,
                "format_info": {"content_format": "", "accept_format": ""},
                "template_info": {
                    "template_default": True,
                    "template_name": None,
                    "template_items": {},
                },
            },
            "message_segment": {"type": "text", "data": astrbot_message["content"]},
            "raw_message": astrbot_message["content"],
            "processed_plain_text": astrbot_message["content"],
        }

    @classmethod
    def convert_to_astrbot_event(cls, event):
        pass
