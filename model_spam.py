import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

nltk.download("stopwords") #las palabras que no sirven de nada, no aportan

df = pd.read_csv("spam.csv", encoding="latin-1") # el csv de spam para entrenar y diferenciar
df = df[["v1", "v2"]].rename(columns={'v1': "label", 'v2': "text"})

stemmer = PorterStemmer()
stop_words = set(stopwords.words("english"))

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z]', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    words = text.split()
    words = [stemmer.stem(word) for word in words if word not in stop_words]
    return " ".join(words)

df["cleaned_text"] = df["text"].apply(clean_text)

tfidf = TfidfVectorizer()
X = tfidf.fit_transform(df["cleaned_text"])  # toarray() no se uso porque se desbordaba la memoria 
y = df["label"].map({'ham': 0, 'spam': 1})

model = MultinomialNB()
model.fit(X, y)

def reconocer_spam(texto):
    texto_limpio = clean_text(texto)
    vector = tfidf.transform([texto_limpio])  # toarray() no se uso porque se desbordaba la memoria 
    prediccion = model.predict(vector)[0]
    return "spam" if prediccion == 1 else "ham"
