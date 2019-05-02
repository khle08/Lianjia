from example.commons import Faker
from pyecharts import options as opts
from pyecharts.charts import Funnel, Page
from pyecharts.render import make_snapshot
# 使用 snapshot-selenium 渲染图片
from snapshot_selenium import snapshot


def funnel_label_inside(key,value,title) -> Funnel:

    c = (
        Funnel()
        .add(
            "商品",
            [list(z) for z in zip(key, value)],
            label_opts=opts.LabelOpts(position="inside"),
        )
        .set_global_opts(title_opts=opts.TitleOpts(title=title))
    )
    make_snapshot(snapshot, c.render(),
                  "Funnel.gif")
    return c
key = ['Locals路客', '链家', '寓艺公寓', '馨馨宾馆', '华舒酒店', '可可酒店', '美人鱼酒店公寓', '遇见青苹果', '德联租房', '郑州1+公寓']
value = [5083, 3102, 2300, 2250, 2200, 2050, 2000, 1950, 1460, 1450]
funnel_label_inside(key,value,'aaa')