#!/usr/bin/env python
# coding: utf-8

# In[1]:


import plotly.express as px


# In[2]:


t=px.line(x=[1,2,3,4,5],y=[1,2,3,4,5])
t.show()


# In[3]:


df=px.data.iris()
df


# In[4]:


g=px.line(df,x='species',y='petal_width')
g.show()


# In[5]:


df1=px.data.tips()
df1


# In[6]:


g1=px.line(df1,x='time',y='total_bill',color='sex',line_group='day',line_dash='smoker',hover_name='tip',title='Restaurant--Data')
g1.show()


# In[7]:


fig=px.bar(df,x='petal_width',y='petal_length')
fig.show()


# In[8]:


df2=px.data.medals_long()
df2


# In[9]:


med=px.bar(df2,x='nation',y='count',color='medal',title='olympic medals data')
med


# In[10]:


fig1=px.bar(df,x='sepal_width',y='sepal_length',color='species')
fig1.show()


# In[11]:


fig1=px.bar(df,x='sepal_width',y='sepal_length',color='species',barmode='group')
fig1.show()


# In[12]:


fig1=px.bar(df,x='sepal_width',y='sepal_length',color='species',barmode='overlay')
fig1.show()


# In[13]:


fig1=px.bar(df,x='sepal_width',y='sepal_length',color='species',barmode='group',facet_row='species')
fig1.show()


# In[14]:


fig1=px.bar(df,x='sepal_width',y='sepal_length',color='species',barmode='group',facet_row='species',facet_col='species_id')
fig1.show()


# In[15]:


fig11=px.bar(df,x='sepal_width',y='sepal_length',color='species',hover_data=['petal_width'],barmode='stack')
fig11.show()


# In[16]:


fig_=px.bar(df1,x='total_bill',y='day',color='sex',barmode='stack')
fig_.show()


# In[17]:


fij=px.histogram(df1,x='total_bill',y='day',color='sex')
fij.show()


# In[18]:


fg=px.histogram(df1,x="total_bill")
fg.show()


# In[19]:


fg=px.histogram(df1,x="total_bill",histnorm='probability density')
fg.show()


# In[20]:


fg=px.histogram(df1,x="total_bill",histnorm='probability density',color='smoker',marginal='box')
fg.show()


# In[21]:


fg=px.histogram(df1,x="total_bill",histnorm='probability density',marginal='rug')
fg.show()


# In[22]:


fg=px.histogram(df1,x="total_bill",histnorm='probability density',color='sex',animation_frame='smoker',facet_row='day',facet_col='time')
fg.show()


# In[23]:


fg=px.histogram(df1,x="total_bill",histnorm='probability density',color='smoker',marginal='violin')
fg.show()


# In[24]:


import plotly.graph_objects as go


# In[25]:


fig7=go.Figure(data=[go.Histogram(x=df['sepal_width'],cumulative_enabled=True)])
fig7.show()


# In[28]:


fig8=px.scatter(df,x='petal_length',y='petal_width',color='species')
fig8.show()


# In[ ]:




