from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

if __name__ == '__main__':
    text = """Hello Mr. Luthra. NLTK is a great library.
            You should learn it otherwise you would be spending
            long time learning too many regular expressions."""
    stop_words = set(stopwords.words("english"))
    print("english stop words = {}".format(stop_words))

    words = word_tokenize(text)

    filtered_sentence = [w for w in words if w not in stop_words]
    print("filtered sentence = {}".format(filtered_sentence))
