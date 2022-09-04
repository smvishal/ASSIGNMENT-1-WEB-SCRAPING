#!/usr/bin/env python
# coding: utf-8

# In[7]:


# # Write a python program to display all the header tags from wikipedia.org
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('https://en.wikipedia.org/wiki/Main_Page')
bs = BeautifulSoup(html, "html.parser")
titles = bs.find_all(['h1', 'h2','h3','h4','h5','h6'])
print('List all the header tags :', *titles, sep='\n\n')


# In[13]:


# # 2) Write a python program to display IMDB’s Top rated 100 movies’ data (i.e. name, rating, year of release)and make data frame.




get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')





from bs4 import BeautifulSoup
import requests
import re
import pandas as pd




url = 'http://www.imdb.com/chart/top'
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")




movies = soup.select('td.titleColumn')
crew = [a.attrs.get('title') for a in soup.select('td.titleColumn a')]
ratings = [b.attrs.get('data-value')
        for b in soup.select('td.posterColumn span[name=ir]')]




list = []




for index in range(0, len(movies)):
    movie_string = movies[index].get_text()
    movie = (' '.join(movie_string.split()).replace('.', ''))
    movie_title = movie[len(str(index))+1:-7]
    year = re.search('\((.*?)\)', movie_string).group(1)
    place = movie[:len(str(index))-(len(movie))]
    data = {"place": place,
            "movie_title": movie_title,
            "rating": ratings[index],
            "year": year,
            }
    list.append(data)





for movie in list:
    
    print(movie['place'], '-', movie['movie_title'], '('+movie['year'],')','-', movie['rating'])
    





df = pd.DataFrame(list)
df.to_csv('imdb_top__movies.csv',index=False)




df.head(100)


# In[15]:



# # 3.Write a python program to display IMDB’s Top rated 100 Indian movies’ data (i.e. name, rating, year of release) and make data frame.



get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')




from bs4 import BeautifulSoup
import requests
import re
import pandas as pd




url = 'https://www.imdb.com/india/top-rated-indian-movies/'
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")




movies = soup.select('td.titleColumn')
crew = [a.attrs.get('title') for a in soup.select('td.titleColumn a')]
ratings = [b.attrs.get('data-value')
        for b in soup.select('td.posterColumn span[name=ir]')]




list =[]



for index in range(0, len(movies)):
    movie_string = movies[index].get_text()
    movie = (' '.join(movie_string.split()).replace('.', ''))
    movie_title = movie[len(str(index))+1:-7]
    year = re.search('\((.*?)\)', movie_string).group(1)
    place = movie[:len(str(index))-(len(movie))]
    data = {"place": place,
            "movie_title": movie_title,
            "rating": ratings[index],
            "year": year,
            }
    list.append(data)





df.head(100)



for movie in list:
    print(movie['place'], '-', movie['movie_title'], '('+movie['year'],')','-', movie['rating'])
    


df = pd.DataFrame(list)
df.to_csv('imdb_top__movies.csv',index=False)




df.head(100)


# In[16]:


# # 4) Write s python program to display list of respected former presidents of India(i.e. Name , Term of office) from https://presidentofindia.nic.in/former-presidents.htm

# In[2]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')




from bs4 import BeautifulSoup
import requests
import re
import pandas as pd




page = requests.get('https://presidentofindia.nic.in/former-presidents.htm')
page




soup = BeautifulSoup(page.content)




soup




soup = BeautifulSoup(page.content, "html.parser")
print(soup.prettify())




scraped_formerPresidents = soup.find_all('div',class_='presidentListing')
scraped_formerPresidents




formerPresidents = []
for formerPresident in scraped_formerPresidents:
    print(formerPresident.get_text())


# In[17]:


# # 5) Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape:
# a) Top 10 ODI teams in men’s cricket along with the records for matches, points and rating.
# b) Top 10 ODI Batsmen along with the records of their team and rating.
# c) Top 10 ODI bowlers along with the records of their team and rating.



get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')



from bs4 import BeautifulSoup
import requests
import re
import pandas as pd



page = requests.get('https://www.icc-cricket.com/rankings/mens/team-rankings/odi')
page




soup = BeautifulSoup(page.content)
soup


# In[20]:


# # 6.
get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')



from bs4 import BeautifulSoup
import requests
import re
import pandas as pd



page = requests.get('https://www.icc-cricket.com/rankings/women/team-rankings/odi')
page




soup = BeautifulSoup(page.content)
soup


# In[18]:


# # 7.Write a python program to scrape mentioned news details from https://www.cnbc.com/world/?region=world :i) Headline ii) Time iii) News Link



get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')




from bs4 import BeautifulSoup
import requests
import re
import pandas as pd



page = requests.get('https://www.cnbc.com/world/?region=world')
page




soup = BeautifulSoup(page.content)
soup




soup = BeautifulSoup(page.content, "html.parser")
print(soup.prettify())




for link in soup.findAll("a"):
    print("Headlines : {}".format(link.text))



for link in soup.findAll('time',{'class' : 'LatestNews-timestamp'}):
    print("Times : {}".format(link.text))



cnbc_url="https://www.cnbc.com/world"




page = requests.get('https://www.cnbc.com/world')
page



soup = BeautifulSoup(page.content)
soup



links_list = soup.find_all('a')



for link in links_list:
    if 'href'in link.attrs:
        print(str(link.attrs['href']))


# In[19]:


# # 8) Write a python program to scrape the details of most downloaded articles from AI in last 90 days.
# https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles Scrape below mentioned details : i) Paper Title ii) Authors iii) Published Date iv) Paper URL



get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')



from bs4 import BeautifulSoup
import requests
import re
import pandas as pd




page = requests.get('https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles')
page




soup = BeautifulSoup(page.content)
soup




soup = BeautifulSoup(page.content, "html.parser")
print(soup.prettify())




for link in soup.findAll("h2"):
    print("PaperTitle : {}".format(link.text))




author = []

for i in soup.find_all('span',{'class' : "sc-1w3fpd7-0 pgLAT"}):
    author.append(i.text)




author




date = []

for i in soup.find_all('span',{'class' : 'sc-1thf9ly-2 bKddwo'}):
    date.append(i.text)




date




url = "https://www.journals.elsevier.com"




page = requests.get('https://www.journals.elsevier.com') 
page




soup = BeautifulSoup(page.content)
soup




soup = BeautifulSoup(page.content, "html.parser")
print(soup.prettify())




links_list = soup.find_all('a')




for link in links_list:
    if 'href'in link.attrs:
        print(str(link.attrs['href']))


# In[40]:






  


# In[22]:


## 10) Write a python program to scrape the details of top publications from Google Scholar from 
#  https://scholar.google.com/citations?view_op=top_venues&hl=en
#  i) Rank 
#  ii) Publication
#  iii) h5-index
#  iv) h5-median

get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[23]:


from bs4 import BeautifulSoup
import requests
import re
import pandas as pd


# In[24]:


page = requests.get('https://scholar.google.com/citations?view_op=top_venues&hl=en')
page


# In[25]:


soup = BeautifulSoup(page.content)
soup


# In[26]:


rank = []
publication = []


# In[27]:


for i in soup.find_all('td',class_="gsc_mvt_p"):
    rank.append(i.text)


# In[28]:


rank


# In[33]:


for i in soup.find_all('td',class_="gsc_mvt_t"):
    publication.append(i.text)


# In[36]:


publication


# In[37]:


citation = []


# In[38]:


for i in soup.find_all('td',class_="gsc_mvt_n"):
   citation.append(i.text)


# In[39]:


citation


# In[ ]:





# In[41]:


# # 9) Write a python program to scrape mentioned details from dineout.co.in :
# i) Restaurant name ii) Cuisine iii) Location iv) Ratings v) Image URL



get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')




from bs4 import BeautifulSoup
import requests
import re
import pandas as pd



page = requests.get('https://www.dineout.co.in/delhi-restaurants/buffet-special')
page


# In[43]:


soup = BeautifulSoup(page.content, "html.parser")
print(soup.prettify())


# In[44]:


# RESTAURANT NAME
scraped_restaurant_name = soup.find_all('a',class_="restnt-name ellipsis")
scraped_restaurant_name


# In[45]:


#EMPTY LIST
restaurant_name = []

#Restaurant name
for rn in scraped_restaurant_name:
    rn = rn.get_text().replace('\n','')
    restaurant_name.append(rn)
restaurant_name


# In[49]:


# Cuisine 
scraped_cuisines = soup.find_all('div',class_="filter-component-wrap cuisine-wrap")
scraped_cuisines


# In[54]:


#EMPTY LIST
cuisines = []

#cuisines
for c in scraped_cuisines:
    c = c.get_text().replace('\n',' ')
cuisines.append(c)
cuisines


# In[55]:


# Location
scraped_location = soup.find_all('div',class_="restnt-loc ellipsis")
scraped_location


# In[57]:


#EMPTY LIST
location = []

#Location
for l in scraped_location :
    l = l.get_text().replace('\n',' ')
location.append(l)
location


# In[62]:


#Ratings
scraped_ratings = soup.find_all('div',class_="restnt-rating rating-4")
scraped_ratings


# In[63]:



#EMPTY LIST
ratings = []

#Location
for r in scraped_ratings :
    r = r.get_text().replace('\n',' ')
ratings.append(r)
ratings


# In[64]:


# Image URL
scraped_image_url = soup.find_all('img',class_= "no-img")
scraped_image_url


# In[69]:


#EMPTY LIST
image_url = []

#Location
for i in scraped_image_url :
    i = i.get_text().replace('\n',' ')
image_url.append(i)
image_url


# In[ ]:




