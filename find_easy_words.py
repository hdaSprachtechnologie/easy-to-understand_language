import access_open_de_wn
from access_open_de_wn import *
import textblob_de
from textblob_de import TextBlobDE
from nlp_melanie import *
import basic_german_dict
from basic_german_dict import *



def find_word_status(word):
      de_wn = open(r"C:\Users\Melanie\Documents\05_Projekte\WordNet\OdeNet\odenet.git\trunk\deWordNet.xml","r",encoding="utf-8")
      lines = de_wn.readlines()
      try:
        lemma_id, lemma, pos, senses = check_word_lemma(word)
        for line in lines:
            if 'id="' + lemma_id + '" dc:type="basic_German"' in line:
                return(True)
      except:
         return(False)
      de_wn.close()
  

def find_easy_syn(word, syns):
      de_wn = open(r"C:\Users\Melanie\Documents\05_Projekte\WordNet\OdeNet\odenet.git\trunk\deWordNet.xml","r",encoding="utf-8")
      lines = de_wn.readlines()
      if find_word_status(word) == True:
            print('Leichtes Wort: ' + word)
      else:
        for w in syns:
                lemma_id, lemma, pos, senses = check_word_lemma(w)
                for line in lines:
                    if 'id="' + lemma_id + '" dc:type="basic_German"' in line:
                        print(word + " hat eine leichte Alternative: " + str(lemma))
      de_wn.close()



# direkt aus OdeNet

def lex_vereinfache(satz):
    word_list = TextBlobDE(satz).words
    for word in word_list:
#        print(word)
        lemma = lemmatize_word(word)
#        print(lemma)
        syns = synonyms(lemma)
        if syns != None:
            find_easy_syn(lemma, syns)
    
        

# mit dem Dictionary, das aus OdeNet heraus gezogen wurde

def complex_terms_satz(satz):
      word_list = TextBlobDE(satz).words
      for word in word_list:
            lemma = lemmatize_word(word)
            if find_word_status(lemma) == True:
                print('Leichtes Wort: ' + word)  
            elif lemma in basic_german.keys():
                  easy_variant = basic_german[lemma]
                  print(word + " hat eine leichte Alternative: " + str(easy_variant))


