from fastapi import FastAPI
from pydantic import BaseModel
from typing import Literal

app = FastAPI(title="OpenAI Tool API")

class GetStartMethodResponse(BaseModel):
    method: str

@app.get("/GetStartMethod", response_model=GetStartMethodResponse, name="GetStartMethod")
def get_start_method(businessCase: str = Query(...)):
    # Find the first occurrence of "Day" followed by an integer (case-insensitive)
    match = re.search(r"Day\d+", businessCase, re.IGNORECASE)
    result = ""

    if match:
        if "Part1".lower() in businessCase.lower():
            result = f"{match.group()}.ProcessPart1Lines"
        else:
            result = f"{match.group()}.ProcessPart2Lines"

    return GetStartMethodResponse(method=result)
