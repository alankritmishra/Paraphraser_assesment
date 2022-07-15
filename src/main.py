import paraphraser
import models
import frequency
from sentence_splitter import SentenceSplitter, split_text_into_sentences

splitter = SentenceSplitter(language='en')
model = models.Model()
parapharser = paraphraser.Parapharser()
freq = frequency.Frequency(model)

print("hello world")
paragraph = "India is a great country. Can you recommed some upscale restaurants in Newyork? I am looking for a restaurant in Newyork."
sentence_list = splitter.split(paragraph)
for sentence in sentence_list:
    parapharsed = parapharser.paraphrase(model, sentence)
    print(parapharsed)

freq, top_four_words = freq.get_frequency(paragraph)
print(freq)
print(top_four_words)
