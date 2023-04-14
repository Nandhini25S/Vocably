"""paraphraser using transformers"""
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

class Paraphraser:
    """Paraphraser class"""

    def __init__(self, model_name: str ='Vamsi/T5_Paraphrase_Paws'):
        self.model_name = model_name
        self.tokenizer = AutoTokenizer.from_pretrained("Vamsi/T5_Paraphrase_Paws")  
        self.model = AutoModelForSeq2SeqLM.from_pretrained("Vamsi/T5_Paraphrase_Paws")
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    def paraphrase(self, text: str, do_sample: bool = True, 
                max_length: int = 50,  top_p: float = 0.99, top_k: int = 120, early_stopping: bool = True,
                num_return_sequences : int = 5):
        text =  "paraphrase: " + text + " </s>"
        self.model = self.model.to(self.device)
        encoding = self.tokenizer.encode_plus(text,pad_to_max_length=True, return_tensors="pt")
        input_ids, attention_masks = encoding["input_ids"].to(self.device), encoding["attention_mask"].to(self.device)
        outputs = self.model.generate(
            input_ids = input_ids, attention_mask=attention_masks,
            max_length = max_length,
            do_sample = do_sample,
            top_k = top_k,
            top_p = top_p,
            early_stopping = early_stopping,
            num_return_sequences = num_return_sequences
        )
        for output in outputs:
            line = self.tokenizer.decode(output, skip_special_tokens=True,clean_up_tokenization_spaces=True)
            return(line)
