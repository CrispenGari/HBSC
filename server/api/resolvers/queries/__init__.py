from ariadne import QueryType
from api.types import * 

query = QueryType()
@query.field("meta")
def meta_resolver(obj, info):
   return Meta(
      programmer = "@crispengari",
      main = "Heart Beat Sound Classification (HBSC)",
      description = "This is a graphql API for classifying heart beat sounds into 4 different categories from audios in real time. Given an audio of a heartbeat sound the API should be able to classify the sound's category with 100% confidence.",
      language = "python",
      libraries = ["pytorch", "torchaudio"],
   ).to_json()
   