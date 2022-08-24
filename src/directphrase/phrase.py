import sys
import os
import string
import regex as re
import itertools

class DirectPhrase():

    # Funtion to split the sentence into words using Regex
    def split_into_words(self, text):
        rgx = re.compile("([\w][\w']*\w)")
        words = rgx.findall(text)
        return words

    def isCountinousSentence(self, seq_1, seq_2):
        arr_1 = seq_1.split()
        arr_2 = seq_2.split()
        arr_1 = arr_1[-3:]
        arr_2 = arr_2[:3]
        if arr_1 == arr_2:
            return True
        else:
            return False

    def sitchText(self, seq_1, seq_2):
        arr_1 = seq_1.split()
        arr_2 = seq_2.split()
        arr_2 = arr_2[3:]
        arr = arr_1 + arr_2
        str = ' '.join(arr)
        return str

    def direct_phrase(self, given_paragraph, user_paragraph):

        triple_wise_list = []
        
        # Looping through each sentence in the given paragraph
        for sentence in given_paragraph:
            words  = self.split_into_words(sentence)
            # Generating triplets from the consecutive words in the sentence
            sentence_triple_list = list(map(list, zip(words, words[1:], words[2:], words[3:])))
            triple_wise_list.append(sentence_triple_list)

        # Removing punctuations from the user paragraph
        user_paragraph = user_paragraph.strip(string.punctuation)

        # Appending inner elements to the triplet list for feeding into regex function
        final_list = []
        start = 0
        stop = len(user_paragraph)
        for words in triple_wise_list:
            for word in words:
                search_str = word[0]+" "+word[1]+" "+word[2]+" "+word[3]
                isThere = user_paragraph.find(search_str, start, stop)
                if isThere != -1:
                    final_list.append(search_str)

        final_matches = []
        for i, m in enumerate(final_list):
            if final_list.index(m) != len(final_list)-1:
                if self.isCountinousSentence(final_list[i], final_list[i+1]) == False:
                    final_matches.append(m)
                else:
                    length = len(final_list)
                    complete_sentence = ""
                    sub_list = final_list[i: length]
                    for j, s in enumerate(sub_list):
                        if sub_list.index(m) != len(sub_list)-1:
                            if complete_sentence == "":
                                complete_sentence = sub_list[j]
                            if self.isCountinousSentence(sub_list[j], sub_list[j+1]) == True:
                                complete_sentence = self.sitchText(complete_sentence, sub_list[j+1])
                                final_list.remove(s)
                            else:
                                final_matches.append(complete_sentence)
                                break
    
        return final_matches