import torch


def pinn_residual(model, t):
    """
    Example residual for a simple ODE:
    dx/dt = -x
    Replace with biological signaling equations later.
    """

    t.requires_grad_(True)
    x = model(t)

    dx_dt = torch.autograd.grad(
        x,
        t,
        grad_outputs=torch.ones_like(x),
        create_graph=True
    )[0]

#    dNFkB_dt = k1 * receptor_activation - k2 * NFkB
#residual = dNFkB_dt - (k1 * receptor_activation - k2 * NFkB)
    residual = dx_dt + x
    return residual


def pinn_loss(model, t):
    """
    Total PINN loss: physics residual + data term (optional)
    """

    residual = pinn_residual(model, t)
    loss_physics = torch.mean(residual ** 2)

    return loss_physics
