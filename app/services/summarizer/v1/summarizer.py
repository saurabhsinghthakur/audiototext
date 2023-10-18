"""Summarizer"""
from transformers import T5Tokenizer, T5ForConditionalGeneration

class Summarizer():
    """Summarizer"""
    def __init__(self, input_data) -> None:
        self.input_text = input_data.get("text", "")

    def post(self, max_length=150, model_name="t5-base"):
        """Summarize Text"""
        # Load pre-trained T5 model and tokenizer
        tokenizer = T5Tokenizer.from_pretrained(model_name)
        model = T5ForConditionalGeneration.from_pretrained(model_name)

        # Tokenize and generate summary
        inputs = tokenizer.encode("summarize: " + self.input_text,
                                  return_tensors="pt", max_length=512, truncation=True)
        summary_ids = model.generate(inputs,
                                     max_length=max_length,
                                     length_penalty=2.0,
                                     num_beams=4,
                                     early_stopping=True)

        # Decode and return the summary
        summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        return {"recognized_text": summary}
