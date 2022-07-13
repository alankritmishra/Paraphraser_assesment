import paraphraser
import models

model = models.Model()
parapharser = paraphraser.Parapharser()

print("hello world")
sentences = ["India is a great country", "Can you recommed some upscale restaurants in Newyork?",
             "I am looking for a restaurant in Newyork"]
for sentence in sentences:
    parapharsed = parapharser.paraphrase(model, sentence)
    print(parapharsed)