import re

url = 'https://image1.ljcdn.com/110000-inspection/e7018042-410f-4236-ae04-a7f154f4ea42.JPG.296x216.jpg.437x300.jpg'
print(len(url))
s = '<a href="https://bj.lianjia.com/xiaoqu/1111027374689/" target="_blank" data-log_index="10" data-el="region">国瑞城东区 1室1厅58.18平米南精装有电梯'
print(len(""".437x300.jpg"><div '
            'class="btn-follow follow" data-hid="101104153147"><span '
            'class="star"></span><span class="follow-text">关注</span></div><div '
            'class="leftArrow"><span></span></div><div '
            'class="rightArrow"><span></span></div><div '
            'class="price"><span>799</span>万</div></a><a class="title" '
            'href="https://bj.lianjia.com/ershoufang/101104153147.html" '
            'target="_blank" data-bl="list" data-log_index="1" '
            'data-housecode="101104153147" data-is_focus=""  '
            'data-el="ershoufang">两居室可改三居  满五公房  有小院 可停车  业主人好</a><div '
            'class="info">马甸<span>/</span"""))