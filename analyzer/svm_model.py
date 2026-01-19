from sklearn.svm import SVC
from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer()
model = SVC(kernel="linear", probability=True)

texts = [
    "gana dinero rapido",
    "oferta limitada",
    "haz clic aqui",
    "reunion mañana",
    "hola como estas"
]

labels = ["phishing", "phishing", "phishing", "legitimo", "legitimo"]

X = vectorizer.fit_transform(texts)
model.fit(X, labels)

def predict_email(text):
    X_test = vectorizer.transform([text])
    pred = model.predict(X_test)[0]
    prob = model.predict_proba(X_test)[0]
    return pred, prob
