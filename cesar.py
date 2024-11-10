def main():
    # Solicita a chave ao usuário e verifica se é um número válido
    chave_input = input("Insira a chave: ")
    
    # Verifica se a chave fornecida é um número
    if not chave_input.isdigit():
        print("A chave deve ser um número.")
        return 1

    # Converte a chave de string para inteiro
    chave = int(chave_input)

    # Requisição do texto a ser criptografado
    texto = input("Insira o texto: ")

    print("texto criptografado: ", end="")

    # Criptografa o texto
    for caractere in texto:
        # Se o caractere for uma letra maiúscula
        if caractere.isupper():
            print(chr((ord(caractere) - 65 + chave) % 26 + 65), end="")

        # Se o caractere for uma letra minúscula
        elif caractere.islower():
            print(chr((ord(caractere) - 97 + chave) % 26 + 97), end="")
            
        # Se não for uma letra, imprime o caractere original
        else:
            print(caractere, end="")

    # Imprime uma nova linha no final
    print()

if __name__ == "__main__":
    main()
