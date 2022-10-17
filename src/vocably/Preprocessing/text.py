import re
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import spacy
from vocably.constants import WHITELIST


class Preprocess:
    def __init__(self, remove_stopwords: bool = False,
                 lemmatize: bool = True,
                 remove_links: bool = True,
                 remove_punctuation: bool = True,
                 remove_numbers: bool = True, nltk_tokenize=False):
        self.remove_stopwords = remove_stopwords
        self.lemmatize = lemmatize
        self.remove_links = remove_links
        self.remove_punctuation = remove_punctuation
        self.remove_numbers = remove_numbers
        self.nltk_tokenize = nltk_tokenize

    def normalise(self, text):
        text = text.lower()
        text = text.replace('\n', ' ')
        text = text.replace('\t', ' ')
        if self.remove_links:
            text = re.sub(r"http(s)?(:)?(\/\/)?|(\/\/)?(www\.)?(.com)?", '', text)
            text = re.sub(r'\S*\s?(http|https)\S*', '', text)
        if self.remove_punctuation:
            text = re.sub(r'[^\w\s]', '', text)
            text = re.sub(r'\s+', ' ', text)
        if self.remove_numbers:
            # text = re.sub(r'[^a-zA-Z]', ' ', text)
            text = re.sub(r'\d+', '', text)
        return text

    def tokenize(self, text):
        if self.remove_stopwords:
            text = self.stopwords_remove(text)
        if self.nltk_tokenize:
            if self.lemmatize:
                lemmatizer = WordNetLemmatizer()
                return [lemmatizer.lemmatize(word, pos='v') for word in word_tokenize(text)]
            stemmer = PorterStemmer()
            return [stemmer.stem(word) for word in word_tokenize(text)]
        if self.lemmatize:
            lemmatizer = WordNetLemmatizer()
            return [lemmatizer.lemmatize(word, pos='v') for word in text.split()]
        stemming = PorterStemmer()
        return [stemming.stem(word) for word in text.split()]

    def stopwords_remove(self, text):
        english = spacy.load('en_core_web_sm')
        stop_words = [i for i in english.Defaults.stop_words]
        white_list = WHITELIST
        return ' '.join([word for word in text.split() if word not in stop_words or word in white_list])
