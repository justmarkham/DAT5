'''
CLASS: APIs

Data Science Toolkit text2sentiment API
'''

'''
APIs without wrappers (i.e. there is no nicely formatted function)
'''
# Import the necessary modules
import requests # Helps construct the request to send to the API
import json # JSON helper functions

# We have a sentence we want the sentiment of
sample_sentence = 'A couple hundred hours & several thousand lines of code later... thank you @GA_DC!! #DataScience #GAGradNight'

# We know end URL endpoint to send it to
url = 'http://www.datasciencetoolkit.org/text2sentiment/'

# First we specify the header
header = {'content-type': 'application/json'}

# Next we specify the body (the information we want the API to work on)
body = sample_sentence

# Now we make the request
response = requests.post(url, data=body, headers=header)
# Notice that this is a POST request

# Let's look at the response
response.status_code
response.ok
response.text

# Let's turn that text back into JSON
r_json = json.loads(response.text)
r_json
r_json['score'] # 2.0

##########################################
############    Exercise 1    ############
##########################################
# Turn the above code into a function
# The function should take in one argument, some text, and return a number,
# the sentiment. Call your function "get_sentiment".
def get_sentiment(text):
    url = 'http://www.datasciencetoolkit.org/text2sentiment/'
    
    #specify header    
    header = {'content-type': 'application/json'}
    
    # Next we specify the body (the information we want the API to work on)
    body = text
    
    # Now we make the request
    response = requests.post(url, data=body, headers=header)
    # Notice that this is a POST request
    r_json = json.loads(response.text)
    sentiment = r_json['score'] # 2.0
    return sentiment




# Now that we've created our own wrapper, we can use it throughout our code.
# We now have multiple sentences
sentences = ['I love pizza!', 'I hate pizza!', 'I feel nothing about pizza!']

# Loop through the sentences
for sentence in sentences:
    sentiment = get_sentiment(sentence)
    print sentence, sentiment # Print the results
   

'''
APIs with wrappers (i.e. there is a nicely formatted function)    
'''    
# Import the API library    
import dstk

# Remember our sample sentence?
sample_sentence

# Let's try our new API library
# Instantiate DSTK object
dstk = dstk.DSTK()
dstk.text2sentiment(sample_sentence) # 2.0

# We can once again loop through our sentences
for sentence in sentences:
    sentiment = dstk.text2sentiment(sentence)
    print sentence, sentiment['score']
