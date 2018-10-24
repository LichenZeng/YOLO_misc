import torch

if __name__ == '__main__':
    x = torch.randn(size=(2, 3, 4, 5))
    print(x.size())

    b = x.view(-1, 5, 4, 3, 1)
    print(b.size())
