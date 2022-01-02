from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

DEFAULT_MODEL = "Helsinki-NLP/opus-mt-ru-en"


class TransformerModel:
    def __init__(self, model_name=DEFAULT_MODEL):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    def translate(self, source_text, source_lang="ru", target_lang="en"):
        assert source_lang == "ru", "Not implemented source language (Supported: 'ru')"
        assert target_lang == "en", "Not implemented target language (Supported: 'en')"

        inputs = self.tokenizer(source_text, return_tensors="pt")
        outputs = self.model.generate(inputs["input_ids"], max_length=40, num_beams=4, early_stopping=True)

        return self.tokenizer.decode(outputs[0][1:]).strip()    # [1:] - remove <pad> token


transformer_model = TransformerModel()
