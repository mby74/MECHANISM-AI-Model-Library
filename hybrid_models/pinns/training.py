import torch
from pinn_model import PINN
from loss_functions import pinn_loss


def train_pinn(num_epochs=1000, lr=1e-3):
    model = PINN()
    optimizer = torch.optim.Adam(model.parameters(), lr=lr)

    t = torch.linspace(0, 1, 100).view(-1, 1)

    for epoch in range(num_epochs):
        optimizer.zero_grad()

        loss = pinn_loss(model, t)
        loss.backward()
        optimizer.step()

        if epoch % 100 == 0:
            print(f"Epoch {epoch}: Loss = {loss.item():.6f}")

    return model


if __name__ == "__main__":
    trained_model = train_pinn()
