from vocably.featurizer.text import Vectorizer


# now test tfidf vectorizer
def test_tfidf_vectorizer():
    vectorizer = Vectorizer(vectorizer_name='tfidf')
    features = ['hello world', 'hello world', 'hello world',
                'hello world', 'hello world', 'hello world']
    vectorizer.fit(features)
    print(vectorizer.transform(['hello world']))


# now test count vectorizer
def test_count_vectorizer():
    vectorizer = Vectorizer(vectorizer_name='countvectorizer')
    features = ['hello world', 'hello world', 'hello world',
                'hello world', 'hello world', 'hello world']
    vectorizer.fit(features)
    print(vectorizer.transform(['hello world']))
