from agno.agent import Agent
from agno.models.ollama import Ollama
from agno.playground import Playground
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json

def celsius_to_fh(temperatura_celsius: float):
    """Converte temperatura de Celsius para Fahrenheit."""
    return (temperatura_celsius * 9/5) + 32

# Criar agente
agent = Agent(
    name="Meu Agente",
    model=Ollama(id="llama3.1"),
    tools=[celsius_to_fh],
)

# Criar app FastAPI
app = FastAPI(title="Agno Playground")

# Adicionar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rotas necessárias para o playground web
@app.get("/playground/status")
async def get_status():
    return {"status": "running", "agents": ["Meu Agente"]}

@app.get("/playground/agents")
async def get_agents():
    return {"agents": ["Meu Agente"]}

@app.post("/playground/chat")
async def chat(request: dict):
    try:
        message = request.get("message", "")
        response = agent.run(message)
        return {"response": response.content}
    except Exception as e:
        return {"error": str(e)}

@app.get("/")
async def root():
    return {"message": "Agno Playground API", "status": "running"}

if __name__ == "__main__":
    print("🚀 Iniciando Agno Playground...")
    print("📱 Acesse: http://localhost:7778")
    print("🌐 Ou use: https://app.agno.com/playground?endpoint=localhost%3A7778")
    print("-" * 50)
    
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=7778,
        reload=False
    ) 