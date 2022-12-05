import spacy 
from spacytextblob.spacytextblob import SpacyTextBlob
from textblob import TextBlob
import Find_Subject
import search_tester
import SkimWikipedia
import random

# create sentence based on inputted statement. search for proper noun or persons name in statemetn and assemble sentence based on noun or name. 
# perform sentiment analysis on input, and cerate sentence that matches inputs sentiment 

def getWikiResponse(search):
    nlp = spacy.load('en_core_web_sm')

    nlp.add_pipe('spacytextblob')


    
    nsubj = []
    aux = []
    dobj = []
    root = []
    noun = []
    SkimWikipedia.Create_Definition_list(search_tester.extract_search_term(Find_Subject.find_Subject(search)))
    nsubj = SkimWikipedia.Get_Wiki_nsubj()
    aux = SkimWikipedia.Get_Wiki_aux()
    dobj = SkimWikipedia.Get_Wiki_dobj()
    root = SkimWikipedia.Get_Wiki_root()
    noun = SkimWikipedia.Get_Wiki_noun()
    print(len(nsubj), '                                                  tesdt')
    print(len(aux), '                                                  tesdt') 
    print(len(dobj), '                                                  tesdt') 
    print(len(root), '                                                  tesdt')
    print(len(noun), '                                                  tesdt')
    # proper noun, adverb,verb, determiner,  verb, proper noun
    sentiment = Find_Subject.find_Sentiment(search)
    #if it fails:
    if sentiment is None:
        return False

    if sentiment >= 0: 
        goodresp = 'ah, '+ str(Find_Subject.find_Subject(search))+ ' I like how ' +str(nsubj[random.randint(0,len(nsubj)-1)])+' '+str(dobj[random.randint(0,len(dobj)-1)])+' '+str(aux[random.randint(0,len(aux)-1)])+' '+str(root[random.randint(0,len(root)-1)])+' '+str(nsubj[random.randint(0,len(nsubj)-1)])
        return goodresp

    if sentiment <= 0:
        badresp = 'ah, '+ str(Find_Subject.find_Subject(search))+ ' I dislike how ' +str(nsubj[random.randint(0,len(nsubj)-1)])+' '+str(dobj[random.randint(0,len(dobj)-1)])+' '+str(aux[random.randint(0,len(aux)-1)])+' '+str(root[random.randint(0,len(root)-1)])+' '+str(nsubj[random.randint(0,len(nsubj)-1)])
        return badresp
