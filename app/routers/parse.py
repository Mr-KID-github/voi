from fastapi import APIRouter
from app.schemas import InputSentence
from app.utils.parser import parse_input

router = APIRouter()

@router.post("/parse")
def parse_sentence(input_sentence: InputSentence):
    result = parse_input(input_sentence.sentence)
    return result
