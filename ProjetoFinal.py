from procedures.menu import menu
from products.create import createProduct;
from validators.validateMenuOption import validateMenuOption;

optionSelected = 0
productList = []
isOptionValidated = False

while optionSelected != 5:

    menu()

    while isOptionValidated == False:
        optionSelected = int(input('Opção desejada: '))
        isOptionValidated = validateMenuOption(optionSelected)

    if (optionSelected == 1):
        productList = createProduct(productList)
    
    print(productList)






    