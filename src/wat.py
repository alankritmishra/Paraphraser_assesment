import paraphraser
import models
import frequency
from sentence_splitter import SentenceSplitter, split_text_into_sentences

class WAT():

    def __init__(self):
        self.splitter = SentenceSplitter(language='en')
        self.model = models.Model()
        self.parapharser = paraphraser.Parapharser()
        self.freq = frequency.Frequency(self.model)

    def paraphrase_text(self, paragraph):
        sentence_list = self.splitter.split(paragraph)
        parapharsed_text = ""
        for sentence in sentence_list:
            parapharsed = self.parapharser.paraphrase(self.model, sentence)
            if parapharsed is not None:
                parapharsed_text += parapharsed_text + " " + parapharsed[0][0]
        return parapharsed_text

    def analyse(self, text):
        bold_text, top_four_words = self.freq.get_frequency(text)
        return bold_text, top_four_words


    
