import torch
print('Here 1')
model = torch.load('Similarity')
print('Here 2')
from sentence_transformers import util
sentence1 = 'It was a great day'
sentence2 = 'Today was awesome'
sentence1_representation = model.encode(sentence1) 
sentence2_representation = model.encode(sentence2)
print('Here 3')
cosine_sim = util.pytorch_cos_sim(sentence1_representation,sentence2_representation)
print(cosine_sim)

