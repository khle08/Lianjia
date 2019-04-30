from pyecharts.charts import Page, Pie, Bar, WordCloud
from pyecharts import options as opts
from pyecharts.render import make_snapshot
from pyecharts.globals import SymbolType
# 使用 snapshot-selenium 渲染图片
from snapshot_selenium import snapshot


class gen_charts():
    # 条形图
    def bar(self, key, value, title, subtitle) -> Bar:
        c = (
            Bar()
                .add_xaxis(key)
                .add_yaxis("商家B", value)
                .set_global_opts(title_opts=opts.TitleOpts(title=title, subtitle=subtitle))
        )
        make_snapshot(snapshot, c.render(), "{}.png".format(title))
        return c

    # 饼图
    def pie(self, key, value, title) -> Pie:
        c = (
            Pie()
                .add("", [list(z) for z in zip(key, value)])
                .set_global_opts(title_opts=opts.TitleOpts(title=title))
                .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
        )
        make_snapshot(snapshot, c.render(), "{}.png".format(title))
        return c

    def wordcloud(self, word, title) -> WordCloud:
        c = (
            WordCloud()
                .add("", word, word_size_range=[20, 100])
                .set_global_opts(title_opts=opts.TitleOpts(title=title))
        )
        make_snapshot(snapshot, c.render(), "{}.png".format(title))
        return c

    def wordcloud_diamond(self, word, title) -> WordCloud:
        c = (
            WordCloud()
                .add("", word, word_size_range=[20, 100], shape=SymbolType.DIAMOND)
                .set_global_opts(title_opts=opts.TitleOpts(title=title))
        )
        return c
