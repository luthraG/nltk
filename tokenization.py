from nltk.tokenize import word_tokenize, sent_tokenize

if __name__ == "__main__":
    text = """Hello Mr. Luthra. NLTK is a great library.
            You should learn it otherwise you would be spending
            long time learning too many regular expressions."""
    sentences = sent_tokenize(text)
    words = word_tokenize(text)

    print("sentences : {}".format(sentences))
    print("words : {}".format(words))
