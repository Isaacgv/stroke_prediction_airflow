from data_processing import pipeline
import pickle


def make_prediction(X):
    X = pipeline(X)
    try:
        X = X.drop(columns=["firstname"])
    except:
        None
    file = "../models/classifier.pickle"
    classifier = pickle.load(open(file, "rb"))
    return classifier.predict(X)
