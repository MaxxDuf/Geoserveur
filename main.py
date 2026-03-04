# main.py
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI(title="GéoServeur Lya")

# Autoriser ton front à communiquer
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # tu peux mettre ton URL front spécifique plus tard
    allow_methods=["*"],
    allow_headers=["*"],
)

# Simuler ton IA pour l'instant
@app.post("/api/generate")
async def generate(request: Request):
    data = await request.json()
    prompt = data.get("prompt", "")
    model = data.get("model", "llama3")

    # Ici, tu peux connecter ton vrai modèle ou l'API interne
    # Pour l'instant, on renvoie un exemple générique
    response_text = f"Réponse simulée pour le prompt:\n{prompt[:200]}..."  # 200 chars max pour test

    return {"response": response_text}

# Route test simple
@app.get("/")
async def root():
    return {"message": "Serveur Lya en ligne"}
