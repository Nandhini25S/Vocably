from vocably.preprocessing.text import Preprocess


def test_preprocess():
    preprocess = Preprocess(remove_links=False, remove_punctuation=False, remove_stopwords=False,
                            lemmatize=False, remove_numbers=False, nltk_tokenize=False)
    text = "hello! Welcome to vocably-0.0.6 from https://pypi.org/project/vocably/"
    assert (preprocess.tokenize(preprocess.normalise(text)) == ['hello!', 'welcom',
                                                                'to', 'vocably-0.0.6', 'from',
                                                                'https://pypi.org/project/vocably/'])
