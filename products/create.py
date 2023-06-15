def createProduct(productList):
    tempProductList = list(productList)

    produto = {
        "id" : 1,
        "type": "",
        "name": "",
        "price": 0,
        "quant": 0
    }

    produto["name"] = input('Nome do produto.')
    produto["type"] = input('Tipo de produto (Pão, Bolo, Salgado, Bebida, etc.).')
    produto["price"] = input('Preço de venda.')
    produto["quant"] = input('Estoque inicial.')

    tempProductList.append(produto)

    return tempProductList 

   



