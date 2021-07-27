from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer()
from sklearn.metrics.pairwise import cosine_similarity

class Kemiripan:
    def __init__(self):
        pass
    
    def proses (self, *data):
        x = vectorizer.fit_transform(data)
        x = x.todense()
        return (cosine_similarity(x[0], x[1]))
if __name__ == '__main__':
    pass