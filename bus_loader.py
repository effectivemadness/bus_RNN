# References
# https://github.com/yunjey/pytorch-tutorial/blob/master/tutorials/01-basics/pytorch_basics/main.py
# http://pytorch.org/tutorials/beginner/data_loading_tutorial.html#dataset-class
import torch
import numpy as np
from torch.autograd import Variable
from torch.utils.data import Dataset, DataLoader
import csv
import gzip


class NameDataset(Dataset):
    """ Diabetes dataset."""

    # Initialize your data, download, etc.
    def __init__(self, is_train_set=False):
        filename = './bus_trainset.csv.gz' if is_train_set else './bus_testset.csv.gz'
        with gzip.open(filename, "rt") as f:
            reader = csv.reader(f)
            rows = list(reader)

        self.names = [row[0] for row in rows]
        self.color = [row[1] for row in rows]
        self.len = len(self.color)

        self.color_list = list(sorted(set(self.color)))

    def __getitem__(self, index):
        return self.names[index], self.color[index]

    def __len__(self):
        return self.len

    def get_color(self):
        return self.color_list

    def get_color_spc(self, id):
        return self.color_list[id]

    def get_color_spc_id(self, color):
        return self.color_list.index(color)

