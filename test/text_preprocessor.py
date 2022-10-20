from vocably.preprocessing.text import Preprocess
from rich import print as rprint

preprocess = Preprocess(remove_links=False, remove_punctuation=False, remove_stopwords=False, lemmatize=False,
                        remove_numbers=True, nltk_tokenize=False)
text = "Hello  this is Pranav 1234 www.google.com !!@@@"
rprint(f"[bold blue]{preprocess.tokenize(preprocess.normalise(text))}[/bold blue]")
