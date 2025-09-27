# 事件转换

```python
message_data = {
        "message_info": {
            "message_id": f"msg_{int(time.time())}",
            "time": time.time(),
            "user_info": {
                "user_id": "12345",
                "user_nickname": "测试用户",
                "platform": "test_platform",
                "user_cardname": "测试卡片名"
            },
            "platform": "test_platform",
            "group_info": {  # 群聊消息，私聊时设为None
                "group_id": "67890",
                "group_name": "测试群组",
                "platform": "test_platform"
            }
        },
        "message_segment": {
            "type": "text",
            "data": "这是一条测试消息"
        },
        "raw_message": "这是一条测试消息"
    }

    await chat_bot.message_process(message_data)
```
