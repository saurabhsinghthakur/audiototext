"""
Summarizer
"""
from transformers import BartTokenizer, BartForConditionalGeneration

class Summarizer():
    """Summarizer"""
    def __init__(self, input_data) -> None:
        self.input_text = input_data.get('text', None)

    def post(self, max_length=150, model_name="facebook/bart-large-cnn"):
        """Post"""
        tokenizer = BartTokenizer.from_pretrained(model_name)
        model = BartForConditionalGeneration.from_pretrained(model_name)

        inputs = tokenizer.encode(
            self.input_text,
            return_tensors="pt",
            max_length=max_length,
            truncation=True)
        summary_ids = model.generate(
            inputs,
            max_length=max_length,
            length_penalty=2.0,
            num_beams=4,
            early_stopping=True)

        summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        return summary
