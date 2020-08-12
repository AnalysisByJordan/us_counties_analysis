#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas
import numpy
import matplotlib
import matplotlib.pyplot as plt
#%matplotlib inline


# In[2]:


table = pandas.read_csv('counties.csv')
table


# In[14]:


scatter_plot = table.plot.scatter(
    x = 'PercentCollegeGrad', # x-axis
    y = 'IncomePerCapita', # y-axis
    s = table.Population/20000,   # size of the dot
    c = 'purple',
    alpha=0.3
)


# In[4]:


filtered = table[table['IncomePerCapita'] != 0]


# In[5]:


#Pearson_correlation_numerator
#X = IncomePerCapita
#Y = PercentCollegeGrad

x_bar = filtered.IncomePerCapita.mean()
y_bar = filtered.PercentCollegeGrad.mean()

list_x = []
x = 0 
for item in filtered.IncomePerCapita:
    x = (item - x_bar)
    list_x.append(x)

list_y = []
y = 0
for item in filtered.PercentCollegeGrad:
    y = (item - y_bar)
    list_y.append(y)

z = [list_x[i]*list_y[i] for i in range(len(list_x))]
numerator = sum(z)
numerator 


# In[6]:


#Pearson_correlation_denominator
#X = IncomePerCapita
#Y = PercentCollegeGrad

list_xx = []
xx = 0 
for item in filtered.IncomePerCapita:
    xx = (item - x_bar)**2
    list_xx.append(xx)
a = (sum(list_xx))**0.5

list_yy = []
yy = 0 
for item in filtered.PercentCollegeGrad:
    yy = (item - y_bar)**2
    list_yy.append(yy)
b = (sum(list_yy))**0.5

denominator = a * b


# In[7]:


Pearsons = numerator / denominator 
Pearsons


# In[8]:


#x = percent college grade
#y = income per capita
m, b = numpy.polyfit(filtered.PercentCollegeGrad, filtered.IncomePerCapita, 1 , rcond=None, full=False, w=None, cov=False)
mb = (m, b)
mb


# In[10]:


Regression_list = []
for i in filtered.PercentCollegeGrad:
    Regression = m * i + b
    Regression_list.append(Regression)

Income_list = []
for i in filtered.IncomePerCapita:
    Income_list.append(i)
Income_list

e = [Income_list[i]-Regression_list[i] for i in range(len(Income_list))]

table = filtered.assign(Error = e)

Error_list = table[['Name', 'State', 'Error']]
Error_list = Error_list.sort_values(['Error'], ascending=[False])
Error_list


# In[11]:


plot = table.plot.scatter(
    x='PercentCollegeGrad', 
    y='IncomePerCapita',
    c = abs(table.Error), 
    colormap=plt.cm.terrain,
    figsize=(10,7),
    sharex=False, 
)
plot.add_line(matplotlib.lines.Line2D([0, 50], [11694, 30801],               color="red"))
plot.annotate("Montgomery, VA",
            xy=(31.6,14185), xycoords='data',
            xytext=(25, 5000), textcoords='data',
            arrowprops=dict(arrowstyle="->",
                            connectionstyle="arc3"),
            )
plot                   

