from agno.agent import Agent
from agno.tools.tavily import TavilyTools
from agno.models.ollama import Ollama
# from agno.models.openai import OpenAIChat
# from agno.models.groq import Groq
from dotenv import load_dotenv
from agno.playground import Playground, serve_playground_app
load_dotenv()

def celsius_to_fh(temperatura_celsius: float):
    """
    Converte temperatura de Celsius para Fahrenheit.

    Args:
    temperatura_celsius (float): Temperatura em graus Celsius

    Returns:
    float: Temperatura convertida para Fahrenheit
    """
    return (temperatura_celsius * 9/5) + 32

# Criar o agente
agent = Agent(
    name="Agente de conversa",
    model=Ollama(id="llama3.1"),
    tools=[
        celsius_to_fh,
    ],
    debug_mode=True,
)

# Criar o playground
playground = Playground(agents=[agent])
app = playground.get_app()

if __name__ == "__main__":
    print("🚀 Iniciando Agno Playground...")
    print("📱 Acesse: http://localhost:7778")
    print("🌐 Ou use: https://app.agno.com/playground?endpoint=localhost%3A7778")
    print("⏹️  Pressione Ctrl+C para parar")
    print("-" * 50)
    
    serve_playground_app("inicio:app", reload=False, port=7778)

