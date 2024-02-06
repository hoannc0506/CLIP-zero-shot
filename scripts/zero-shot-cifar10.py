import os
import sys
sys.path.insert(0, os.path.dirname("clip"))

import torch
import clip
from PIL import Image


device = "cuda:0"
import pdb; pdb.set_trace()
model, preprocess = clip.load("ViT-B/32", device=device)

image = preprocess(Image.open("CLIP.png")).unsqueeze(0).to(device)
text = clip.tokenize(["a diagram", "a dog", "a cat"]).to(device)


with torch.no_grad():
    image_features = model.encode_image(image)
    text_features = model.encode_text(text)
    
    import pdb; pdb.set_trace()
    
    logits_per_image, logit_per_text = model(image, text)
    probs = logits_per_image.softmax(dim=-1).cpu().numpy()

print("Label probs:", probs)  # prints: [[0.9927937  0.00421068 0.00299572]]

# print(text.shape)
                   