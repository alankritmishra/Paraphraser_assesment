from pysimilar import compare
from sentence_transformers import util

class Similarity():

    def __init__(self, model):
        self.sem_model = model.get_similarity_model()

    def lexical_similarity(self, given_para, user_para):
        return compare(given_para, user_para)

    def semantic_similarity(self, given_para, user_para):
        """
        Compute the semantic similarity between two paragraphs.
        """

        embedding1 = self.sem_model.encode(given_para)
        embedding2 = self.sem_model.encode(user_para)
        cosine_score = util.pytorch_cos_sim(embedding1, embedding2)
        return cosine_score.cpu().detach().numpy()[0][0]

    def get_similarity_index(self, given_para, user_para):
        """
        Compute the similarity index between two paragraphs.
        """
        lexical_sim = self.lexical_similarity(given_para, user_para)
        semantic_sim = self.semantic_similarity(given_para, user_para)
        return lexical_sim, semantic_sim