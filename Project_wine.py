#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd #для работы с базой данной
import matplotlib.pyplot as plt #для графики
import matplotlib as mpl


# In[2]:


data = pd.read_csv('winemag-data_first150k.csv')
fig, ax = plt.subplots(2,2)
fig.set_size_inches(15,9)
fig.suptitle('Гистограммы распределения вина по разным признакам', fontsize=14, color="black", fontweight= "black")
plt.subplots_adjust(top= 0.85 )
plt.subplots_adjust(wspace=0.5, hspace=1)

ax[0, 0].hist(data['points'], color='plum', edgecolor='blueviolet', linewidth=3)
ax[0, 0].set_title("Гистограмма распределения баллов", fontsize=14, color="blueviolet", fontweight= "black")
ax[0, 0].set_xlabel('Баллы', fontsize=14, color="blueviolet", fontweight= "bold")
ax[0, 0].set_ylabel('Количество вин', fontsize=14, color="blueviolet", fontweight= "bold")

variety = data['variety'].value_counts().head(28) #вернет количество уникальных совпадений в столбце по убыванию
ax[0, 1].set_title("Гистограмма разнообразия вина", fontsize=14, color="forestgreen", fontweight= "black")
ax[0, 1].set_xlabel('Вид вина', fontsize=14, color="forestgreen", fontweight= "bold")
ax[0, 1].set_ylabel('Количество вин', fontsize=14, color="forestgreen", fontweight= "bold")
ax[0, 1].bar(x=variety.index, height=variety.values, color='beige', edgecolor='forestgreen', linewidth=3)
ax[0, 1].set_xticklabels(variety.index, rotation=45, verticalalignment =  'top', horizontalalignment = "right")

ax[1, 0].hist(data['price'].head(100), bins=100, color='lightskyblue', edgecolor='royalblue', linewidth=1)
ax[1, 0].set_title("Гистограмма распределения цен на вина", fontsize=14, color="royalblue", fontweight= "black")
ax[1, 0].set_xlabel('Цена', fontsize=14, color="royalblue", fontweight= "bold")
ax[1, 0].set_ylabel('Количество вин', fontsize=14, color="royalblue", fontweight= "bold")

province = data['province'].value_counts().head(30)
ax[1, 1].set_title("Гистограмма частоты регионов", fontsize=14, color="maroon", fontweight= "black")
ax[1, 1].set_xlabel('Регион', fontsize=14, color="maroon", fontweight= "bold")
ax[1, 1].set_ylabel('Количество вин', fontsize=14, color="maroon", fontweight= "bold")
ax[1, 1].bar(x=province.index, height=province.values, color='bisque', edgecolor='maroon', linewidth=3)
ax[1, 1].set_xticklabels(province.index, rotation=45, verticalalignment =  'top', horizontalalignment = "right")

plt.show()


# In[ ]:




