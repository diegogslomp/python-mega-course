from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool, ColumnDataSource
import pandas


df = pandas.read_csv('Times.csv', parse_dates=["Start","End"])

df["Start_"] = df["Start"].dt.strftime("%Y-%m-%d %H:%M:%S")
df["End_"] = df["End"].dt.strftime("%Y-%m-%d %H:%M:%S")

cds = ColumnDataSource(df)

p = figure(x_axis_type='datetime', height=400 ,responsive=True, title="Motion Graph", logo=None)

p.yaxis.minor_tick_line_color=None

p.ygrid[0].ticker.desired_num_ticks=1

hover=HoverTool(tooltips=[("Start", "@Start_"),("End", "@End_")])
p.add_tools(hover)

q = p.quad(left='Start', right='End', bottom=0, top=1, color='green', source=cds)

output_file("20186_motion_detector_plot.html")
show(p)
