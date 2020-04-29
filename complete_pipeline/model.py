from torchvision import models
import torch

def construct_binary_resnet50():
    net = models.resnet50(pretrained=True)
    input_dim = net.fc.in_features
    output_dim = 1
    net.fc = torch.nn.Linear(input_dim, output_dim)
    return net