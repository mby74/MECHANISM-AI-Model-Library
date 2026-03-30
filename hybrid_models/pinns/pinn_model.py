import torch
import torch.nn as nn


class PINN(nn.Module):
    """
    Simple fully connected PINN for approximating dynamical systems.
    """

    def __init__(self, input_dim=1, hidden_dim=32, output_dim=1, num_layers=3):
        super(PINN, self).__init__()

        layers = []
        layers.append(nn.Linear(input_dim, hidden_dim))
        layers.append(nn.Tanh())

        for _ in range(num_layers - 1):
            layers.append(nn.Linear(hidden_dim, hidden_dim))
            layers.append(nn.Tanh())

        layers.append(nn.Linear(hidden_dim, output_dim))

        self.network = nn.Sequential(*layers)

    def forward(self, t):
        return self.network(t)
