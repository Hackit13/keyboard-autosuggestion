#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install textdistance')


# In[30]:


import numpy as np
import pandas as pd
import textdistance
import re
from collections import Counter


# # File opening and cleaning (change format to utf-8)

# In[26]:


words=[]
with open('autocorrect book.txt', 'r', encoding='utf-8') as f:
    data=f.read();   
    data=data.lower()
    word=re.findall('\w+', data)
    words+=word;


# In[19]:


print(words[0:10]);


# # Make vocabulary

# In[21]:


len(words)


# In[24]:


len(set(words))


# In[25]:


v=set(words)


# # Build the frequency of those words

# In[32]:


word_freq_dict=Counter(words)


# In[40]:


word_freq_dict


# In[43]:


word_freq_dict.most_common(10)


# # Relative frequency of words (probability nikaalna hai of each word)

# Now we want to get the probability of occurrence of each word, this equals the relative frequencies of the words:
# 
# The formula used to calculate the probability of a word in the provided code is:
# Probability(word) = Frequency(word)/Total count of all words

# In[44]:


['all my friends follow me on this insta id of mine. I have a good insta id. this is the best id you could think to follow']


# In[46]:


total_words_freq = sum(word_freq_dict.values())


# In[50]:


total_words_freq = sum(word_freq_dict.values())
prob = {}
for k in word_freq_dict.keys():
    print (k)
    prob[k] = word_freq_dict[k] / total_words_freq


# In[51]:


prob


# # Finding similar words

# Now we will sort words according to the Jaccard distance by calcuulating the 2 grams Q of the words. Next, we will return the 5 most similar words ordered by similarity and probability.
# 
# The Jaccard distance measures the dissimilarity between two sets by comparing their intersection and union.
# 
# ![image.png](attachment:image.png)

# In[115]:





# In[120]:


def autocorrect(word):
    word = word.lower()
    if word in prob:
        print('the word is already there and it is correct', word)
    else:
        similarities = [1-(textdistance.Jaccard(qval=2)).distance(w,word) for w in word_freq_dict.keys()]
        df = pd.DataFrame.from_dict(prob, orient='index').reset_index()
        df = df.rename(columns={'index':'Word', 0:'Probability'})  #renaming names of both the columns
        df['Similarity'] = similarities
        output = df.sort_values(['Similarity','Probability'],ascending=False).head(10)  
        return(output)
autocorrect('lod')


# In[ ]:





# In[ ]:




