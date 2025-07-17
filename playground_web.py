from agno.agent import Agent
from agno.models.ollama import Ollama
from agno.playground import Playground
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

def celsius_to_fh(temperatura_celsius: float):
    """Converte temperatura de Celsius para Fahrenheit."""
    return (temperatura_celsius * 9/5) + 32

# Criar agente
agent = Agent(
    name="Meu Agente",
    model=Ollama(id="llama3.1"),
    tools=[celsius_to_fh],
)

# Criar playground
playground = Playground(agents=[agent])
app = playground.get_app()

# Adicionar CORS para permitir conexão com o playground web
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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