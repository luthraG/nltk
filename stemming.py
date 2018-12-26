from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

if __name__ == "__main__":
    text = """I was taking a ride in the car. I was riding in the car."""
    ps = PorterStemmer()
    words = word_tokenize(text)
    stems = [ps.stem(w) for w in words]
    print("PorterStemmer generates = {}".format(stems))
