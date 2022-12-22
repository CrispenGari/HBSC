class Meta:
    def __init__(self,
                 programmer:str,
                 main: str,
                 description: str,
                 language: str,
                 libraries: list
                 ):
        self.programmer = programmer
        self.main = main
        self.description = description
        self.language = language
        self.libraries= libraries
        
    def to_json(self):
        return{
            "programmer": self.programmer,
            "main": self.main,
            "description": self.description,
            "language": self.language,
            "libraries": self.libraries,
        }
        
class Error:
    def __init__(self, field: str, message: str):
        self.field = field
        self.message = message
        
    def __repr__(self) -> str:
        return f"<Error: ${self.message}>"

    def __str__(self) -> str:
        return f"<Error: ${self.message}>"

    def to_json(self):
        return {
            'field':  self.field,
            'message':  self.message,
        }
        
class Prediction:
    def __init__(self, className: str, label: int, confidence: float):
        self.className = className
        self.confidence = confidence
        self.label = label

    def __repr__(self) -> str:
        return f"<Prediction: {self.className}>"

    def __str__(self) -> str:
        return f"<Prediction: {self.className}>"

    def to_json(self):
        return {
            'className':  self.className,
            'label':  self.label,
            'confidence':  self.confidence,
        }
     
     
class PredictionResponse:
    def __init__(self, topPrediction: Prediction, predictions:list) -> None:
        self.predictions = predictions
        self.topPrediction = topPrediction
        
    def __repr__(self) -> str:
        return f"<Prediction Response: {self.topPrediction.className}>"
    
    def __str__(self) -> str:
        return f"<Prediction Response: {self.topPrediction.className}>"
    
    def to_json(self):
        return{
           "predictions": [item.to_json() for item in self.predictions],
            "topPrediction": self.topPrediction.to_json()
        }