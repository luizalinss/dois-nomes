def calcular_soma_e_media(lista):
    soma = sum(lista)
    media = soma / len(lista) if len(lista) > 0 else 0
    return soma, media

# Exemplo de utilização:
lista_de_numeros = [1, 2, 3, 4, 5]
soma, media = calcular_soma_e_media(lista_de_numeros)
print("A soma da lista é:", soma)
print("A média da lista é:", media)
def substituir_palavra(lista, palavra_antiga, palavra_nova):
    nova_lista = [palavra_nova if palavra == palavra_antiga else palavra for palavra in lista]
    return nova_lista

# Exemplo de utilização:
lista_de_palavras = ['morango', 'banana', 'limão']
palavra_antiga = 'morango'
palavra_nova = 'framboesa'
nova_lista = substituir_palavra(lista_de_palavras, palavra_antiga, palavra_nova)
print("Lista original:", lista_de_palavras)
print("Lista com substituição:", nova_lista)
def triangulo_asteriscos(numero_linhas):
    for i in range(1, numero_linhas + 1):
        print("*" * i)

def funcl (a):
    return sum(a), sum(a)/len(a)

def substituir_palavra(lista, palavra_procurada, nova_palavra):
    return [nova_palavra if palavra == palavra_procurada else palavra for palavra in lista]


lista_palavras = ["banana", "morango", "limão"]
nova_lista = substituir_palavra(lista_palavras, "morango", "maçã")
print("Lista alterada:", nova_lista)

def gerar_triangulo (num_linhas):
    for i in range(1, num_linhas + 1):
        print('*' * i)

num_linhas = 4
gerar_triangulo(num_linhas)
