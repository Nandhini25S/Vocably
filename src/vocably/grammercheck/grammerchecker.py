"""grammer corrector using transformers"""
from happytransformer import HappyTextToText, TTSettings

class GrammerCheck:
    """grammer check class"""
    def __init__(self,model_name : str ='vennify/t5-base-grammar-correction'):
        self.model_name = model_name
        self.happy_tt = HappyTextToText("T5", "vennify/t5-base-grammar-correction")
        
    def correct(self, text :str ,num_beams : int = 5, min_length : int = 5):
        args = TTSettings(num_beams=num_beams, min_length=min_length)
        result = self.happy_tt.generate_text(text, args=args)
        print(result.text) # This sentence has bad grammar.
        

    