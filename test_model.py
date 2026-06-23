import torch
from torchvision import transforms
from PIL import Image
import os

# -----------------------------
# DEVICE
# -----------------------------
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# -----------------------------
# MODEL DEFINITION
# -----------------------------
class Conv4(torch.nn.Module):
    def __init__(self):
        super(Conv4, self).__init__()
        self.layer = torch.nn.Sequential(
            torch.nn.Conv2d(1, 64, 3, padding=1),
            torch.nn.BatchNorm2d(64),
            torch.nn.ReLU(),
            torch.nn.MaxPool2d(2),
            torch.nn.Conv2d(64, 64, 3, padding=1),
            torch.nn.BatchNorm2d(64),
            torch.nn.ReLU(),
            torch.nn.MaxPool2d(2),
            torch.nn.Conv2d(64, 64, 3, padding=1),
            torch.nn.BatchNorm2d(64),
            torch.nn.ReLU(),
            torch.nn.MaxPool2d(2),
            torch.nn.Conv2d(64, 64, 3, padding=1),
            torch.nn.BatchNorm2d(64),
            torch.nn.ReLU(),
            torch.nn.MaxPool2d(2)
        )

    def forward(self, x):
        x = self.layer(x)
        return x.view(x.size(0), -1)

# -----------------------------
# LOAD TRAINED MODEL
# -----------------------------
state = torch.load("trained_fewshot_model.pth", map_location=device)
if isinstance(state, dict):
    model = Conv4().to(device)
    model.load_state_dict(state)
else:
    model = state.to(device)
model.eval()

print("Model loaded successfully!")

# -----------------------------
# IMAGE TRANSFORMS
# MUST match training transforms
# -----------------------------
transform = transforms.Compose([
    transforms.Grayscale(num_output_channels=1),   # remove if trained on RGB
    transforms.Resize((28, 28)),                   # change if needed
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,))
])

# -----------------------------
# CLASS NAMES
# Example:
# character01 -> German/Korean char
# character02 -> German/Korean char
# ...
# -----------------------------
class_names = [
    "character01",
    "character02",
    "character03",
    "character04",
    "character05",
    "character06",
    "character07",
    "character08",
    "character09",
    "character10"
]

# -----------------------------
# PREDICT SINGLE IMAGE
# -----------------------------
def predict_image(image_path):

    # Load image
    image = Image.open(image_path).convert("L")

    # Apply transforms
    image = transform(image)

    # Add batch dimension
    image = image.unsqueeze(0).to(device)

    # Prediction
    with torch.no_grad():

        outputs = model(image)

        _, predicted = torch.max(outputs, 1)

        predicted_class = class_names[predicted.item()]

    print(f"\nImage: {image_path}")
    print(f"Predicted Class: {predicted_class}")

# -----------------------------
# TEST ALL REAL-WORLD IMAGES
# -----------------------------
test_folder = "real_test_images"

for filename in os.listdir(test_folder):

    if filename.lower().endswith((".png", ".jpg", ".jpeg")):

        image_path = os.path.join(test_folder, filename)

        predict_image(image_path)