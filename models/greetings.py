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
            "Does the Department of Entomology have any events coming up?",
            "Can you provide me with a link to the Department of Entomology's website?"
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
           "Entomology is the study of insects and related arthropods. Would you like more information?", 
           "Entomology is the scientific study of insects, their relationships to humans, other animals, and plants, and their roles in the environment. Would you like more information?",
           "The Department of Entomology conducts research on insect ecology, pest managem. Would you like more information on a specific research area?",
           "You can check the Department of Entomology's website for information on upcoming events.",    
           "You can find the Department of Entomology's website at: https://www.example.com/entomology"
           ]

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import SVC
# convert text data into numerical vectors
vectorizer = CountVectorizer()
# create a classifier








