class CaesarCipherQueue:
    def __init__(self, chave):
        self.fila = []
        self.chave = chave

    # Enfileira cada caractere do texto para ser cifrado
    def enqueue_text(self, texto):
        for char in texto:
            self.fila.append(char)

    # Desenfileira e aplica a cifra de César em cada caractere
    def encrypt(self):
        encrypted_text = ""
        
        while self.fila:
            char = self.fila.pop(0)  # Desenfileira o primeiro caractere
            
            # Aplica a cifra de César apenas em letras
            if char.isupper():
                encrypted_char = chr((ord(char) - 65 + self.chave) % 26 + 65)
            elif char.islower():
                encrypted_char = chr((ord(char) - 97 + self.chave) % 26 + 97)
            else:
                encrypted_char = char  # Mantém o caractere se não for letra
            
            encrypted_text += encrypted_char
        
        return encrypted_text


chave = int(input("Insira a chave: "))
texto = input("Insira o texto: ")

# Cria a fila da cifra de César
cipher_queue = CaesarCipherQueue(chave)
cipher_queue.enqueue_text(texto)

# Criptografa o texto e exibe o resultado
ciphered_text = cipher_queue.encrypt()
print("Texto criptografado:", ciphered_text)

# Exemplos de uso:
# Insira a chave: 2
# Insira um texto: Algoritmos
# Texto criptografado: Cniqtkvoqu

# o mesmo ocorre quando se usa a chave "28"