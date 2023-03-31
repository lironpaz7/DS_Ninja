import pickle
import sklearn


def predict(title):
    with open('vectorizer.pkl', 'rb') as f_vect:
        lb = pickle.load(f_vect)
    with open('model.pkl', 'rb') as f_model:
        rf = pickle.load(f_model)
    X_inp = lb.transform([title.lower()])
    y_inp = rf.predict(X_inp)
    return y_inp[0]
