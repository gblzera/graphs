import matplotlib.pyplot as plt
import numpy as np

# --- 1. CONFIGURAÇÃO DA SIMULAÇÃO ---

POPULACAO_TOTAL = 1000
GERACOES = 300 # Como você pediu

# Parâmetros do Dilema
# Com estes valores, os Egoístas vão "contaminar" e vencer.
T = 0.5  # Tentação
R = 3  # Recompensa
P = 0.25  # Punição
S = 0.1  # Otário

# --- 2. INICIALIZAÇÃO DA POPULAÇÃO ---

# Começamos com 500 de cada (50/50)
num_cooperadores = 900.0 # Usar float para cálculos de proporção
num_egoistas = 100.0

# --- 3. CONFIGURAÇÃO DA VISUALIZAÇÃO ---

plt.ion() # Ligar modo interativo para animação
fig, ax = plt.subplots(figsize=(8, 6))

# Define as categorias e as cores das barras
categorias = ['Egoístas', 'Cooperadores']
cores = ['#FF5733', '#33FF57'] # Vermelho para Egoístas, Verde para Cooperadores

# Desenha as barras iniciais e guarda a referência 'bar_container'
bar_container = ax.bar(categorias, [num_egoistas, num_cooperadores], color=cores)

# Configurações do gráfico
ax.set_title("Geração 0")
ax.set_ylim(0, POPULACAO_TOTAL) # Trava o eixo Y de 0 a 1000
ax.set_ylabel("Número de Indivíduos")

plt.tight_layout()

# --- 4. O LOOP DA SIMULAÇÃO (GERAÇÃO POR GERAÇÃO) ---

for g in range(GERACOES):
    
    # 4.1. Calcula as proporções atuais
    # (Evita divisão por zero se uma população for extinta)
    if POPULACAO_TOTAL == 0:
        break 
        
    prop_cooperadores = num_cooperadores / POPULACAO_TOTAL
    prop_egoistas = num_egoistas / POPULACAO_TOTAL

    # 4.2. Calcula a Pontuação (Fitness) Média de cada estratégia
    
    # Fitness do Cooperador: (Chance de encontrar C * R) + (Chance de encontrar E * S)
    fit_cooperador = (prop_cooperadores * R) + (prop_egoistas * S)
    
    # Fitness do Egoísta: (Chance de encontrar C * T) + (Chance de encontrar E * P)
    fit_egoista = (prop_cooperadores * T) + (prop_egoistas * P)

    # 4.3. Calcula o Fitness Médio da população inteira
    fit_medio_total = (prop_cooperadores * fit_cooperador) + (prop_egoistas * fit_egoista)

    # 4.4. EVOLUÇÃO: Calcula a nova população (Dinâmica do Replicador)
    if fit_medio_total > 0:
        # A nova % de cada grupo é sua % atual * (seu fitness / fitness médio)
        num_cooperadores = (prop_cooperadores * fit_cooperador / fit_medio_total) * POPULACAO_TOTAL
        num_egoistas = (prop_egoistas * fit_egoista / fit_medio_total) * POPULACAO_TOTAL
    else:
        # Se o fitness for 0, ninguém se reproduz, a população não muda
        pass
    
    # 4.5. ATUALIZAÇÃO VISUAL
    
    # Pega as barras individuais
    barra_egoista = bar_container[0]
    barra_cooperador = bar_container[1]
    
    # Atualiza a ALTURA de cada barra
    barra_egoista.set_height(num_egoistas)
    barra_cooperador.set_height(num_cooperadores)
    
    # Atualiza o título
    ax.set_title(f"Geração {g + 1}")
    
    # Pausa rápida para o Matplotlib desenhar. 
    # Use 0.1 para mais lento, 0.01 para mais rápido.
    plt.pause(0.05) 

# --- 5. FIM DA SIMULAÇÃO ---
print("Simulação concluída.")
ax.set_title(f"Resultado Final (Geração {GERACOES})")
plt.ioff() # Desliga o modo interativo
plt.show() # Mantém a janela final aberta