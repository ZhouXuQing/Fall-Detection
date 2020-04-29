import torch
from torch.nn import BCELoss

class SigmoidBCELoss(BCELoss):
    def __init__(self):
        super(SigmoidBCELoss, self).__init__()
        
    def forward(self, output, label):
        sigmoid = torch.nn.Sigmoid()
        bce = torch.nn.BCELoss()
        loss = bce(sigmoid(output),label)
        return loss
    
class WeightedSigmoidBCELoss(BCELoss):
    def __init__(self):
        super(WeightedSigmoidBCELoss, self).__init__()
        self.weight = torch.tensor([1/6, 5/6]).float().cuda()
        # weight class_0 as 1/6 and class_1 as 5/6
    
    def forward(self, output, label):
        sigmoid = torch.nn.Sigmoid()
        batch_weight = self.weight[label.data.view(-1).long()].view_as(label)
        bce = torch.nn.BCELoss(weight = batch_weight)
        loss = bce(sigmoid(output),label)
        return loss

class BinaryHitRate():
    def __call__(self, output, label):
        prediction = (output > 0.5).float()
        hit_rate = torch.eq(prediction, label).float().mean()
        return hit_rate