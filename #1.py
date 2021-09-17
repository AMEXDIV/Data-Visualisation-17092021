#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as Mat


# In[2]:


dataXAxis = np.array([1,20])
dataYAxis = np.array([10,1000])

# Plotting X-Axis and Y-Axis Data
Mat.plot(dataXAxis,dataYAxis)
# Giving names to X-Axis and Y-Axis.
Mat.xlabel("X-Axis")
Mat.ylabel("Y-Axis")
Mat.show()


# In[3]:


# The plot() function is used to draw points (markers) in a diagram.

# By default, the plot() function draws a line from point to point.

# The function takes parameters for specifying points in the diagram.

# Parameter 1 is an array containing the points on the x-axis.

# Parameter 2 is an array containing the points on the y-axis.

# If we need to plot a line from (1, 3) to (8, 10), we have to pass two arrays [1, 8] and [3, 10] to the plot function.


xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

Mat.plot(xpoints, ypoints)
Mat.show()

# The x-axis is the horizontal axis.

# The y-axis is the vertical axis.


# In[4]:


# To plot only the markers, you can use shortcut string notation parameter 'o', which means 'rings'.

xpoints = np.array([1, 8])
ypoints = np.array([3, 90])

Mat.plot(xpoints, ypoints, 'o')
Mat.show()


# In[5]:


# You can plot as many points as you like, just make sure you have the same number of points in both axis.

xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])

Mat.plot(xpoints, ypoints)
Mat.show()


# In[6]:


# Thats all for 17-09-2021 !

# Question --> What if we dosen't specify X-Axis or Y-Axis ?


"""
Downloadble things -->
pip install pandas 
pip install numpy
pip install matoplotlib
https://www.anaconda.com/products/individual
"""



# IF you see this file as a big trouble please download Anaconda Navigator.
# Change this file extension .py to .ipynb so that you can run it in Anaconda Navigator.

# https://www.anaconda.com/products/individual is link to download Anaconda Navigator.
