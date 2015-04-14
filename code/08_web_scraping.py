'''
CLASS: Web Scraping

We will be using two packages in particular:  requests and Beautiful Soup 4.
'''

'''
Introduction to Beautiful Soup
'''

# imports
import requests     # How Python gets the webpages
from bs4 import BeautifulSoup   # Creates structured, searchable object
import pandas as pd
import matplotlib.pyplot as plt

# First, let's play with beautiful soup on a "toy" webpage
html_doc = """
<!doctype html>

<html lang="en">
<head>
  <title>Brandon's Homepage!</title>
</head>

<body>
  <h1>Brandon's Homepage</h1>
  <p id="intro">My name is Brandon.  I'm love web scraping!</p>
  <p id="background">I'm originally from Louisiana.  I went to undergrad at Louisiana Tech and grad school at UNC.</p>
  <p id="current">I currently work as a Product Manager of Linguistics and Analytics at Clarabridge.</p>
  
  <h3>My Hobbies</h3>
  <ul>
      <li id="my favorite">Data Science</li>
      <li>Backcountry Camping</li>
      <li>Rock Climbing</li>
      <li>Cycling</li>
      <li>The Internet</li>
  </ul>
</body>
</html>
"""
type(html_doc)

# Beautiful soup allows us to create a structured object out of this string
b = BeautifulSoup(html_doc)
type(b)

# Let's look at "b"
b

# The most useful methods in a Beautiful Soup object are "find" and "findAll".
# "find" takes several parameters, the most important are "name" and "attrs".
# Let's talk about "name".
b.find(name='body') # Finds the 'body' tag and everything inside of it.
body = b.find(name='body')
type(body) #tag

# You can search tags also
h1 = body.find(name='h1') # Find the 'h1' tag inside of the 'body' tag
h1
h1.text # Print out just the text inside of the body

# Now let's find the 'p' tags
p = b.find(name='p')
# This only finds one.  This is where 'findAll' comes in.
all_p = b.findAll(name='p')
all_p
type(all_p) # Result sets are a lot like Python lists
all_p[0] # Access specific element with index
all_p[1]
# Iterable like  list
for one_p in all_p:
    print one_p.text # Print text
    
# Access specific attribute of a tag
all_p[0] # Specific tag
all_p[0]['id'] # Speific attribute of a specific tag

# Now let's talk about 'attrs'
# Beautiful soup also allows us to choose tags with specific attributes
b.find(name='p', attrs={"id":"intro"})
b.find(name='p', attrs={"id":"background"})
b.find(name='p', attrs={"id":"current"})
    
##########################################
############    Exercise 1    ############
##########################################
   
# 1. Extact the 'h3' element from Brandon's webpage.
b.find(name='h3')
   
# 2. Extract Brandon's hobbies from the html_doc.  Print out the text of the hobby.  
hobbies = b.findAll(name='ul')
for hobby in hobbies:
    print hobby.text

# 3. Extract Brandon's hobby that has the id "my favorite".
b.find(name='li', attrs={'id':'my favorite'})

    
'''
Beautiful Soup from the web
'''

# We see data on a web page that we want to get.  First we need the HTML.
# This downloads the HTML and puts it into the variable r
r = requests.get('http://www.imdb.com/title/tt1856010/') 
# But when we look at it, it's just one giant string.
type(r.text) # Unicode string
r.text[0:200]

# Beautiful soup allows us to create a structured object out of this string
b = BeautifulSoup(r.text)
type(b)


'''
"find" and "findAll" with the 'name' parameter in Beautiful Soup
'''
b.find(name='body') # Find a specific HTML tag
body = b.find(name='body') # Store the output of your "find"
type(body) # Let's look at the type

# Can we still run another "find" command on the output?
img = body.find('img') # Find the image tags
img
type(img)
# Yes, but it only finds one of the "img" tags.  We want them all.
imgs = body.findAll(name='img')
imgs # Now we get them all.
type(imgs) # Resultsets are a lot like Python lists

# Let's look at each individual image
imgs[0]
imgs[1]

# We're really interested is the 'src' attribute, the actual image location.
# How do we access attributes in a Python object?  Using the dot notation or the
# brackets.  With Beautiful Soup, we must use the brackets
imgs[0]['src']

# Now we can look through each image and print the 'src' attribute.
for img in imgs:
    print img['src']
    
# Or maybe we want to create a list of all of the 'src' attributes
src_list = []
for img in imgs:
    src_list.append(img['src'])
    
len(src_list)


'''
"find" and "findAll" with the 'attrs' parameter in Beautiful Soup
'''
# Now let's talk about 'attrs'
# Beautiful soup also allows us to choose tags with specific attributes
title = b.find(name="span", attrs={"class":"itemprop", "itemprop":"name"})
title # Prints HTML matching that tag, but we want the actual name
title.text # The "text" attribute gives you the text between two HTML tags

star_rating = b.find(name="div", attrs={"class":"titlePageSprite star-box-giga-star"})
# How do I get the actual star_rating number?
star_rating.text

# How do I make this star_rating a number instead of a string?
float(star_rating.text)

##########################################
############    Exercise 2    ############
##########################################
'''
We've retrieved the title of the show, but now we want the show's rating, 
duration, and genre.  Using "find" and "find all", write code that retrieves 
each of these things
Hint:  Everything can be found in the "infobar".  Try finding that first and
searchng within it.
'''

infobar = b.find(name="div", attrs={"class":"infobar"})
# Retrieve the show's content rating
content_rating = infobar.find(name='meta', attrs={"itemprop":"contentRating"})['content']

# Retrieve the show's duration
duration = infobar.find(name='time', attrs={"itemprop":"duration"}).text

# Retrieve the show's genre
genre = infobar.find(name='span', attrs={"itemprop":"genre"}).text


'''
Looping through 'findAll' results
'''
# Now we want to get the list of actors and actresses
# First let's get the "div" block with all of the actor info
actors_raw = b.find(name='div', attrs={"class":"txt-block", "itemprop":"actors", "itemscope":"", "itemtype":"http://schema.org/Person"})

# Now let's find all of the occurences of the "span" with "itemprop" "name",
# meaning the tags with actors' and actresses' names.
actors = actors_raw.findAll(name="span", attrs={"itemprop":"name"})

# Now we want to loop through each one and get the text inside the tags
actors_list = [actor.text for actor in actors]

'''
Creating a "Web Scraping" Function  
The above code we've written is useful, but we don't want to have to type it 
everytime.  We want to create a function that takes the URL and outputs the pieces
we want everytime.
'''

def getIMDBInfo(url):
    r = requests.get(url) # Get HTML
    b = BeautifulSoup(r.text) # Create Beautiful Soup object
    # Get various attributes and put them in dictionary
    results = {} # Initialize empty dictionary
    
    # Get the title
    results['title'] = b.find(name="span", attrs={"class":"itemprop", "itemprop":"name"}).text

    # Rating     
    results['star_rating'] = float(b.find(name="div", attrs={"class":"titlePageSprite"}).text)
   
    # Actors/actresses   
    actors_raw = b.find(name='div', attrs={"class":"txt-block", "itemprop":"actors", "itemscope":"", "itemtype":"http://schema.org/Person"})
    actors = actors_raw.findAll(name="span", attrs={"class":"itemprop", "itemprop":"name"})
    results['actors_list'] = [actor.text for actor in actors]
    
    # Content Rating    
    infobar = b.find(name="div", attrs={"class":"infobar"})
    results['content_rating'] = infobar.find(name='meta', attrs={"itemprop":"contentRating"})['content']
    
    # Show duration
    results['duration'] = int(infobar.find(name='time', attrs={"itemprop":"duration"}).text.strip()[:-4])#infobar.find(name='time', attrs={"itemprop":"duration"}).text
    
    # Genre    
    results['genre'] = infobar.find(name='span', attrs={"itemprop":"genre"}).text
    
    # Return dictionary    
    return results

# Let's see if it worked
# We can look at the results of our previous web page, "House of Cards"
getIMDBInfo('http://www.imdb.com/title/tt1856010/')
# Now let's try another one:  Interstellar
getIMDBInfo('http://www.imdb.com/title/tt0816692/')

# Now let's show the true functionality
list_of_title_urls = []
with open('imdb_movie_urls.csv', 'rU') as f:
    list_of_title_urls = f.read().split('\n')

# Let's get the data for each title in the list
data = []
for title_url in list_of_title_urls:
    imdb_data = getIMDBInfo(title_url)    
    data.append(imdb_data)
    
column_names = ['star_rating', 'title', 'content_rating', 'genre', 'duration', 'actors_list']
movieRatings = pd.DataFrame(data, columns = column_names)
movieRatings
# Now we have some data we can begin exploring, aggregating, etc.


'''
Bonus material: Getting movie data for the top 1000 movies on IMDB
'''

# Or let's build another webscraper to get the IMDB top 1000
movie_links = [] # Create empty list
# Notice that we are creating a list [1,101,201,...] and changing the URL slightly each time.
for i in range(1,1000,100):
    # Get url
    r = requests.get('http://www.imdb.com/search/title?groups=top_1000&sort=user_rating&start=' + str(i) + '&view=simple') # Get HTML
    b = BeautifulSoup(r.text) # Create Beautiful Soup object
    links = b.findAll(name='td', attrs={'class':'title'}) # Find all 'td's with 'class'='title'
    for link in links:
        a_link = link.find('a') # Find liks
        movie_links.append('http://www.imdb.com' + str(a_link['href'])) # Add link to list
 
# Create dataframe of the top 1000 movies on IMDB    
# NOTE:  This could take 5-10 minutes.  You can skip this part as I've already
# pulled all of this data and saved it to a file. 
data = []
j=0
# Loop through every movie title
for movie_link in movie_links:  
    try:    
        imdb_data = getIMDBInfo(movie_link) # Get movie data   
        data.append(imdb_data) # Put movie data in list
    except:
        pass
    j += 1  
    if j%50 == 0:
            print 'Completed ' + str(j) + ' titles!' # Print progress
    
# Create data frame with movies
column_names = ['star_rating', 'title', 'content_rating', 'genre', 'duration', 'actors_list']
movieRatingsTop1000 = pd.DataFrame(data, columns = column_names)

# Read in the  reated dataframe
movieRatingsTop1000 = pd.read_csv('imdb_movie_ratings_top_1000.csv')

# Now you're ready to do some analysis
movieRatingsTop1000.describe()
movieRatingsTop1000.groupby('genre').star_rating.mean()
movieRatingsTop1000.groupby('content_rating').star_rating.mean()
movieRatingsTop1000.plot(kind='scatter', x='duration', y='star_rating')
plt.show()