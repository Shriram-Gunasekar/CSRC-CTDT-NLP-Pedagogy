import torch
qa_pipeline = torch.load('QA')
results = qa_pipeline({ 'question': "What is machine learning?",
'context': "Machine learning is a subset of artificial intelligence. It is widely for creating a variety of applications such as email filtering and computer vision"
})
print(results)