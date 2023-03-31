"""
Мы команда лучше всех, нас ждет большой успех!!!
Test example of pretrained model
"""

import torch
from torchvision import transforms
import urllib
from PIL import Image
import unittest


model = torch.hub.load('nicolalandro/ntsnet-cub200', 'ntsnet', pretrained=True,
                       **{'topN': 6, 'device': 'cpu', 'num_classes': 200})

transform_test = transforms.Compose([
    transforms.Resize((600, 600), Image.BILINEAR),
    transforms.CenterCrop((448, 448)),
    # transforms.RandomHorizontalFlip(),  # only if train
    transforms.ToTensor(),
    transforms.Normalize((0.485, 0.456, 0.406), (0.229, 0.224, 0.225)),
])


model = torch.hub.load('nicolalandro/ntsnet-cub200', 'ntsnet',
                       pretrained=True,
                       **{'topN': 6, 'device': 'cpu', 'num_classes': 200})
model.eval()

url = '''
https://raw.githubusercontent.com/nicolalandro/ntsnet-cub200/master/images/nts-net.png
'''
img = Image.open(urllib.request.urlopen(url))
scaled_img = transform_test(img)
torch_images = scaled_img.unsqueeze(0)

with torch.no_grad():
    top_n_coordinates, concat_out, raw_logits, concat_logits, \
        part_logits, top_n_index, top_n_prob = model(torch_images)

    _, predict = torch.max(concat_logits, 1)
    pred_id = predict.item()
    my_bird_class = model.bird_classes[pred_id]
    print('bird class:', my_bird_class)


class TestBirdClassifier(unittest.TestCase):
    '''Test suite for bird classifier'''

    def test_result_range(self):
        self.assertTrue(pred_id < len(model.bird_classes))

    def test_result(self):
        self.assertEqual(my_bird_class, '153.Philadelphia_Vireo')


unittest.main()
