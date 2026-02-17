import torch
import torch.nn as nn

class GRUModel(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(GRUModel, self).__init__()
        self.gru = nn.GRU(input_size, hidden_size, batch_first=True)
        self.fc = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        # x: (batch_size, sequence_length, input_size)
        out, _ = self.gru(x)
        # Get the last time step output
        out = out[:, -1, :]
        out = self.fc(out)
        return out

# Prediction logic

def predict(model, input_data):
    model.eval()  # Set the model to evaluation mode
    with torch.no_grad():
        input_tensor = torch.tensor(input_data, dtype=torch.float32).unsqueeze(0)  # Add batch dimension
        output = model(input_tensor)
        return output.numpy()  # Convert to numpy array for easier handling