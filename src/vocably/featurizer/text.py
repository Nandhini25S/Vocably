"""Author : Nandhini and Sanjaypranav
Date : 21/10/2022"""
import pickle
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from scipy.sparse import spmatrix


class Vectorizer:
    """Common class for all vectorizer
    getting vectorizer name as parameter like tfidf, countvectorizer
    in set vectorizer method written in sklearn"""

    def __init__(self, vectorizer_name: str = None):
        """initializing vectorizer"""
        params = {'tfidf': TfidfVectorizer(), 'countvectorizer': CountVectorizer()}
        if vectorizer_name is None:
            self.vectorizer = CountVectorizer()
        elif vectorizer_name not in params.keys():
            raise ValueError("Vectorizer name should be tfidf or countvectorizer")
        else:
            self.vectorizer = params[vectorizer_name]

    def fit(self, features: list) -> spmatrix:
        """fitting vectorizer"""
        return self.vectorizer.fit(features)

    def transform(self, feature: list) -> spmatrix:
        """transforming vectorizer"""
        return self.vectorizer.transform(feature).toarray()

    def fit_transform(self, feature: list) -> spmatrix:
        """fitting and transforming vectorizer"""
        return self.vectorizer.fit_transform(feature).toarray()

    def get_feature_names(self) -> list:
        """getting feature names"""
        return self.vectorizer.get_feature_names()

    def get_params(self, deep=True) -> dict:
        """getting params"""
        return self.vectorizer.get_params(deep=deep)

    def set_params(self, **params) -> None:
        """setting params"""
        return self.vectorizer.set_params(**params)

    def save_vectorizer(self, path: str) -> str:
        """saving vectorizer"""
        if path is None:
            path = 'vectorizers/vectorizer.pkl'
        with open(path, 'wb') as file:
            pickle.dump(self.vectorizer, file)
        return "Vectorizer saved"

    def load_vectorizer(self, path: str) -> str:
        """loading vectorizer"""
        with open(path, 'rb') as file:
            self.vectorizer = pickle.load(file)
        return "Vectorizer loaded"

    def get_vectorizer(self) -> object:
        """getting vectorizer"""
        return self.vectorizer
