from pkg.plugin.models import *
from pkg.plugin.host import EventContext, PluginHost
import plugins.emoticon.config as config

"""
多段回复
"""

# 注册插件
@register(name="SplitNewline", description="多段回复", version="0.1", author="cillow")
class SplitNewlinePlugin(Plugin):
    # 定义一个函数，接受一个事件名和一个字典作为参数
    # 当收到GPT回复时触发

    @on(NormalMessageResponded)
    def on_event(self, event: EventContext, **kwargs):
        # 判断事件名是否是NormalMessageResponded
        # 获取事件参数中的响应文本
        response_text = kwargs["response_text"]
        # 判断响应文本是否包含换行符
        if "\n" in response_text:
            # 按换行符分割响应文本
            parts = response_text.split("\n")
            # 创建一个空列表，用来存储修改后的回复消息组件
            reply = []
            # 遍历每个部分
            for part in parts:
                # 把当前部分作为一个文字消息组件添加到回复列表中
                reply.append({"type": "text", "data": {"text": part}})
            # 返回修改后的回复列表，替换原始回复
            return {"reply": reply}
            # debug 输出内容
            logging.debug(reply)

        

    # 插件卸载时触发
    def __del__(self):
        pass