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
    return [user_ingredients]

# Solicitar os ingredientes ao usuário
ingredientes_disponiveis = capturar_ingredientes()

# Fazer a previsão com os ingredientes fornecidos
previsao = clf.predict(ingredientes_disponiveis)
print(f"\nCom os ingredientes disponíveis, você pode fazer: {previsao[0]}")

# Visualizar a árvore de decisão
plt.figure(figsize=(12, 8))
plot_tree(clf, feature_names=feature_names, class_names=clf.classes_, filled=True)
plt.title("Árvore de Decisão para Receitas")
plt.show()
