from paraphraser.parrot import Parrot


class Parapharser:
    def correct_grammar(self, model, sentence):
        happy_tt, beam_settings = model.get_grammar_model()
        correct_sen = happy_tt.generate_text(sentence, args=beam_settings).text
        return correct_sen

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

        para_phrases = [[self.correct_grammar(model=model, sentence=para_phrase[0]), para_phrase[1]]
                        for para_phrase in para_phrases]
        return para_phrases

    def paraphrase_batch(self, model, sentences):
        parrot = Parrot(model)
        para_phrases = parrot.augment_batch(
            input_phrase=sentences, use_gpu=False)
        return para_phrases
