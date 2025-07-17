from agno.agent import Agent
from agno.models.ollama import Ollama
from agno.playground import Playground
import uvicorn

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

if __name__ == "__main__":
    print("🚀 Iniciando Agno Playground...")
    print("📱 Acesse: http://localhost:7778")
    print("🌐 Ou use: https://app.agno.com/playground?endpoint=localhost%3A7778")
    print("-" * 50)
    
    # Usar uvicorn com o app do playground
    uvicorn.run(
        playground.get_app(),
        host="0.0.0.0",
        port=7778,
        reload=False
    ) 