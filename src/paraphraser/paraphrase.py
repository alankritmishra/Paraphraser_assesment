from paraphraser.parrot import Parrot


class Parapharser:
    def paraphrase(self, model, sentence):
        parrot = Parrot(model)
        para_phrases = parrot.augment(input_phrase=sentence,
                                      use_gpu=False,
                                      diversity_ranker="levenshtein",
                                      do_diverse=False,
                                      max_return_phrases=10,
                                      max_length=32,
                                      adequacy_threshold=0.23,
                                      fluency_threshold=0.75)
        return para_phrases

    def paraphrase_batch(self, model, sentences):
        parrot = Parrot(model)
        para_phrases = parrot.augment_batch(
            input_phrase=sentences, use_gpu=False)
        return para_phrases
