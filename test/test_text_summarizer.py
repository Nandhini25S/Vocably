from vocably.preprocessing.summarizer import Summarizer


def test_summarize():
    summarizer = Summarizer('t5-base')
    text = """Author : Nandhini Date : 18/10/2022   Text summarizer using transformers from transformers import pipeline class Summarizer:     """
    summarizer.summarize(text, max_length=25, min_length=10, do_sample=False)
