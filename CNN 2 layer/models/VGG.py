import torch.nn as nn
import torch.nn.functional as F
import torch
# The network should inherit from the nn.Module
##This is the 3 Layer CNN

class VGG(nn.Module):

    def __init__(self):
        super(VGG, self).__init__()

        self.layer1 = nn.Sequential(
            nn.Conv2d(in_channels=1, out_channels=32, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            nn.BatchNorm2d(32)
        )

        self.layer2 = nn.Sequential(
            nn.Conv2d(in_channels=16, out_channels=64, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2)
        )

        self.layer3 = nn.Sequential(
            nn.Conv2d(in_channels=32, out_channels=128, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            nn.BatchNorm2d(128)
        )

        self.layer4 = nn.Sequential(
            nn.Conv2d(in_channels=64, out_channels=256, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2)
        )
        self.flatten = nn.Flatten()
        self.fc1 = nn.Linear(512, 10)
        self.batch1 = nn.BatchNorm2d(512)
        self.fc2 = nn.Linear(512, 10)
        self.batch2 = nn.BatchNorm2d(512)
        self.softmax = nn.Softmax(dim=1)

    def forward(self, x):
        out = self.layer1(x)
        out = self.layer1(out)
        out = self.layer2(out)
        out = self.layer2(out)
        out = self.layer3(out)
        out = self.layer3(out)
        out = self.layer4(out)
        out = self.layer4(out)
        out = out.view(out.size(0), -1)
        out = self.flatten(out)
        out = F.relu(self.fc1(out))
        out = self.batch1(out)
        out = F.relu(self.fc2(out))
        out = self.batch2(out)
        out = self.softmax(out)
        return out