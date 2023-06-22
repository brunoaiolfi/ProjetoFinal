from procedures.menu import menu
from products.create import createProduct
from products.update import updateProduct;
from validators.validateMenuOption import validateMenuOption;

optionSelected = 0
productList = []
isOptionValidated = False

# Enquanto a opção selecionada for diferente de sair(5)
while optionSelected != 5:

    # Função que printa o menu
    menu()

    # Enquanto a opção for inválida
    while isOptionValidated == False:
        optionSelected = int(input('Opção desejada: '))
        isOptionValidated = validateMenuOption(optionSelected)

    # Cadastro
    if (optionSelected == 1):
        productList = createProduct(productList)
    
    if (optionSelected == 2):
        productList = updateProduct(productList)

    optionSelected = 0
    isOptionValidated = False


