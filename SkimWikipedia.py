from queue import Empty
import bs4 as bs
import urllib.request
import spacy 
from spacytextblob.spacytextblob import SpacyTextBlob
from textblob import TextBlob
from spacy import displacy
from spacy.matcher import Matcher

#Skim info from wikipedia. must populate definitions before anything. 





nlp = spacy.load('en_core_web_sm')


definitions = []


def Create_Definition_list(link):     # call me first
    print(link)
    url=urllib.request.urlopen(link)
    soup=bs.BeautifulSoup(url, "html.parser") #changed!
    for paragraph in soup.find_all('p'):
        definitions.append(str(paragraph.text))
    
    return definitions




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
