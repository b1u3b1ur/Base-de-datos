class Dish():
    def set_dish_information(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.dish = f'{self.name} {self.quantity} - {self.price}'
    def get_dish_information(self):
        return self.dish

class Menu():
    def set_menu_information(self, name):
        self.name = name
        self.products = []
    def set_menu(self, dish):
        self.dish = dish
        self.products.append(self.dish)
    def get_menu(self):
        print(self.name)
        return self.products

class Receipt():
    result = 0
    def set_order_information(self, name):
        self.name = name
        self.order = []
    def set_order(self, parametr1, parametr2):
        self.parametr1 = parametr1
        self.order.append(self.parametr1)
        self.parametr2 = parametr2
        self.result = self.result + int(self.parametr2)
    def get_order(self):
        print("Comprobación general: ")
        return self.order
    def get_result(self):
        print("Total: ")
        return self.result

def menu_entry(name_menu):
    for i in range(question1):
        name = input("Ingrese el nombre del plato: ")
        quantity = input("Ingrese el tamaño de la porción: ")
        price = input("Ingrese el precio de 1 porción: ")
        d = Dish()
        d.set_dish_information(name, quantity, price)
        name_menu.set_menu(d)

def menu_output(name_menu):
    name_menu.get_menu()
    for i in name_menu.products:
        print(f'{i.name} ({i.quantity}g.) - {i.price}$')

def order_entry(name_menu):
    for i in range(question4):
        question = input("Ingrese el nombre del plato: ")
        for j in name_menu.products:
            if j.name == question:
                check.set_order(j, j.price)
    check.get_order()
    for i in check.order:
        print(f'{i.name} ({i.quantity}g.) - {i.price}$')
    check.get_result()
    print(str(check.result) + "$")

breakfast = Menu()
lunch = Menu()
dinner = Menu()
check = Receipt()

breakfast.set_menu_information("Desayunos")
lunch.set_menu_information("Almuerzos")
dinner.set_menu_information("Cenas")
check.set_order_information("Hacer un pedido")

print('''
Este es un programa de menú.
Las siguientes acciones están disponibles en él:
    1 - Llenar el menú
    2 - Mostrar el menú
    3 - Hacer un pedido
    0 - Finalizar el programa
Tipos de menú:
    11 - Desayunos
    22 - Cenas
    33 - Almuerzos
Para hacer algo, ingrese el número correspondiente.
''')

question = input("¿Qué es lo que quieres hacer?: ")
while question != "0":
    if question == "1":
        question1 = int(input("¿Cuántos platos quieres agregar?: "))
        question2 = input("¿Qué menú quieres completar?: ")
        if question2 == "11":
            menu_entry(breakfast)
        if question2 == "22":
            menu_entry(dinner)
        if question2 == "33":
            menu_entry(lunch)
        question = input("¿Qué es lo que quieres hacer?: ")
    if question == "2":
        question3 = input("¿Qué menú quieres mostrar?: ")
        if question3 == "11":
            menu_output(breakfast)
        if question3 == "22":
            menu_output(dinner)
        if question3 == "33":
            menu_output(lunch)
        question = input("¿Qué es lo que quieres hacer?: ")
    if question == "3":
        question4 = int(input("¿Cuántos platos quieres agregar?: "))
        question5 = input("¿Qué menú? ")
        if question5 == "11":
            order_entry(breakfast)
        if question5 == "22":
            order_entry(dinner)
        if question5 == "33":
            order_entry(lunch)
        question = input("¿Qué es lo que quieres hacer?: ")