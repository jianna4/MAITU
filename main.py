import requests
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()
@app.get("/")
def read_root():
    return {"message": "Welcome to the chatbot API"}
# 🔹 Use your free Together AI API key
TOGETHER_API_KEY = "01d14f38cd11da2c0b541d994c2fa8bcc7a5853844818011b6dcd1627766c7d7"
#this should not be seen
class ChatRequest(BaseModel):
    message: str

@app.post("/chat/")
async def chat(request: ChatRequest):
    try:
        url = "https://api.together.xyz/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {TOGETHER_API_KEY}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": "meta-llama/Llama-3.3-70B-Instruct-Turbo",  # ✅ Use a free model
            "messages": [{"role": "user", "content": request.message}]
        }
        
        response = requests.post(url, json=payload, headers=headers)
        response_json = response.json()
        
        return {"response": response_json["choices"][0]["message"]["content"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
