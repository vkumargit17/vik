#!/usr/bin/env python
# coding: utf-8

# # Chapter 6 -  Data Sourcing via Web
# ## Segment 4 - Web scraping

# In[1]:


from bs4 import BeautifulSoup
import urllib.request
from IPython.display import HTML
import pdfkit


# In[2]:


r = urllib.request.urlopen('https://analytics.usa.gov/').read() #reading the website


# In[3]:


pdfkit.from_url(['https://analytics.usa.gov/'], 'webpageVisit.pdf') #capture the content to a pdf


soup = BeautifulSoup(r, "lxml")
print(soup.prettify())


hreftags=[] #array to hold all href tags


for atag in soup.find_all('a'):
#     print(atag.get('href'))
    hreftags.append(atag.get('href'))
    
hreftags


# In[ ]:




