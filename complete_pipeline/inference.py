import torch
from model import construct_binary_resnet50
from PIL import Image
from torchvision import transforms
import cv2

from emergency_call import send_text_message

def start_infer(phone_number):
    # load environment
    model = construct_binary_resnet50()
    model.load_state_dict(torch.load('./model_on_epoch49.pkl', map_location=lambda storage, loc: storage))
    model.eval()

    trans = transforms.Compose([transforms.CenterCrop(720),transforms.Resize(224),transforms.ToTensor()])
    sigmoid = torch.nn.Sigmoid()
    
    # loop over frames
    cap = cv2.VideoCapture(0)
    # ensembly method
    window_size = 3
    pred_seq = torch.zeros(window_size)
    position_counter = 0

    while(1):
        ret, frame = cap.read()
        cv2.imshow("capture", frame)
        
        # inference
        img = Image.fromarray(frame)
        network_in = trans(img).unsqueeze(0)
        prediction = sigmoid(model(network_in))
        print(prediction)
        
        if prediction > 0.5:
            pred_seq[position_counter] = 1
            if pred_seq.mean() > 0.5:
                send_text_message(phone_number)
                print('send_message')
                break
        else:
            pred_seq[position_counter] = 0
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        position_counter = (position_counter+1)%window_size

    cap.release()
    cv2.destroyAllWindows()
  
