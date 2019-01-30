#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[3]:


from sklearn import datasets

boston_house_prices = datasets.load_boston()


# In[4]:


print(boston_house_prices.keys())

print(boston_house_prices.data.shape)

print(boston_house_prices.feature_names)


# In[5]:


data_frame = pd.DataFrame(boston_house_prices.data)

data_frame.tail()


# In[7]:


data_frame.columns = boston_house_prices.feature_names
data_frame.head()


# In[8]:


data_frame['Price'] = boston_house_prices.target
data_frame.tail()


# In[9]:


from sklearn import linear_model

linear_regression = linear_model.LinearRegression()

linear_regression.fit(X = pd.DataFrame(data_frame["RM"]), y = data_frame["Price"])

prediction = linear_regression.predict(X = pd.DataFrame(data_frame["RM"]))


# In[10]:


print('a value = ', linear_regression.intercept_)

print('b balue = ', linear_regression.coef_)


# In[17]:


print(data_frame["RM"].shape, prediction.shape)


# In[27]:


data_frame.plot(kind = "scatter", x = "RM", y = "Price", figsize = (6,6),
                color = "black", xlim = (4,8), ylim = (10, 45))

# plt.plot(data_frame["RM"], prediction, color="blue")

#xx = np.array([4,8])
xx = np.array([data_frame["RM"].min(), data_frame["RM"].max()])
plt.plot(xx, xx * linear_regression.coef_[0] + linear_regression.intercept_, color="blue")


# In[31]:


df = pd.DataFrame([1,2,3])
df.values

# ser = pd.Series([1,2,3])
# ser.values

