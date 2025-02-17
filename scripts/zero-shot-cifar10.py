import os
import sys
sys.path.insert(0, os.path.dirname("clip"))

import torch
import clip
from PIL import Image
from torchvision.datasets import CIFAR10

print(clip.available_models())
# exit()

device = "cuda:3"
# import pdb; pdb.set_trace()
model, preprocess = clip.load("ViT-B/32", device=device)

cifar10 = CIFAR10(root="data", download=True, train=False)

# prepare inputs
image, class_id = cifar10[2000]
image = preprocess(image).unsqueeze(0).to(device)

prompts = [f"a photo of {cls_name}" for cls_name in cifar10.classes]
print(prompts)
text = torch.cat([clip.tokenize(prompt) for prompt in prompts]).to(device)

print(text.shape)

# exit()


with torch.no_grad():
    image_features = model.encode_image(image)
    text_features = model.encode_text(text)
    
    logits_per_image, logit_per_text = model(image, text)
    probs = logits_per_image.softmax(dim=-1).cpu().numpy()

print("Label probs:", probs)  # prints: [[0.9927937  0.00421068 0.00299572]]

# print(text.shape)
                   