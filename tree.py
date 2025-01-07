from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

# Dados de exemplo: ingredientes disponíveis e receitas sugeridas
X = [
    [1, 1, 1, 0, 0],  # Ovo, farinha, açúcar (Bolo)
    [1, 0, 0, 1, 0],  # Ovo, queijo (Omelete)
    [0, 1, 1, 0, 1],  # Farinha, açúcar, manteiga (Biscoito)
    [1, 1, 0, 1, 0],  # Ovo, farinha, queijo (Panqueca)
    [0, 0, 1, 1, 1],  # Açúcar, queijo, manteiga (Doce de queijo)
]

# Rótulos correspondentes às receitas
y = ["Bolo", "Omelete", "Biscoito", "Panqueca", "Doce de queijo"]

# Nomes das características (ingredientes)
feature_names = ["Ovo", "Farinha", "Açúcar", "Queijo", "Manteiga"]

# Criar e treinar a árvore de decisão
clf = DecisionTreeClassifier(criterion="gini", max_depth=3, random_state=42)
clf.fit(X, y)

# Função para capturar os ingredientes disponíveis
def capturar_ingredientes():
    print("\nDigite os ingredientes disponíveis (sim = 1, não = 0):")
    user_ingredients = []
    for feature in feature_names:
        while True:
            resposta = input(f"Você tem {feature.lower()}? (1 = Sim, 0 = Não): ")
            if resposta in ["0", "1"]:
                user_ingredients.append(int(resposta))
                break
            else:
                print("Por favor, insira 1 para 'Sim' ou 0 para 'Não'.")
    return user_ingredients

# Função para verificar receitas possíveis com os ingredientes fornecidos
def verificar_receitas(user_ingredients):
    possiveis = []
    faltantes = []

    for i, receita in enumerate(X):
        # Verificar se todos os ingredientes necessários para a receita estão disponíveis
        diferenca = [feature_names[j] for j in range(len(user_ingredients)) if receita[j] == 1 and user_ingredients[j] == 0]
        if not diferenca:
            return y[i], []  # Receita completa encontrada
        else:
            possiveis.append((y[i], diferenca))
    
    return None, possiveis

# Capturar os ingredientes do usuário
ingredientes_disponiveis = capturar_ingredientes()

# Verificar se é possível fazer uma receita
receita, receitas_possiveis = verificar_receitas(ingredientes_disponiveis)

if receita:
    print(f"\nCom os ingredientes disponíveis, você pode fazer: {receita}")
else:
    print("\nCom os ingredientes disponíveis, não é possível fazer uma receita completa.")
    print("Aqui estão as receitas possíveis e os ingredientes que faltam:")
    for nome, faltando in receitas_possiveis:
        print(f"- {nome}: falta {', '.join(faltando)}")

# Visualizar a árvore de decisão
plt.figure(figsize=(12, 8))
plot_tree(clf, feature_names=feature_names, class_names=clf.classes_, filled=True)
plt.title("Árvore de Decisão para Receitas")
plt.show()
