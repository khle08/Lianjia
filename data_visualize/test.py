from example.commons import Faker
from pyecharts import options as opts
from pyecharts.charts import Bar, Pie,Line3D
from pyecharts.render import make_snapshot
# 使用 snapshot-selenium 渲染图片
from snapshot_selenium import snapshot
from pyecharts.globals import ThemeType
import math


class lianjia_visual():
    def __int__(self, params):
        data = []
        self.choose = params['choose']
        self.values = params['values']
        self.title = params['title']
        self.subtitle = params['subtitle']
        self.y_title = params['y_title']
        self.filename = params['filename']
        self.params = params

    def bar_base(self) -> Bar:
        c = (
            Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
                .add_xaxis(self.params['choose'])
                .add_yaxis(self.y_title, self.params['values'])
                # .add_yaxis("商家B", Faker.values(), is_selected=False)
                .set_global_opts(title_opts=opts.TitleOpts(title=self.params['title'],
                                                           subtitle=self.params['subtitle']))
        )
        make_snapshot(snapshot, c.render(), "{}.png".format(self.params['filename']))
        return c

    def pie_base(self) -> Pie:
        c = (
            Pie()
                .add("", [list(z) for z in zip(self.params['choose'], self.params['values'])])
                .set_global_opts(title_opts=opts.TitleOpts(title=self.params['title']))
                .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
        )
        make_snapshot(snapshot, c.render(), "{}.png".format(self.params['filename']))
        return c


# print(Faker.choose())
# print(Faker.values())
# ['小米', '三星', '华为', '苹果', '魅族', 'VIVO', 'OPPO']
# [103, 50, 116, 25, 95, 73, 66]
def line3d_auto_rotate() -> Line3D:
    data = []
    for t in range(0, 25000):
        _t = t / 1000
        x = (1 + 0.25 * math.cos(75 * _t)) * math.cos(_t)
        y = (1 + 0.25 * math.cos(75 * _t)) * math.sin(_t)
        z = _t + 2.0 * math.sin(75 * _t)
        data.append([x, y, z])
    c = (
        Line3D()
        .add(
            "",
            data,
            xaxis3d_opts=opts.Axis3DOpts(Faker.clock, type_="value"),
            yaxis3d_opts=opts.Axis3DOpts(Faker.week_en, type_="value"),
            grid3d_opts=opts.Grid3DOpts(
                width=100, depth=100, rotate_speed=150, is_rotate=True
            ),
        )
        .set_global_opts(
            visualmap_opts=opts.VisualMapOpts(
                max_=30, min_=0, range_color=Faker.visual_color
            ),
            title_opts=opts.TitleOpts(title="Line3D-旋转的弹簧"),
        )
    )
    make_snapshot(snapshot, c.render(), "{}.gif".format('line3d'))
    return c

line3d_auto_rotate()