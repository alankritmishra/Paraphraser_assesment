from transformers import AutoTokenizer
class Model:
    def __init__(self, adequacy_model_tag='prithivida/parrot_adequacy_model', 
                fluency_model_tag='prithivida/parrot_fluency_model', 
                diversity_model_tag='paraphrase-distilroberta-base-v2', 
                paraphrase_model_tag='prithivida/parrot_paraphraser_on_T5',
                 similarity_model_tag='sentence-transformers/all-MiniLM-L6-v2'):

        # Importing required libraries
        # from transformers import AutoModelForSequenceClassification, AutoTokenizer, AutoModelForSeq2SeqLM
        from sentence_transformers import SentenceTransformer
        # from happytransformer import TTSettings, HappyTextToText

        # Load the model for the similarity
        self.similarity_model = SentenceTransformer(similarity_model_tag)

        # # Load the model for the adequacy model
        # self.adequacy_model = AutoModelForSequenceClassification.from_pretrained(
        #     adequacy_model_tag)
        # self.adequacy_tokenizer = AutoTokenizer.from_pretrained(
        #     adequacy_model_tag)

        # # Load the model for the fluency model
        # self.fluency_model = AutoModelForSequenceClassification.from_pretrained(
        #     fluency_model_tag)
        self.fluency_tokenizer = AutoTokenizer.from_pretrained(
            fluency_model_tag)

        # Load the model for the diversity model
        # self.diversity_model = SentenceTransformer(diversity_model_tag)

        # # Load the model for the paraphrase model
        # self.paraphrase_model = AutoModelForSeq2SeqLM.from_pretrained(
        #     paraphrase_model_tag)
        # self.paraphrase_tokenizer = AutoTokenizer.from_pretrained(
        #     paraphrase_model_tag)

        # # load grammar for paraphrase model
        # self.happy_tt = HappyTextToText(
        #     "T5", "vennify/t5-base-grammar-correction")
        # self.beam_settings = TTSettings(
        #     num_beams=5, min_length=1, max_length=100)

    # Getter functions for Similarity model
    def get_similarity_model(self):
        return self.similarity_model
    # def get_adequancy_model(self):
    #     return self.adequacy_model

    # def get_adequacy_tokenizer(self):
    #     return self.adequacy_tokenizer

    # # Getter functions for fluency model
    # def get_fluency_model(self):
    #     return self.fluency_model

    def get_fluency_tokenizer(self):
        return self.fluency_tokenizer

    # # Getter functions for diversity model
    # def get_diversity_model(self):
    #     return self.diversity_model

    # # Getter functions for paraphrase model
    # def get_paraphrase_model(self):
    #     return self.paraphrase_model

    # def get_paraphrase_tokenizer(self):
    #     return self.paraphrase_tokenizer

    # # getter for grammar in paraphrase model
    # def get_grammar_model(self):
    #     return self.happy_tt, self.beam_setting