from pkg.plugin.models import *
from pkg.plugin.host import EventContext, PluginHost
import re
from time import sleep

"""
多段回复
"""


# 注册插件
@register(name="SplitNewline", description="多段回复", version="0.1", author="ciallo")
class SplitNewlinePlugin(Plugin):

    # 插件加载时触发
    # plugin_host (pkg.plugin.host.PluginHost) 提供了与主程序交互的一些方法，详细请查看其源码
    def __init__(self, plugin_host: PluginHost):
        pass

    # 定义一个函数，接受一个事件名和一个字典作为参数
    # 当收到GPT回复时触发
    @on(NormalMessageResponded)
    def on_event(self, event: EventContext, **kwargs):
        # 获取事件参数中的响应文本
        responses_text = kwargs['response_text']

        pattern = "·"

        parts = re.split(pattern, responses_text)

        # 遍历列表中的每个元素
        for msg in parts:
            
            # send_person_message
            host: pkg.plugin.host.PluginHost = kwargs['host']
            host.send_person_message(kwargs['launcher_id'], msg) if kwargs['launcher_type'] == 'person' else host.send_group_message(
                kwargs['launcher_id'], msg)
        event.prevent_default()
        event.prevent_postorder()
        
    # 插件卸载时触发
    def __del__(self):
        pass
