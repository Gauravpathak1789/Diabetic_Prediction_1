#!/usr/bin/env python
# coding: utf-8

# # Team ;- freebirds; 1st member:- Gaurav-Pathak(12204085) ;2nd member:- Aditya-Dev(12204086)

# In[53]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


df=pd.read_csv("C:\\Users\\Gaurav Pathak\\Downloads\\heart.csv")


# In[3]:


df.head()


# In[4]:


df.columns.values


# # *columns detail
# #HERE CP=CHEST PAIN ; trestbps=RESTING BLOOD PRESSURE ; CHOL=SERUM CHOLESTORAL(ng/dl) ;
# 
# #fbs=FASTING BLOOD SUGAR ; restecg=RESTING ELECTROCARDIOGRAPHIC RESULT ;
# 
# #thalach= MAX HEART RATE ACHIEVED ;(1=male ;0=female)
# 
# #exang=EXERCISE INDUCED ANGINA; oldpeak=ST depresion induced by exercise relative to rest ;
# 
# #slope=slope of the peak exercise ST segment ; target= having heart diseases or not (0=no dieases,1=diseases)
# 
# 
# 
# 

# In[5]:


df.info()


# In[6]:


df.isna().sum()


# In[ ]:


df.hist(bins=40,figsize=(20,15))
plt.show()


# In[7]:


df.describe()


# # DATA ANALYSIS:-
# 

# 1.How many people have heart diseases and people doesn't have heart diseases?
# 2.People of which sex has most heart diseases?
# 3.People of which sex has which type of pain most?
# 4.people with which chestpain are most pron to have  heart diseases?
# 5.Age vs maximum heart rate when people have heart diseases.
# 6.Age vs maximum heart rate when people doesn't have heart diseases.
# 7.Age vs serum cholestoral when  people have heart diseases .
# 8.Age vs serum cholestoral when people doesn't have heart diseases .
# 9.People of which sex has more exercise induced again?
# 10.Which sex of people has more fasting blood sugar>120mg/dl?
# 
# 

# In[8]:


#1.How many people have heart diseases and people doesn't have heart diseases?

a=df.target.value_counts()
a


# In[10]:


df.target.value_counts().plot(kind='bar',color=['r','g'])
plt.title('Heart diseases value')
plt.xlabel('1= diseases    o= no diseases', fontsize=14)
plt.ylabel('amount',fontsize=14)
plt.show()


# In[9]:


df.target.value_counts().plot(kind='pie')
plt.legend(['diseases','no diseases'])


# In[11]:


df[['sex','target']]


# In[12]:


bins=[0,1]
sns.lineplot(x=df['sex'],y=df['target'],data=df,hue='sex',style='sex',markers=["<","o"])#0=female,1=male.
plt.title("diseases based on sex",fontsize=16)
plt.xlabel("sex",fontsize=15)
plt.ylabel("target",fontsize=15)
plt.show()


# In[13]:


b=df.sex.value_counts()
b


# In[14]:


b.plot(kind='pie')
plt.legend(['Male','Female'])


# In[15]:


pd.crosstab(df.sex,df.target)


# In[16]:


sns.countplot(x='target',data=df,hue='sex')
plt.show()


# In[17]:


df.cp.value_counts()


# In[18]:


df.cp.value_counts().plot(kind='bar',color=['salmon','lightblue','springgreen','khaki'])
plt.title('chest pain vs number of people')
plt.show()


# In[19]:


pd.crosstab(df.sex,df.cp)


# In[20]:


pd.crosstab(df.sex,df.cp).plot(kind='bar',color=['r','b','g','k'])
plt.title('Types of chest pain with respect to sex')
plt.xlabel('0=Female , 1=Male');


# In[21]:


pd.crosstab(df.cp,df.target)


# In[22]:


sns.countplot(x='cp',data=df,hue='target');


# In[23]:


sns.displot(x='age',data=df,bins=30,kde=True);


# In[24]:


#5.Age vs maximum heart rate when people have heart diseases

df.age[df.target==1]


# In[27]:


#6.Age vs maximum heart rate when people doesn't have heart diseases.
df.age[df.target==0]


# In[25]:


plt.scatter(df.age[df.target==1],df.thalach[df.target==1],c='tomato')
plt.scatter(df.age[df.target==0],df.thalach[df.target==0],c='lightgreen')
plt.title('Max heart rate vs age')
plt.xlabel('age')
plt.ylabel('Max heart rate')
plt.legend(['Diseases','no-diseases'])
plt.show()


# In[29]:


# 7.Age vs serum cholestoral when people have heart diseases . 
#8.Age vs serum cholestoral when people doesn't have heart diseases 


# In[32]:


plt.scatter(df.age[df.target==1],df.chol[df.target==1],color='yellow')
plt.scatter(df.age[df.target==0],df.chol[df.target==0],color='blue')
plt.title('age vs serum cholestrol')
plt.xlabel('age')
plt.ylabel('serum cholestrol')
plt.legend(['Diseases','No Diseases'])
plt.show()


# In[33]:


#9.People of which sex has more exercise induced again?
df.sex[df.exang==1].value_counts()


# In[35]:


sns.countplot(x='exang',data=df,hue='sex')#here,sex(0)=Female ; sex(1)=Male.


# In[39]:


#10.Which sex of people has more fasting blood sugar>120mg/dl?
df.sex[df.fbs==1].value_counts()


# In[52]:


sns.barplot(x=df.sex,y=df.fbs,data=df,hue='sex');


# In[ ]:




