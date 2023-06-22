def createProduct(productList):
    tempProductList = list(productList)

    produto = {
        "id" : len(productList), # Campo unico, por ser o tamanho da lista consequentemente já é o index
        "type": "",
        "name": "",
        "price": 0,
        "quant": 0
    }

    while produto["name"] == "":
        produto["name"] = input('Nome do produto: ')

        if (produto["name"] == ""):
            print("Nome inválido")
    
    while produto["type"] == "":
        produto["type"] = input('Tipo de produto (Pão, Bolo, Salgado, Bebida, etc.): ')

        if (produto["type"] == ""):
            print("Produto invalido")

    while produto["price"] <= 0 or produto["price"] == "":
        produto["price"] = int(input('Preço de venda: '))

        if (produto["price"] <= 0):
            print("Nome inválido")
    
    while produto["quant"] <= 0 or produto["quant"] == "":
        produto["quant"] = int(input('Estoque inicial: '))

        if (produto["quant"] <= 0):
            print("Produto invalido")
    

    tempProductList.append(produto)

    return tempProductList 



   



