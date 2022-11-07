frase = str('Luan santos').strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
print(junto, len(junto))
for letra in range(len(junto) -1, -1, -1):
    inverso = inverso + junto[letra]
print(inverso)