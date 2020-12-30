"""
HappyROBERTA: a wrapper over PyTorch's RoBERTa implementation
"""
# disable pylint TODO warning
# pylint: disable=W0511

from happytransformer.happy_transformer import HappyTransformer

from transformers import RobertaForMaskedLM, RobertaTokenizerFast

class HappyROBERTA(HappyTransformer):
    """
    Currently available public methods:
        RobertaForMaskedLM:
            1. predict_mask(text: str, options=None, k=1)
        RobertaForSequenceClassification:
            1. init_sequence_classifier()
            2. advanced_init_sequence_classifier()
            3. train_sequence_classifier(train_csv_path)
            4. eval_sequence_classifier(eval_csv_path)
            5. test_sequence_classifier(test_csv_path)

    """

    def __init__(self, model='roberta-base'):
        super().__init__(model, "ROBERTA")

        self.mlm = None  # Masked Language Model
        self.nsp = None  # Next Sentence Prediction
        self.tokenizer = RobertaTokenizerFast.from_pretrained(model)

    def _get_masked_language_model(self):
        """
        Initializes the RoBERTaForMaskedLM transformer
        """
        self.mlm = RobertaForMaskedLM.from_pretrained(self.model)
        self.mlm.eval()

    def _postprocess_option(self, text):
        if text.startswith("Ġ"):
            return text[1:]
        if text == '</s>':
            return '.'
        return text