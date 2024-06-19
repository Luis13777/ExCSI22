from abc import ABC, abstractmethod
from enum import Enum

# Componente (Classe Base Abstrata)
class Pizza(ABC):
    @abstractmethod
    def get_cost(self):
        pass

    @abstractmethod
    def get_ingredients(self):
        pass

    @abstractmethod
    def get_name(self):
        pass


class PizzaType(Enum):
    SAVORY = "savory"
    SWEET = "sweet"

# ComponenteConcreto (Implementação da Classe Base)
class Base(Pizza):
    def __init__(self, pType, name):
        super().__init__()
        self._type = pType
        self._name = name
    
    def get_cost(self):
        return 50.0

    def get_ingredients(self):
        if self._type == PizzaType.SAVORY:
            return "Molho de Tomate"
        elif self._type == PizzaType.SWEET:
            return ""
    
    def get_name(self):
        return self._name

# Decorador (Classe Base)
class IngredientDecorator(Pizza):
    def __init__(self, pizza):
        self._decorated_pizza = pizza
    
    @abstractmethod
    def get_cost(self):
        pass

    @abstractmethod
    def get_ingredients(self):
        pass

    def get_name(self):
        return self._decorated_pizza.get_name()

# Decoradores Concretos
class Queijo(IngredientDecorator):
    def get_cost(self):
        return self._decorated_pizza.get_cost() + 10.0

    def get_ingredients(self):
        return self._decorated_pizza.get_ingredients() + ", Queijo"

class Calabresa(IngredientDecorator):
    def get_cost(self):
        return self._decorated_pizza.get_cost() + 5.0

    def get_ingredients(self):
        return self._decorated_pizza.get_ingredients() + ", Calabresa"

class Frango(IngredientDecorator):
    def get_cost(self):
        return self._decorated_pizza.get_cost() + 6.0

    def get_ingredients(self):
        return self._decorated_pizza.get_ingredients() + ", Frango"
    
class Presunto(IngredientDecorator):
    def get_cost(self):
        return self._decorated_pizza.get_cost() + 5.0

    def get_ingredients(self):
        return self._decorated_pizza.get_ingredients() + ", Presunto"
    
class Catupiry(IngredientDecorator):
    def get_cost(self):
        return self._decorated_pizza.get_cost() + 4.0

    def get_ingredients(self):
        return self._decorated_pizza.get_ingredients() + ", Catupiry"
    
class Ovo(IngredientDecorator):
    def get_cost(self):
        return self._decorated_pizza.get_cost() + 1.0

    def get_ingredients(self):
        return self._decorated_pizza.get_ingredients() + ", Ovo"

class Tomate(IngredientDecorator):
    def get_cost(self):
        return self._decorated_pizza.get_cost()

    def get_ingredients(self):
        return self._decorated_pizza.get_ingredients() + ", Tomate"

class Cebola(IngredientDecorator):
    def get_cost(self):
        return self._decorated_pizza.get_cost() 

    def get_ingredients(self):
        return self._decorated_pizza.get_ingredients() + ", Cebola"

class Manjericao(IngredientDecorator):
    def get_cost(self):
        return self._decorated_pizza.get_cost()

    def get_ingredients(self):
        return self._decorated_pizza.get_ingredients() + ", Manjericão"


class Chocolate(IngredientDecorator):
    def get_cost(self):
        return self._decorated_pizza.get_cost() + 10.0

    def get_ingredients(self):
        return self._decorated_pizza.get_ingredients() + "Chocolate ao Leite"

class Morango(IngredientDecorator):
    def get_cost(self):
        return self._decorated_pizza.get_cost() + 5.0

    def get_ingredients(self):
        return self._decorated_pizza.get_ingredients() + ", Morango"
          

# interação com o usuário

def select_pizza():
    menu = [
            Cebola(Calabresa(Base(PizzaType.SAVORY, "Calabresa"))),
            Manjericao(Tomate(Queijo(Base(PizzaType.SAVORY, "Marguerita")))),
            Frango(Queijo(Base(PizzaType.SAVORY, "Frango"))),
            Cebola(Ovo(Presunto(Queijo(Base(PizzaType.SAVORY, "Portuguesa"))))),
            Cebola(Ovo(Calabresa(Queijo(Base(PizzaType.SAVORY, "Baiana"))))),
            Catupiry(Frango(Queijo(Base(PizzaType.SAVORY, "Frango Especial")))),
            Chocolate(Base(PizzaType.SWEET, "Chocolate")),
            Morango(Chocolate(Base(PizzaType.SWEET, "Chocolate Especial"))),
            ]
    
    print("\nSelecione uma opção:")
    k = 1
    for pizza in menu:
        print(str(k) + ". " + pizza.get_name() + " (" + pizza.get_ingredients() + ") R$", round(pizza.get_cost(), 2))
        k += 1

    while True:
        try:
            option = int(input("Opção: "))

            if option >= 1 and option <= len(menu):
                name = menu[option - 1].get_name()
                cost = menu[option - 1].get_cost()
                return name, cost
            else:
                print("Opção não existe! Tente novamente.")

        except (ValueError, TypeError):
            print("Entrada inválida! Tente novamente.")


def main():
    print("--------------------------------------------------")
    print("Bem vindo(a) à Pizzaria em Python!")
    print("--------------------------------------------------")
    
    pizzaList = ''
    totalCost = 0.0

    while True:
        print("\nSelecione uma opção:")
        print("1. Adicionar Pizza")
        print("2. Finalizar pedido")
        print("3. Sair")   

        while True:
            try:
                option = int(input("Opção: "))

                if option == 1:
                    try:
                        name, cost = select_pizza()
                        pizzaList += name + ". "
                        totalCost += cost       
                    except Exception as error:
                        print(f'{error}')
                    break
                elif option == 2:
                    print("\nPedido finalizado!")
                    print("pizzas: ", pizzaList)
                    print("preço: R$", round(totalCost, 2))
                    return
                elif option == 3:
                    print("Saindo...")
                    return
                else:
                    print("Opção não existe! Tente novamente.")
                
            except (ValueError, TypeError):
                print("Entrada inválida! Tente novamente.")

        print("\npizzas adicionadas:", pizzaList)
        print("preço: R$", round(totalCost, 2))


if __name__ == "__main__":
    main()
