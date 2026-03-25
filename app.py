from flask import Flask, request, render_template
import torch
import numpy as np

app = Flask(__name__)

# Load model
import torch
import torch.nn as nn

# Step 1: Define SAME model architecture
class ANNModel(nn.Module):
    def __init__(self):
        super(ANNModel, self).__init__()
        self.model = nn.Sequential(
            nn.Linear(4, 16),
            nn.ReLU(),
            nn.Linear(16, 8),
            nn.ReLU(),
            nn.Linear(8, 1)
        )

    def forward(self, x):
        return self.model(x)

# Step 2: Create model object
model = ANNModel()

# Step 3: Load weights (THIS is the fix)
model.load_state_dict(torch.load("best_model.pt"))

# Step 4: Set eval mode
model.eval()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get input values from form
        at = float(request.form["AT"])
        v = float(request.form["V"])
        ap = float(request.form["AP"])
        rh = float(request.form["RH"])

        # Convert to tensor
        input_data = torch.tensor([[at, v, ap, rh]], dtype=torch.float32)

        # Prediction
        output = model(input_data).item()

        return render_template("index.html", prediction_text=f"Predicted Energy Output: {output:.2f}")

    except:
        return render_template("index.html", prediction_text="Error in input!")

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)