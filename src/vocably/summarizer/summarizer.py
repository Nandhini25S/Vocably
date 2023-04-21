"""Text summarizer using transformers"""
from transformers import BartTokenizer, BartForConditionalGeneration, BartConfig

class Summarizer:
    """Text summarizer using transformers"""

    def __init__(self, model_name: str = 'facebook/bart-large-cnn'):
        self.model = BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn')
        self.tokenizer = BartTokenizer.from_pretrained('facebook/bart-large-cnn')

    # def summarize(self, text: str, max_length: int = 50, min_length: int = 10,
    #               do_sample: bool = False) -> str:
    #     """Summarize text"""
    #     return self.summarizer(text, max_length=max_length,
    #                            min_length=min_length, do_sample=do_sample)[0]['summary_text']

    # def get_model_name(self) -> str:
    #     """Get model name"""
    #     return self.model_name

    
    def summarizer(self, text: str, max_length : int = 200,early_stopping : bool = False ):
    
        inputs = self.tokenizer([text], return_tensors='pt')
        summary_ids = self.model.generate(inputs['input_ids'], max_length=max_length, early_stopping=early_stopping)
        #summary_ids
        summarized_text= ([self.tokenizer.decode(g, skip_special_tokens=True) for g in summary_ids])
        return summarized_text