import pickle
import re
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))
with open("MODELS/tfidf2.pkl", "rb") as f:
    tfidf2= pickle.load(f)
with open("MODELS/svm_model.pkl", "rb") as f:
    svm_model= pickle.load(f)
def trans_text1(text):
    text=text.lower()
    text=re.sub(r'[^a-zA-Z0-9?!. ]', '', text)
    text=text.split()
    text1=[]
    for word in text:
        if word not in stop_words:
            
            text1.append(word)
    return " ".join(text1)
def predict_email(new_email):
    clean_email= trans_text1(new_email)
    new_email_tf=tfidf2.transform([clean_email])
    new_email_pred = svm_model.predict(new_email_tf)
    if new_email_pred == 1:
        return ("SPAM")
    else:
        return ("HAM")
