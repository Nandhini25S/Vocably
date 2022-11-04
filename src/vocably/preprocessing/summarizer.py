"""Text summarizer using transformers"""
from transformers import pipeline


class Summarizer:
    """Text summarizer using transformers"""

    def __init__(self, model_name: str = 't5-base'):
        self.model_name = model_name
        self.summarizer = pipeline('summarization', model=model_name, tokenizer=model_name)

    def summarize(self, text: str, max_length: int = 50, min_length: int = 10,
                  do_sample: bool = False) -> str:
        """Summarize text"""
        return self.summarizer(text, max_length=max_length,
                               min_length=min_length, do_sample=do_sample)[0]['summary_text']

    def get_model_name(self) -> str:
        """Get model name"""
        return self.model_name
