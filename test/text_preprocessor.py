from vocably.Preprocessing.text import Preprocess

preprocess = Preprocess(remove_links=True, remove_punctuation=True, remove_stopwords=True,
                        remove_numbers=False, nltk_tokenize=True)
text = 'Friendship is not only about caring for each other. Being with them in hard times'
print(f"{preprocess.tokenize(preprocess.normalise(text))}")
