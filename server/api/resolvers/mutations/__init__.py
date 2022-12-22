from ariadne import MutationType
from api.models import *
from api.types import *
import io
from api.models.pytorch import *
import soundfile as sf
import numpy as np

mutation = MutationType()
@mutation.field("classifyHeatBeatSound")
async def create_session_resolver(obj, info, input):
    try:
        ext = "."+str(input['audio'].filename).split('.')[-1]
        if not ext in allowed_extensions:
            return {
                "ok" : False,
                "error": {
                    "field" : 'audio',
                    "message" : f'Only audios with extensions ({", ".join(allowed_extensions)}) are allowed.'
                }
            }
        audio = await input['audio'].read()
        audio = io.BytesIO(audio)
        waveform, samplerate = sf.read(file=audio, dtype='float32')
        waveform = torch.from_numpy(np.array([waveform]))
        res = predict_sound(hbsc_model, waveform, device)
        return {
           'ok': True,
           'prediction': res.to_json() 
        }
    except Exception as e:
       print(e)
       return {
           "ok": False,
           "error":{
               "field": 'server',
               'message':  "Something went wrong on the server."
           }
       }
