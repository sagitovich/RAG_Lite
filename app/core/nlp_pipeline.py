import os
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

nltk_data_dir = os.path.expanduser('~/nltk_data')
if not os.path.exists(nltk_data_dir) or not any(os.scandir(nltk_data_dir)):
    nltk.download('punkt')
    nltk.download('stopwords')
    nltk.download('wordnet')


class NLPPipeline:
    def __init__(self):
        self.stop_words = set(stopwords.words('russian'))
        self.lemmatizer = WordNetLemmatizer()

    def preprocess(self, text: str) -> list:
        """
        Логика обработки текста
        """
        try:
            text = text.lower()
            tokens = word_tokenize(text, language='russian')
            tokens = [
                self.lemmatizer.lemmatize(word)
                for word in tokens if word.isalnum() and word not in self.stop_words
            ]
            return tokens
        except Exception as e:
            raise ValueError(f"Ошибка обработки текста: {e}")
