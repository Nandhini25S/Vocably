from vocably.preprocessing.text import Preprocessor


def test_preprocess():
    preprocess = Preprocessor()
    text = "hello! Welcome to vocably-0.0.6 from https://pypi.org/project/vocably/"
    assert (preprocess.tokenize(preprocess.normalize(text)) == ['hello', 'welcome', 'to', 'vocably', 'from', 'pypi',
                                                                'org', 'project', 'vocably'])
