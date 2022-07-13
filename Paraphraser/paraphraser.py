from Paraphraser.parrot import Parrot
from Assets.models import Model
    
class Parapharser:
    def paraphrase(self, model, sentence):
        parrot = Parrot(model)
        para_phrases = parrot.augment(input_phrase=sentence, use_gpu=False)
        return para_phrases

    def paraphrase_batch(self, model, sentences):
        parrot = Parrot(model)
        para_phrases = parrot.augment_batch(input_phrase=sentences, use_gpu=False)
        return para_phrases