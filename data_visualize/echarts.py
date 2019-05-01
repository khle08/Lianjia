from pyecharts.charts import Page, Pie, Bar, WordCloud, Scatter
from pyecharts import options as opts
from pyecharts.globals import SymbolType, ThemeType
import random


class charts():
    # 条形图
    def bar(self, key, value, city, title, subtitle) -> Bar:
        theme = [
            ThemeType.LIGHT, ThemeType.DARK, ThemeType.WHITE, ThemeType.CHALK,
            ThemeType.ESSOS, ThemeType.INFOGRAPHIC, ThemeType.MACARONS, ThemeType.PURPLE_PASSION,
            ThemeType.ROMA, ThemeType.ROMANTIC, ThemeType.SHINE, ThemeType.VINTAGE,
            ThemeType.WALDEN, ThemeType.WESTEROS, ThemeType.WONDERLAND
        ]
        c = (
            Bar(init_opts=opts.InitOpts(theme=random.choice(theme)))
                .add_xaxis(key)
                .add_yaxis(city, value)
                .set_global_opts(title_opts=opts.TitleOpts(title=title, subtitle=subtitle),
                                 toolbox_opts=opts.ToolboxOpts(),
                                 legend_opts=opts.LegendOpts(is_show=False)
                                 )
        )
        return c

    # 饼图
    def pie(self, key, value, title) -> Pie:
        c = (
            Pie()
                .add("", [list(z) for z in zip(key, value)])
                .set_global_opts(title_opts=opts.TitleOpts(title=title))
                .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
        )
        return c

    # 词云图
    def wordcloud(self, word, title) -> WordCloud:
        c = (
            WordCloud()
                .add("", word, word_size_range=[20, 100])
                .set_global_opts(title_opts=opts.TitleOpts(title=title))
        )
        return c

    def wordcloud_diamond(self, word, title) -> WordCloud:
        shape = [SymbolType.ARROW, SymbolType.DIAMOND, SymbolType.RECT,
                 SymbolType.ROUND_RECT, SymbolType.TRIANGLE]
        c = (
            WordCloud()
                .add("", word, word_size_range=[20, 100], shape=random.choice(shape))
                .set_global_opts(title_opts=opts.TitleOpts(title=title))
        )
        return c

    # 散点图显示分割线
    def scatter_spliteline(self, key, value, city, title) -> Scatter:
        c = (
            Scatter()
                .add_xaxis(key)
                .add_yaxis(city, value)
                .set_global_opts(
                title_opts=opts.TitleOpts(title=title),
                xaxis_opts=opts.AxisOpts(splitline_opts=opts.SplitLineOpts(is_show=True)),
                yaxis_opts=opts.AxisOpts(splitline_opts=opts.SplitLineOpts(is_show=True)),
            )
        )
        return c

    def scatter_visualmap_color(self, key, value, city, title) -> Scatter:
        c = (
            Scatter()
                .add_xaxis(key)
                # .add_yaxis("商家A", Faker.values())
                .add_yaxis(city, value)
                .set_global_opts(
                title_opts=opts.TitleOpts(title=title),
                visualmap_opts=opts.VisualMapOpts(type_="size", max_=150, min_=20),
            )
        )
        # c.render("scrtter_visual_map.html")
        # make_snapshot(snapshot, c.render(), "scatter_visual_map_color.gif")
        return c
