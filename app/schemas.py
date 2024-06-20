from pydantic import BaseModel

class InputSentence(BaseModel):
    sentence: str
