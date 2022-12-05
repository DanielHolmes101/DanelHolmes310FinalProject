from queue import Empty
import bs4 as bs
import urllib.request
import spacy 
from spacytextblob.spacytextblob import SpacyTextBlob
from textblob import TextBlob
from spacy import displacy
from spacy.matcher import Matcher
import wikipediaapi
from urllib.parse import urlparse, parse_qs, urlsplit, parse_qs
import re
#Skim info from wikipedia. must populate definitions before anything. 

wiki_wiki = wikipediaapi.Wikipedia('en')



nlp = spacy.load('en_core_web_sm')


global definitions 


# Page - Exists: False

def Create_Definition_list(link):     # call me first
    print(link)
    split_link = urlsplit(link)
    print(split_link)
    subject = split_link.path.split("/wiki/",1)[1]
    page_py = wiki_wiki.page(subject)
    print("Page - Exists: %s" % page_py.exists())
    global definitions
    definitions = page_py.summary[0:400]
    definition = definitions
    return definition




# test class for robustness only. do not call

def Get_Wiki_infofails():

    def_doc = nlp(str(definitions))
    nsubj = [] 
    aux = []
    dobj = []
    for token in def_doc:
        if token.dep_ =='nsubj':
            nsubj.append(token)
        if token.dep_ == 'aux':
            aux.append(token)
        if token.dep_ == 'dobj':
            dobj.append(token)
    return nsubj,aux,dobj

def Get_Wiki_nsubj():        # finds proper nouns, not strictly nsubj 
    print(definitions, 'asda                                                          asd      asd ')
    def_doc = nlp(str(definitions))
    nsubj = [] 
    for token in def_doc:
        if token.tag_ =='NNP':
            nsubj.append(token)
   
    return nsubj
def Get_Wiki_aux():                     # finds verbs
    def_doc = nlp(str(definitions))
    aux = [] 
    for token in def_doc:
        if token.tag_ =='VBZ':
            aux.append(token)
    return aux
def Get_Wiki_root():             # finds determinant( english )
    def_doc = nlp(str(definitions))
    root = [] 
    for token in def_doc:
        if token.tag_ =='DT':
            root.append(token)
    return root
def Get_Wiki_dobj():          # finds adverb
    def_doc = nlp(str(definitions))  
    dobj = [] 
    for token in def_doc:
        if token.pos_ =='ADV':
            dobj.append(token)
    return dobj
def Get_Wiki_noun():           # finds noun
    def_doc = nlp(str(definitions))
    dobj = [] 
    for token in def_doc:
        if token.pos_ =='NOUN':
            dobj.append(token)
    return dobj

def Get_Wiki_info(link): # not used currently, for future use
    url=urllib.request.urlopen(link)
    soup=bs.BeautifulSoup(url,'lxml')
    definitions=[]
    for paragraph in soup.find_all('p'):
        definitions.append(str(paragraph.text))

    def_doc = nlp(str(definitions))

    for token in def_doc.ents:
        lists = ''
        if token.text:
            lists += str(token.text)
    return lists
