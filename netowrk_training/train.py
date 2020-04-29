import os
os.environ["CUDA_VISIBLE_DEVICES"] = "3"

import torch
from torch.utils.data import DataLoader
from torchvision import transforms
from tqdm import tqdm
import json


def one_epoch(epoch_num, model, dataloader, func_los, func_acc, optimizer, update_param):
    # if update_param = True, train network, otherwise do not update network parameters
    
    dataloader = tqdm(dataloader, desc = f'on epoch {epoch_num}')
    total_los = 0.0; total_acc = 0.0
    
    for data in dataloader:
        image = data[0].cuda()
        label = data[1].cuda()
        # los
        if update_param:
            model.train() # set net in training mode
            optimizer.zero_grad()
            output = model(image)
            batch_los = func_los(output, label)
            batch_los.backward()
            optimizer.step()
        else:
            model.eval()
            output = model(image)
            batch_los = func_los(output, label)
        # acc
        batch_acc = func_acc(output, label)
        # accumulate
        total_los += batch_los.item()
        total_acc += batch_acc.item()
        
    avg_los = total_los/len(dataloader)
    avg_acc = total_acc/len(dataloader)
    return avg_los, avg_acc


def save_checkpoint(epoch_num, total_epoch, train_los, test_los, train_acc, test_acc, model):
    history = {'train_los': train_los,
               'test_los': test_los,
               'train_acc': train_acc,
               'test_acc': test_acc
              }
    with open('./train_result/history.json','w') as file:
        json.dump(history, file)
    
    if (epoch_num % 5 == 0) or (epoch_num == total_epoch-1):
        torch.save(model.state_dict(), f'./train_result/model_on_epoch{epoch_num}.pkl')
        

def train(model, trainloader, testloader, func_los, func_acc, total_epoch, optimizer, scheduler):
    train_los = []
    test_los = []
    train_acc = []
    test_acc = []
    
    for epoch_num in range(total_epoch):
        if epoch_num == 0:
            _train_los, _train_acc = one_epoch(epoch_num, model, trainloader, func_los, func_acc, optimizer, update_param = False)
            _test_los, _test_acc = one_epoch(epoch_num, model, testloader, func_los, func_acc, optimizer, update_param = False)
        else:
            _train_los, _train_acc = one_epoch(epoch_num, model, trainloader, func_los, func_acc, optimizer, update_param = True)
            _test_los, _test_acc = one_epoch(epoch_num, model, testloader, func_los, func_acc, optimizer, update_param = False)
        scheduler.step()
        
        train_los.append(_train_los)
        test_los.append(_test_los)
        train_acc.append(_train_acc)
        test_acc.append(_test_acc)
        
        save_checkpoint(epoch_num, total_epoch, train_los, test_los, train_acc, test_acc, model)
            

if __name__ == "__main__":
    from dataset import Fall
    from model import construct_binary_resnet50
    from loss import BinaryHitRate, WeightedSigmoidBCELoss

    # DataSet
    trainset = Fall('./train.csv')
    trainloader = DataLoader(trainset, batch_size=32, shuffle=True, num_workers = 16)

    testset = Fall('./test.csv')
    testloader = DataLoader(testset, batch_size=32, shuffle=True, num_workers = 16)

    # Model, Loss, Eval
    model = construct_binary_resnet50().cuda()
    func_los = WeightedSigmoidBCELoss()
    func_acc = BinaryHitRate()

    # Train Config
    total_epoch = 50
    optimizer = torch.optim.SGD(model.parameters(), lr = 0.1, momentum = 0.9)
    scheduler = torch.optim.lr_scheduler.MultiStepLR(optimizer, milestones=[round(total_epoch/2),round(total_epoch*3/4)], gamma=0.1)

    # Start training 
    train(model, trainloader, testloader, func_los, func_acc, total_epoch, optimizer, scheduler)

            