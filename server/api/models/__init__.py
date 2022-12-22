import torch
import os
import torchaudio
from api.types import *
import numpy as np

# torch device
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# allowed extensions
allowed_extensions = ['.wav', '.WAV', '.mp3', '.MP3']

# Model name
MODEL_NAME = "hbsc-model.pt"
# Model paths
PYTORCH_HBSC_MODEL_PATH = os.path.join(os.getcwd(),
                                      f"api/models/static/{MODEL_NAME}"
                                      )

classes = ['artifact', 'extrahls', 'murmur', 'normal' ]

new_sample_rate = 8000
sample_rate = 44100
resample_transform = torchaudio.transforms.Resample(orig_freq=sample_rate,
                                           new_freq=new_sample_rate)

def pad_sequence(batch):
    batch = torch.nn.utils.rnn.pad_sequence([batch], batch_first=True, padding_value=0.)
    return batch

def preprocess(waveform):
    waveform = pad_sequence(waveform)
    return resample_transform(waveform)

def predict_sound(model, waveform, device): 
    model.eval()
    with torch.no_grad():
        waveform = preprocess(waveform).to(device)
        probabilities = torch.softmax(model(waveform).squeeze(), dim=0)
        prediction = torch.argmax(probabilities)
        prediction = prediction.detach().cpu().item()
        predictions = [
            Prediction(
                label = i,
                className = classes[i],
                confidence = float(np.round(probabilities[i], 2))
            ) for i, _ in enumerate(probabilities)
        ]
        predicted = Prediction(
            label = prediction,
            className = classes[prediction],
            confidence = float(np.round(probabilities[prediction], 2))
        )
        return PredictionResponse(
            topPrediction = predicted,
            predictions = predictions
        )