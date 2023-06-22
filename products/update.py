def updateProduct(productList):
    tempProductList = list(productList)

    print("Selecione um produto da lista: ")
    print("")
    
    for product in productList:
        print("ID: "+str(product["id"])+" Produto: "+product["name"])
        print("")

    # int(optionSelected) in options

    optionSelected = -1
    idExist = False

    while idExist == False:
        optionSelected = int(input('ID do produto: '))
        
        for product in productList:
            if (optionSelected == product["id"]):
                idExist = True

    productList[optionSelected]["name"] = input('Nome do produto: ')
    productList[optionSelected]["type"] = input('Tipo de produto (Pão, Bolo, Salgado, Bebida, etc.): ')
    productList[optionSelected]["price"] = input('Preço de venda: ')
    productList[optionSelected]["quant"] = input('Estoque inicial: ')

    return tempProductList 

   



