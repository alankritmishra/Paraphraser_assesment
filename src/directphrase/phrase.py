import sys
import os
import string
import regex as re
import itertools

class DirectPhrase():

    # TODO: Add a method to generate paraphrases from a given text
    # Funtion to split the sentence into words using Regex
    def split_into_words(text):
        rgx = re.compile("([\w][\w']*\w)")
        words = rgx.findall(text)
        return words

    def direct_phrase(self, given_paragraph, user_paragraph):

        triple_wise_list = []
        
        # Looping through each sentence in the given paragraph
        for sentence in given_paragraph:
            words  = self.split_into_words(sentence)
            # Generating triplets from the consecutive words in the sentence
            sentence_triple_list = list(map(list, zip(words, words[1:], words[2:])))
            triple_wise_list.append(sentence_triple_list)

        # Appending inner elements to the triplet list for feeding into regex function
        triple_list = []
        for words in triple_wise_list:
            triple_list.append(words[0]+" "+words[1]+" "+words[2])

        # Removing punctuations from the user paragraph
        user_paragraph = user_paragraph.strip(string.punctuation)

        # Regex operation to the direct phrase
        pattern = r'.*\b(?='+'|'.join(triple_list) + r')\b.*'
        matches = re.findall(pattern, user_paragraph, re.IGNORECASE)
        return matches