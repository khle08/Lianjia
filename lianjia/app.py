from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from lianjia.form import *
from lianjia.list import *
from lianjia.search import es_search

app = Flask(__name__)
# csrf保护密匙
app.config['SECRET_KEY'] = 'dfjhiFHBCUDHBVdbvbHXbfgnghklVJfuhkbfgv'
app.config['DEBUG'] = True
bootstrap = Bootstrap(app)
moment = Moment(app)


# manager = Manager(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = SearchForm()
    search = ''
    search_result = {}
    search_flag = 0
    if form.validate_on_submit():
        search = form.search.data
        search_type = form.search_type.data
        print(search)
        print(search_type)
        search_result = es_search(search_type, search)
        if search_result:
            search_flag = 1
    return render_template('index.html', form=form, search=search,
                           search_result=search_result, search_flag=search_flag)


# 新房分析中心
@app.route('/newhouse', methods=['GET', 'POST'])
def newhouse():
    form = NewhouseDropDownListForm()
    data = []
    # is_submit字段用于前端判断是否提交了表单
    is_submit = 0
    if form.validate_on_submit():
        is_submit = 1
        city = form.city.data
        analysis = form.analysis.data
        return_data = newhouse_list(city, analysis)
        data = return_data.parse()
    else:
        print("false")
    return render_template('newhouse.html', form=form, data=data, is_submit=is_submit)


# 二手房分析中心
@app.route('/ershoufang', methods=['GET', 'POST'])
def ershoufang():
    form = ErshoufangDropDownListForm()
    data = []
    is_submit = 0
    if form.validate_on_submit():
        print('success')
        is_submit = 1
        city = form.city.data
        analysis = form.analysis.data
        return_data = ershoufang_list(city, analysis)
        print(return_data)
        data = return_data.parse()
    else:
        print("false")
    return render_template('ershoufang.html', form=form, data=data, is_submit=is_submit)


@app.route('/rent', methods=['GET', 'POST'])
def rent():
    form = RentDropDownListForm()
    data = []
    is_submit = 0
    if form.validate_on_submit():
        print('success')
        is_submit = 1
        city = form.city.data
        analysis = form.analysis.data
        return_data = rent_list(city, analysis)
        data = return_data.parse()
    else:
        print("false")
    return render_template('rent.html', form=form, data=data, is_submit=is_submit)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run()
    # manager.run()
