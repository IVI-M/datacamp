# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 01:34:07 2018

@author: d91067
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 17:22:49 2017

@author: d91067
"""
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from numpy.random import random
path = 'C:\\Users\\d91067\\Desktop\\R\\datacamp\\02_Python\\13_Interactive_Data_Visualization_with_Bokeh'
# path = 'C:\\Users\\georg\\Desktop\\georgi\\github\\datacamp\\02_Python\\13_Interactive_Data_Visualization_with_Bokeh'
os.chdir(path)

# Import figure from bokeh.plotting
from bokeh.plotting import figure
# Import output_file and show from bokeh.io
from bokeh.io import output_file, show
# Import the ColumnDataSource class from bokeh.plotting
from bokeh.plotting import ColumnDataSource
# import the HoverTool
from bokeh.models import HoverTool
#Import CategoricalColorMapper from bokeh.models
from bokeh.models import CategoricalColorMapper
# Import row from bokeh.layouts
from bokeh.layouts import row, column
# # Import gridplot from bokeh.layouts
from bokeh.layouts import gridplot
# Import Panel from bokeh.models.widgets
from bokeh.models.widgets import Panel, Tabs


# Perform necessary imports
from bokeh.io import curdoc
from bokeh.plotting import figure
# Perform the necessary imports
from bokeh.io import curdoc
from bokeh.layouts import widgetbox, column
from bokeh.models import Slider, ColumnDataSource







# How to combine Bokeh models into layouts
N = 300
x = random(N)
y = np.sin(x)
slider = Slider(title='my slider', start=1, end=10, step=1, value=1)
# Create ColumnDataSource: source
plot = figure()
source = ColumnDataSource(data={'x': x, 'y': y})
# Add a line to the plot
plot.line('x', 'y', source=source)
# Create a column layout: layout
layout = column(widgetbox(slider), plot)
# Add the layout to the current document
curdoc().add_root(layout)


# Define a callback function: callback
def callback(attr, old, new):
    # Read the current value of the slider: scale
    scale = slider.value
    # Compute the updated y using np.sin(scale/x): new_y
    new_y = np.sin(scale/x)
    # Update source with the new data values
    source.data = {'x': x, 'y': new_y}
# Attach the callback to the 'value' property of slider
slider.on_change('value', callback)
# Create layout and add to current document
layout = column(widgetbox(slider), plot)
curdoc().add_root(layout)