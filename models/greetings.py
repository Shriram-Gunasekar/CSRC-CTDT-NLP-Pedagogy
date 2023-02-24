# conversation dataset
questions = [
            "Hello!",
            "Hi there!",
            "How are you?",
            "What can you do?",
            "Can you summarize PDFs?",
            "Can you summarize text?",
            "Can you check for plagiarism in PDFs?",
            "Can you check for plagiarism in text?",
            "Can you answer questions about PDFs?",   
            "Can you answer questions about text?",
            "Do you know anything about entomology?",
            "What is entomology?",
            "What kind of research does the Department of Entomology do?",
            "Can you provide me with a link to the Department of Entomology's website?",
            "How old are you?",
            "What are your hobbies?",
            "Can you provide me with a link to the Machining department's website?",
            "Do you know anything about the Machining department?"
            ]

answers = [
           "Hello! How can I assist you today?",
           "Hi there! What can I do for you?",
           "I am an AI language model, so I don't have feelings, but I'm here to help!", 
           "I can supply links to different resources on our website. Which would you like me to assist with?",
           "Yes, we offer a PDF summarizer tool. You can find it at:",
           "Yes, we offer a text summarizer tool. You can find it at:",
           "Yes, we offer a PDF plagiarism checker tool.",
           "Yes, we offer a text plagiarism checker tool.",   
           "Yes, we offer a PDF Q&A tool. You can find it at:",
           "Yes, we offer a text Q&A tool. You can find it at:", 
           "Entomology is the study of insects and related arthropods.", 
           "Entomology is the scientific study of insects, their relationships to humans, other animals, and plants, and their roles in the environment. Would you like more information?",
           "The Department of Entomology conducts research on insect ecology, pest managem. Would you like more information on a specific research area?",
           "You can find the Department of Entomology's website at: https://www.example.com/entomology",
           "I am an AI language model, so I don't have an age.",
           "I enjoy serving students and faculty like yourself!",
           "You can find the Machining department's website at:",
           "The Machining department is a part of the College of Engineering. Would you like more information?"
           ]

from sklearn.feature_extraction.text import CountVectorizer
from sklearn import svm
# convert text data into numerical vectors
vectorizer = CountVectorizer()
# create a classifier
classifier = svm.SVC(kernel='linear')
# train the classifier
classifier.fit(vectorizer.fit_transform(questions), answers)
# while True:
#     # get user input
#     question = input("You: ")
#     # get the answer
#     answer = classifier.predict(vectorizer.transform([question]))[0]
#     # print the answer
#     print("Bot: " + answer)
import pickle
# save the vectorizer
pickle.dump(vectorizer, open("convovectorizer", "wb"))
# save the classifier
pickle.dump(classifier, open("convoclassifier", "wb"))
#check








