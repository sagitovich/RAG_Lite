from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import stopwords

class SearchEngine:
    def __init__(self, texts: list):
        self.texts = texts
        stop_words = stopwords.words('russian')
        self.vectorizer = TfidfVectorizer(stop_words=stop_words, ngram_range=(1, 2))
        self.tfidf_matrix = self.vectorizer.fit_transform(texts)

    def search(self, query: str, top_n: int = 3) -> list:
        """
        Основная логика поиска релевантных совпадений
        """
        try:
            query_vec = self.vectorizer.transform([query])
            similarities = cosine_similarity(query_vec, self.tfidf_matrix).flatten()
            top_indices = similarities.argsort()[-top_n:][::-1]
            print([{self.texts[i]} for i in top_indices])
            return [
                {"text": self.texts[i], "score": float(similarities[i])}
                for i in top_indices
            ]
        except Exception as e:
            raise ValueError(f"Ошибка поиска: {e}")
