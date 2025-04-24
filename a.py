import matplotlib.pyplot as plt

# Dados com nomes e contexto
dados = [
    ["Ana",     "S1000", 23, "Female", 0.0, 1.2, 1.1, "No", 85.0, 8.0, "Fair"],
    ["Bianca",  "S1001", 20, "Female", 6.9, 2.8, 2.3, "No", 97.3, 4.6, "Good"],
    ["Carlos",  "S1002", 21, "Male",   1.4, 3.1, 1.3, "No", 94.8, 8.0, "Poor"],
    ["Daniela", "S1003", 23, "Female", 1.0, 3.9, 1.0, "No", 71.0, 9.2, "Poor"],
    ["Eduarda", "S1004", 19, "Female", 5.0, 4.4, 0.5, "No", 90.9, 4.9, "Fair"]
]

# Rótulos principais
rotulos = [f"{linha[0]} ({linha[-1]})" for linha in dados]

# Valores (soma de estudo, redes e Netflix)
valores = [sum(linha[4:7]) for linha in dados]

# Cores personalizadas
cores = ['#FF9999','#66B2FF','#99FF99','#FFCC99','#C2C2F0']

# Detalhes adicionais para a legenda
detalhes = [
    f"{linha[0]} - {linha[2]} anos\nEstudo: {linha[4]}h\nRedes: {linha[5]}h\nNetflix: {linha[6]}h\nSono: {linha[9]}h\nDieta: {linha[-1]}"
    for linha in dados
]

# Criar o gráfico
fig, ax = plt.subplots(figsize=(8, 8))
wedges, texts, autotexts = ax.pie(
    valores,
    labels=rotulos,
    autopct='%1.1f%%',
    startangle=140,
    colors=cores,
    textprops=dict(color="black", fontsize=10)
)

# Legenda ao lado com informações detalhadas
ax.legend(wedges, detalhes, title="Detalhes dos Estudantes", loc="center left", bbox_to_anchor=(1, 0.5), fontsize=9)

# Título e estilo
ax.set_title("Distribuição de Tempo (Estudo + Redes + Netflix)\ncom Perfil de Estudantes", fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()
