# -*- coding: utf-8 -*-

import nltk
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')
import re
from nltk.stem import WordNetLemmatizer
from pymorphy2 import MorphAnalyzer
from bs4 import BeautifulSoup

c_dict = { 
"ain't": "am not",
"aren't": "are not",
"can't": "cannot",
"can't've": "cannot have",
"'cause": "because",
"could've": "could have",
"couldn't": "could not",
"couldn't've": "could not have",
"didn't": "did not",
"doesn't": "does not",
"don't": "do not",
"hadn't": "had not",
"hadn't've": "had not have",
"hasn't": "has not",
"haven't": "have not",
"he'd": "he would",
"he'd've": "he would have",
"he'll": "he will",
"he's": "he is",
"how'd": "how did",
"how'll": "how will",
"how's": "how is",
"i'd": "i would",
"i'll": "i will",
"i'm": "i am",
"i've": "i have",
"isn't": "is not",
"it'd": "it would",
"it'll": "it will",
"it's": "it is",
"let's": "let us",
"ma'am": "madam",
"mayn't": "may not",
"might've": "might have",
"mightn't": "might not",
"must've": "must have",
"mustn't": "must not",
"needn't": "need not",
"oughtn't": "ought not",
"shan't": "shall not",
"sha'n't": "shall not",
"she'd": "she would",
"she'll": "she will",
"she's": "she is",
"should've": "should have",
"shouldn't": "should not",
"that'd": "that would",
"that's": "that is",
"there'd": "there had",
"there's": "there is",
"they'd": "they would",
"they'll": "they will",
"they're": "they are",
"they've": "they have",
"wasn't": "was not",
"we'd": "we would",
"we'll": "we will",
"we're": "we are",
"we've": "we have",
"weren't": "were not",
"what'll": "what will",
"what're": "what are",
"what's": "what is",
"what've": "what have",
"where'd": "where did",
"where's": "where is",
"who'll": "who will",
"who's": "who is",
"won't": "will not",
"wouldn't": "would not",
"you'd": "you would",
"you'll": "you will",
"you're": "you are",
"1st": "first",
"2nd": "second",
"3rd": "third",
"4th": "forth",
"5th": "fifth",
"6th": "sixth",
"7th": "seventh",
"8th": "eighth",
"9th": "ninth"
}

def text_filter(inputt , lang = 'english'):

    # Remove unwanted characters
    soup = BeautifulSoup(inputt)
    text = soup.get_text(' ')
    text = re.sub("\n", " ", text)
    text = re.sub(r'<.*?>', ' ', text)
    # text = re.sub("^\s+|\n|\r|\s+$", ' ', text)
    text = re.sub(r'https?:\/\/.*[\r\n]*', ' ', text, flags=re.MULTILINE)
    # text = re.sub(r'[_"\-;%()|+&=*%.,!?:#$@\[\]/]', ' ', text)
    text = re.sub(r'\<a href', ' ', text)
    text = re.sub(r'&amp;', ' ', text) 
    text = re.sub(r'<br />', ' ', text)
    text = re.sub(r'\'', ' ', text)
    text = re.sub(r'>', ' ', text)

    # Convert words to lower case
    text = text.lower()
    # Remove constructions
    if lang == 'english':
        text = text.split()
        new_text = []
        for word in text:
            # print(word)
            if word in c_dict:
                new_text.append(c_dict[word])
            else:
                new_text.append(word)
        text = " ".join(new_text)

    # Remove SW
    text = text.split()
    sw = set(nltk.corpus.stopwords.words(lang))
    # sw.extend(['x', 'u'])
    text = [w for w in text if not w in sw]
    # print(text)
    # text = " ".join(text)

    # Split numbers and words
    # text = text.split()
    # new_text2 = []
    # for word in text:
    #     if (word.isalpha() or word.isdigit()):
    #         new_text2.append(word)
    #     else:
    #         for i in range(0,len(word)-1):
    #             if ((word[i].isdigit() and word[i+1].isalpha()) or (word[i+1].isdigit() and word[i].isalpha())):
    #                 word1 = word[0:(i+1)]
    #                 word2 = word[(i+1):len(word)]
    #                 new_text2.append(word1)
    #                 new_text2.append(word2)
    # print(new_text2)
    # text = " ".join(new_text2)
    # new_text3 = []
    # if lang == 'english':
    lemmatizer = WordNetLemmatizer()
    # # elif lang == 'russian':
    # #     lemmatizer = MorphAnalyzer()
    # for word in text:
    #     if not word.isdigit():
    #         # if lang == 'english':
    #             word = lemmatizer.lemmatize(word)
    #             new_text3.append(word)
    #         # elif lang == 'russian':
    #         #     parser = lemmatizer.parse(word)[0]
    #         #     word = parser.normal_form
    #         #     new_text3.append(word)
    text2 = [lemmatizer.lemmatize(token) for token in text]
    # print(text)
    text = " ".join(text2)
    text = re.sub("[^A-Za-z]", " ", text)

    while "  " in text:
        text= text.replace("  ", " ")
    
    text = text.split()
    trash = []
    for w in text:
        if len(w)<3:
            trash.append(w)
    for el in trash:
        while el in text:
            text.remove(el)
    text = " ".join(text)
    
    
    return text