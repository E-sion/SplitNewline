from pkg.plugin.models import *
from pkg.plugin.host import EventContext, PluginHost

"""
多段回复
"""

# 注册插件
@register(name="SplitNewline", description="多段回复", version="0.1", author="cillow")
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
        response_text:str = kwargs['response_text']

        # 判断响应文本是否包含换行符
        def print_split(s):
             # 用·符号分割字符串，得到一个列表
            parts = s.split('·')
             # 遍历列表中的每个元素
            for part in parts:
            # 打印元素
                event.add_return("reply", [reply])
        # 回复消息
        print_split(response_text)
        
        # 阻止该事件默认行为（向接口获取回复）
        event.prevent_default()
        event.prevent_postorder()

        
        

    # 插件卸载时触发
    def __del__(self):
        pass
