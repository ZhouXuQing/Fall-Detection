import os
import pandas as pd
from PIL import Image
import torch
from torch.utils.data import Dataset
from torchvision import transforms

class Fall(Dataset):
    def __init__(self, csv_path, transform = transforms.ToTensor()):
        self.csv = pd.read_csv(csv_path)
        self.transform = transform
    
    def __len__(self):
        return len(self.csv)
    
    def __getitem__(self, index):
        img = Image.open(self.csv.loc[index]['img'])
        img = self.transform(img)                   
        label = torch.tensor(self.csv.loc[index]['label']).float().unsqueeze(dim = 0)
        return img, label