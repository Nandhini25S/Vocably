"""Spell check using transformers"""
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

class SpellCheck:
    """Spell check class"""

    def __init__(self, model_name: str ='Bhuvana/t5-base-spellchecker'):
        self.model_name = model_name
        self.tokenizer = AutoTokenizer.from_pretrained("Bhuvana/t5-base-spellchecker")
        self.model = AutoModelForSeq2SeqLM.from_pretrained("Bhuvana/t5-base-spellchecker")

    def correct(self, text: str, do_sample: bool = True, 
                max_length: int = 50,  top_p: float = 0.99,
                num_return_sequences : int = 1):
        input_ids = self.tokenizer.encode(text,return_tensors='pt')
        sample_output = self.model.generate(
            input_ids,
            do_sample = do_sample,
            max_length = max_length,
            top_p = top_p,
            num_return_sequences = num_return_sequences
        )
        return self.tokenizer.decode(sample_output[0], skip_special_tokens=True)
       

