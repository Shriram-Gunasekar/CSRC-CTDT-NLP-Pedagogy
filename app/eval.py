# answer key and given answer
answer_key = "The quick brown fox jumps over the lazy dog"
given_answer = "The fast brown fox jumps over the lazy dog"
def result(answer_key, given_answer):
# pre-processing function
    def preprocess(text):
        # remove punctuation and convert to lowercase
        text = text.lower().replace('.', '').replace(',', '').replace('!', '').replace('?', '')
        # split into words
        words = text.split()
        # remove stop words
        stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'not', 'is', 'are', 'am', 'was', 'were', 'be', 'been'}
        words = [word for word in words if word not in stop_words]
        # lemmatize words
        lemmatizer = {'jumps': 'jump', 'running': 'run', 'played': 'play', 'faster': 'fast'}
        words = [lemmatizer.get(word, word) for word in words]
        # return preprocessed text
        return ' '.join(words)

    # preprocess answer key and given answer
    preprocessed_answer_key = preprocess(answer_key)
    preprocessed_given_answer = preprocess(given_answer)

    # compute similarity scores
    answer_key_words = set(preprocessed_answer_key.split())
    given_answer_words = set(preprocessed_given_answer.split())
    intersection = answer_key_words.intersection(given_answer_words)
    union = answer_key_words.union(given_answer_words)
    jaccard_sim = len(intersection) / len(union)
    cosine_sim = len(intersection) / ((len(answer_key_words) * len(given_answer_words)) ** 0.5)
    euclidean_sim = 1 / (1 + ((len(answer_key_words) - len(intersection)) ** 2 + (len(given_answer_words) - len(intersection)) ** 2) ** 0.5)
    manhattan_sim = 1 / (1 + (len(answer_key_words) - len(intersection)) + (len(given_answer_words) - len(intersection)))

    # print similarity scores
    return (jaccard_sim, cosine_sim, euclidean_sim, manhattan_sim)
