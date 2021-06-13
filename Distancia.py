from geopy.geocoders import Nominatim
from geopy import distance


# Função para a realização de pedidos
def realizarpedido():
    # Formulário de Dados
    nome = input("Digite seu nome:")
    cep = input("Digite seu cep: ")
    pedido = input("Digite o nome do objeto que está sendo encomendado: ")
    valor = float(input("Valor do pedido: (00.00)  "))
    promo = int(input("Você deseja inserir o valor de um código promocional: 1 para sim e 2 para não  "))

    geolocator = Nominatim(user_agent="App de Encomenda")

    # Calculo de Distancia
    Vendedor = input("Digite o local do Vendedor: ")
    destinatario = input("Digite o local do Cliente: ")

    local_vendedor = geolocator.geocode(Vendedor)
    local_destinatario = geolocator.geocode(destinatario)

    local_v = (local_vendedor.latitude, local_vendedor.longitude)
    local_d = (local_destinatario.latitude, local_destinatario.longitude)

    distancia = distance.distance(local_v, local_d).km

    frete = distancia / valor * 0.15

    # Gerando o Formulário em Txt
    dadosTxt = open('Formulário_do_Pedido.txt', 'a')
    dadosTxt.write("\n\n------------------Formulário do Pedido-----------------")
    dadosTxt.write("\nNome do cliente: ")
    dadosTxt.write(nome)
    dadosTxt.write("\nCep: ")
    dadosTxt.write(cep)
    dadosTxt.write("\nPedido: ")
    dadosTxt.write(pedido)
    dadosTxt.write("\nDistancia em KM: ")
    dadosTxt.write(str(distancia))



    # Promoções que são aplicadas conforme o valor do pedido
    if valor >= 10.00:
        valorFinal = valor + frete
        dadosTxt.write("\nValor Final: ")
        dadosTxt.write(str(valorFinal))
        dadosTxt.write("\n========================================================")
        print("valor total: ", valorFinal)
    if valor < 10.00:
        valorFinal_fg = valor + 00.00
        dadosTxt.write("\nValor Final com frete gratuito: ")
        dadosTxt.write(str(valorFinal_fg))
        dadosTxt.write("\n========================================================")
        print("valor total: ", valorFinal_fg)

    # Se o cliente possuir um valor de desconto ele pode utilizar nessa condição
    if promo == 1:
        cod = float(input("Valor do código: "))
        ValorPromo = valorFinal - cod
        dadosTxt.write("\nValor Final Promocional: ")
        dadosTxt.write(str(ValorPromo))
        dadosTxt.write("\n========================================================")
        print("Valor final promocional: ", ValorPromo)


# Inicialização do programa
op = int(input("Digite 1 para realizar o seu pedido: "))

while op != 0:
    print("----------Formulario de Pedido-------")
    if op == 1:
        realizarpedido()
    op = int(input("Digite 1 para realizar um novo pedido: "))
