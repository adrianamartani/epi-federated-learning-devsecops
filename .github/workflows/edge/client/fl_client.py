import flwr as fl
import numpy as np
import torch
import os

class DummyNet(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = torch.nn.Linear(10,2)
    def forward(self,x):
        return self.fc(x)

def get_params(model):
    return [val.cpu().numpy() for _, val in model.state_dict().items()]

def set_params(model, params):
    params_dict = {k: torch.tensor(v) for k,v in zip(model.state_dict().keys(), params)}
    model.load_state_dict(params_dict)

class FlowerClient(fl.client.NumPyClient):
    def __init__(self, model):
        self.model = model

    def get_parameters(self):
        return get_params(self.model)

    def fit(self, parameters, config):
        set_params(self.model, parameters)
        # estoque de "treino" fictício
        opt = torch.optim.SGD(self.model.parameters(), lr=0.01)
        x = torch.randn(4,10)
        y = torch.tensor([0,1,0,1])
        for _ in range(int(config.get("epochs",1))):
            out = self.model(x)
            loss = torch.nn.functional.cross_entropy(out, y)
            opt.zero_grad()
            loss.backward()
            opt.step()
        return get_params(self.model), 4, {}

    def evaluate(self, parameters, config):
        return 0.5, 4, {}

if __name__ == "__main__":
    server = os.getenv("FLOWER_SERVER", "SERVER_PUBLIC_IP:8080")
    model = DummyNet()
    client = FlowerClient(model)
    print("Starting Flower client connecting to", server)
    fl.client.start_numpy_client(server_address=server, client=client)
