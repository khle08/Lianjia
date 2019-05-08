from wtforms import StringField, SubmitField, SelectMultipleField, SelectField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
from lianjia.constants import *


class SearchForm(FlaskForm):
    search_type = SelectField('请选择房产类型:',
                              validators=[DataRequired()], coerce=int,
                              choices=search_type)
    search = StringField('请输入要搜索的房产数据:', validators=[DataRequired()])
    submit = SubmitField('搜索')


class NewhouseDropDownListForm(FlaskForm):
    city = SelectField('请选择城市:', validators=[DataRequired()], coerce=int,
                       choices=newhouse_city_form)
    analysis = SelectField('请选择分析视角:', validators=[DataRequired()], coerce=int,
                           choices=newhouse_analysis_form)
    submit = SubmitField('查询')


class ErshoufangDropDownListForm(FlaskForm):
    city = SelectField('请选择城市:', validators=[DataRequired()], coerce=int,
                       choices=ershoufang_city_form)
    analysis = SelectField('请选择分析视角:', validators=[DataRequired()], coerce=int,
                           choices=ershoufang_analysis_form)
    submit = SubmitField('查询')


class RentDropDownListForm(FlaskForm):
    city = SelectField('请选择城市:', validators=[DataRequired()], coerce=int,
                       choices=rent_city_form)
    analysis = SelectField('请选择分析视角:', validators=[DataRequired()], coerce=int,
                           choices=rent_analysis_form)
    submit = SubmitField('查询')
