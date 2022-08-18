import paraphraser
import models
import frequency
import directphrase
import similarity
from sentence_splitter import SentenceSplitter, split_text_into_sentences

class WAT():

    def __init__(self):
        self.splitter = SentenceSplitter(language='en')
        self.model = models.Model()
        # self.parapharser = paraphraser.Parapharser()
        self.freq = frequency.Frequency(self.model)
        self.direct_phrase = directphrase.DirectPhrase()
        self.similarity = similarity.Similarity(self.model)
        
    # def paraphrase_text(self, paragraph):
    #     sentence_list = self.splitter.split(paragraph)
    #     parapharsed_text = ""
    #     for sentence in sentence_list:
    #         parapharsed = self.parapharser.paraphrase(self.model, sentence)
    #         if parapharsed is not None:
    #             parapharsed_text += " " + parapharsed[0][0]
    #     return parapharsed_text

    def analyse(self, given_paragraph, user_paragraph):
        sentence_list = self.splitter.split(given_paragraph)
        directphrase = self.direct_phrase.direct_phrase(sentence_list, user_paragraph)
        bold_text, frequent_words = self.freq.get_frequency(user_paragraph)
        lexical_sim, semantic_sim = self.similarity.get_similarity_index(given_paragraph, user_paragraph)
        freq_words = {}

        if len(frequent_words) > 0:
            for x in frequent_words:
                word = x[0]
                freq = x[1]
                freq_words[word] = freq
        else:
            word = "No frequent words found"
            freq = ""
            freq_words[word] = freq

        # sort freq_words by value
        freq_words = sorted(freq_words.items(),
                            key=lambda x: x[1], reverse=True)

        serialised_freq_words = {}
        for x in freq_words:
                word = x[0]
                freq = x[1]
                serialised_freq_words[word] = freq

        return bold_text, serialised_freq_words, directphrase, lexical_sim, semantic_sim