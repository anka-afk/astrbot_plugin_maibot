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
                    "user_cardname": event.message_obj.sender.nickname,  # AstrBot 没有同时保存两个东西
                    "platform": "astrbot_platform",
                },
                "group_info": {
                    "group_id": event.message_obj.group.group_id,
                    "group_name": event.message_obj.group.group_name,
                    "platform": "astrbot_platform",
                },
                "additional_config": None,
                "format_info": {"content_format": "", "accept_format": ""},
                "template_info": {
                    "template_default": True,
                    "template_name": None,
                    "template_items": {},
                },
            },
            "message_segment": {"type": "text", "data": event.message_obj.message},
            "raw_message": event.message_obj.raw_message,
            "processed_plain_text": event.message_str,
        }
        return maibot_message_data

    @classmethod
    def convert_to_astrbot_event(cls, event):
        pass
