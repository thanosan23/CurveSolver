import numpy as np
import torch
import pandas as pd

class config:
    filename = 'data.csv'
    x_column = 'x'
    y_column = 'y'

data = pd.read_csv(config.filename)
x = np.array(data[config.x_column], dtype=np.float32)
y = np.array(data[config.y_column], dtype=np.float32)

x = torch.tensor(x)
y = torch.tensor(y)

# uses the log trick
x_log = np.log(x)
y_log = np.log(y)

m = torch.rand(1, requires_grad=True)
y_int = torch.rand(1, requires_grad=True)

optim = torch.optim.Adam(params=[m, y_int], lr=1e-1)
criterion = torch.nn.MSELoss()

for i in range(1000):
    y_pred = m*x_log + y_int
    loss = criterion(y_pred, y_log)

    optim.zero_grad()
    loss.backward()
    optim.step()

m = m.item()
y_int = y_int.item()
y_int = np.e**y_int

print(f"The curve of best fit is: {y_int:.1f}x^{m:.1f}")
