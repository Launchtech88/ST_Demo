import pandas as pd
import streamlit as st
from pyecharts import options as opts
from pyecharts.charts import Bar
from streamlit_echarts import st_pyecharts


def charts(xdata, y):
    bar = (
        Bar()
        .add_xaxis(xdata)
        .add_yaxis('1', y[0], stack="stack1", color='Blue')
        .add_yaxis('2', y[1], stack="stack1", color='DarkCyan')
        .add_yaxis('3', y[2], stack="stack1", color='Purple')
        .add_yaxis('4', y[3], stack="stack1", color='Green')
        .add_yaxis('5', y[4], stack="stack1", color='Orange')
        .set_series_opts(label_opts=opts.LabelOpts(position="inside", color="white", font_size=15))
        # 全局配置：标题/副标题
        .set_global_opts(title_opts=opts.TitleOpts(title="满意度与课前准备行为相关性", pos_left='center'),
                         tooltip_opts=opts.TooltipOpts(trigger='axis', axis_pointer_type='cross'),  # 指示器类型，十字/阴影/直线/无
                         toolbox_opts=opts.ToolboxOpts(is_show=True),
                         legend_opts=opts.LegendOpts(pos_left='-2%'))

    )
    return bar


file = st.sidebar.file_uploader('请上传表格', ['.xlsx'])
if file:
    df = pd.read_excel('线上学习调查问卷.xlsx', sheet_name='Sheet1')
    x_data = df['1、对线上学习效果的自我满意度评价是？'].to_list()
    y_data = df['2、线上学习前，我会提前做好课前准备，如预习课程内容、准备相关课本笔记、调好上网设备等'].to_list()
    xy_data = tuple(zip(x_data, y_data))
    xdata = ['0-20', '21-40', '41-60', '61-80', '81-100']
    ydata = {'0-20': {1:0, 2:0, 3:0, 4:0, 5:0}, '21-40': {1:0, 2:0, 3:0, 4:0, 5:0}, '41-60': {1:0, 2:0, 3:0, 4:0, 5:0}, '61-80': {1:0, 2:0, 3:0, 4:0, 5:0}, '81-100': {1:0, 2:0, 3:0, 4:0, 5:0}}
    for item in xy_data:
        for j in xdata:
            if int(j.split('-')[0]) <= item[0] < int(j.split('-')[1]):
                for i in range(1, 6):
                    if item[1] == i:
                        ydata[j][i] += 1
    y = []
    for i in range(1, 6):
        d = []
        for key, value in ydata.items():
            d.append('' if value[i] == 0 else value[i])
        y.append(d)

    st_pyecharts(charts(xdata, y))
