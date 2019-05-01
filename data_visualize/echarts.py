from pyecharts.charts import Page, Pie, Bar, WordCloud
from pyecharts import options as opts
from pyecharts.render import make_snapshot
from pyecharts.globals import SymbolType, ThemeType
# 使用 snapshot-selenium 渲染图片
from snapshot_selenium import snapshot


class charts():
    # 条形图
    def bar(self, key, value, city, title, subtitle) -> Bar:
        c = (
            Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
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
        c = (
            WordCloud()
                .add("", word, word_size_range=[20, 100], shape=SymbolType.DIAMOND)
                .set_global_opts(title_opts=opts.TitleOpts(title=title))
        )
        return c
