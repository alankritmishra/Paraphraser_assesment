import matplotlib.pyplot as plt
import nltk
import sys
import os
import string
from nltk.corpus import stopwords


class Frequency():

    def __init__(self, model):
        self.tokenizer = model.get_fluency_tokenizer()
        self.stop_words = stopwords.words('english')

    def filter_words(self, tokens):
        # this function filters out the only words that are not stopwords, punctuation, or numbers, cls token, & pad token
        filter = [word for word in tokens if word not in [
            '[CLS]', '[SEP]', '</s>']]
        filter = [word for word in filter if word not in self.stop_words]
        filter = [word for word in filter if word not in string.punctuation]
        filter = [word for word in filter if word not in string.digits]
        return filter

    def cap_first(self, words):
        # capitalize the first letter of each sentence
        new_token = []
        for i, word in enumerate(words):
            if i == 1:
                new_token.append(word.capitalize())
            elif words[i-1] in ['.', '!', '?']:
                new_token.append(word.capitalize())
            else:
                new_token.append(word)
        return new_token

    def get_frequency(self, paragraph):
        # this function returns a dictionary of the frequency of each word in the paragraph and top 4 frquent words

        input_paragraph = self.tokenizer(paragraph)
        tokens = self.tokenizer.convert_ids_to_tokens(
            input_paragraph['input_ids'])
        filtered_words = self.filter_words(tokens)

        # plot frequency distribution of words with frequency greater than 1
        freq = nltk.FreqDist(filtered_words)
        # filter set where value is more than 1
        new_set = [(sub, val)
                   for sub, val in freq.items() if val > 1 and not ('##' in sub)]
        # and not ('##' in sub)
        top = freq.most_common(4)
        top = [(sub, val)
               for sub, val in freq.items() if not ('##' in sub)]
        # sort by value
        top = sorted(top, key=lambda x: x[1], reverse=True)
        # select top 4
        # top_four_words = top[:4]

        tokens_new = self.cap_first(tokens)
        # bold the words that are most common in the original text
        for sub, val in new_set:
            tokens_new = [word if word.lower() != sub else '**' +
                          word + '**' for word in tokens_new]

        # final ouptut
        modified_text = self.tokenizer.convert_tokens_to_string(tokens_new)

        # filter cls & sep tokens
        print(modified_text)
        result = modified_text.replace('[CLS]', '').replace(
            '[SEP]', '.').replace('[sep]', '')

        return result, new_set
