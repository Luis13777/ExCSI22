from abc import ABC, abstractmethod

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

    @abstractmethod
    def get_type(self):
        pass

# ComponenteConcreto (Implementação da Classe Base)
class Base(Pizza):
    def __init__(self, pType, name):
        super().__init__()
        self._type = pType
        self._name = name
    
    def get_cost(self):
        return 45.0

    def get_ingredients(self):
        if self._type == "salgada":
            return "Molho de Tomate"
        else:
            return ""
    
    def get_name(self):
        return self._name

    def get_type(self):
        return self._type

# Decorador (Classe Base)
class ingredientDecorator(Pizza):
    def __init__(self, pizza):
        self._decorated_pizza = pizza

    def get_cost(self):
        return self._decorated_pizza.get_cost()

    def get_ingredients(self):
        return self._decorated_pizza.get_ingredients()
    
    def get_name(self):
        return self._decorated_pizza.get_name()

    def get_type(self):
        return self._decorated_pizza.get_type()

# Decoradores Concretos
class Queijo(ingredientDecorator):
    def get_cost(self):
        return self._decorated_pizza.get_cost() + 4.0

    def get_ingredients(self):
        return self._decorated_pizza.get_ingredients() + ", Queijo"

class Calabresa(ingredientDecorator):
    def get_cost(self):
        return self._decorated_pizza.get_cost() + 5.0

    def get_ingredients(self):
        return self._decorated_pizza.get_ingredients() + ", Calabresa"

class Frango(ingredientDecorator):
    def get_cost(self):
        return self._decorated_pizza.get_cost() + 5.0

    def get_ingredients(self):
        return self._decorated_pizza.get_ingredients() + ", Frango"
    
class Presunto(ingredientDecorator):
    def get_cost(self):
        return self._decorated_pizza.get_cost() + 3.0

    def get_ingredients(self):
        return self._decorated_pizza.get_ingredients() + ", Presunto"
    
class Catupiry(ingredientDecorator):
    def get_cost(self):
        return self._decorated_pizza.get_cost() + 2.0

    def get_ingredients(self):
        return self._decorated_pizza.get_ingredients() + ", Catupiry"
    
class Ovo(ingredientDecorator):
    def get_cost(self):
        return self._decorated_pizza.get_cost() + 1.0

    def get_ingredients(self):
        return self._decorated_pizza.get_ingredients() + ", Ovo"

class Tomate(ingredientDecorator):
    def get_cost(self):
        return self._decorated_pizza.get_cost()

    def get_ingredients(self):
        return self._decorated_pizza.get_ingredients() + ", Tomate"

class Cebola(ingredientDecorator):
    def get_cost(self):
        return self._decorated_pizza.get_cost() 

    def get_ingredients(self):
        return self._decorated_pizza.get_ingredients() + ", Cebola"

class Manjericao(ingredientDecorator):
    def get_cost(self):
        return self._decorated_pizza.get_cost()

    def get_ingredients(self):
        return self._decorated_pizza.get_ingredients() + ", Manjericão"
    
class Azeitona(ingredientDecorator):
    def get_cost(self):
        return self._decorated_pizza.get_cost()

    def get_ingredients(self):
        return self._decorated_pizza.get_ingredients() + ", Azeitona"

class Chocolate(ingredientDecorator):
    def get_cost(self):
        return self._decorated_pizza.get_cost() + 4.0

    def get_ingredients(self):
        return self._decorated_pizza.get_ingredients() + "Chocolate ao Leite"

class Morango(ingredientDecorator):
    def get_cost(self):
        return self._decorated_pizza.get_cost() + 3.0

    def get_ingredients(self):
        return self._decorated_pizza.get_ingredients() + ", Morango"

class MM(ingredientDecorator):
    def get_cost(self):
        return self._decorated_pizza.get_cost() + 1.0

    def get_ingredients(self):
        return self._decorated_pizza.get_ingredients() + ", MM"
          

# interação com o usuário

def select_pizza():
    pizzas = [Azeitona(Manjericao(Tomate(Queijo(Base("salgada", "Marguerita"))))),
              Azeitona(Cebola(Calabresa(Base("salgada", "Calabresa")))),
              Azeitona(Catupiry(Frango(Queijo(Base("salgada", "Frango"))))),
              Azeitona(Cebola(Ovo(Presunto(Queijo(Base("salgada", "Portuguesa")))))),
              Morango(Chocolate(Base("doce", "Chocolate com Morango"))),
              MM(Chocolate(Base("doce", "Chocolate com MM")))
              ]
    
    print("\nSelecione uma opção:")
    k = 1
    for pizza in pizzas:
        print(str(k) + ". " + pizza.get_name() + " (" + pizza.get_ingredients() + ") R$ " + str(pizza.get_cost()))
        k += 1

    while True:
        try:
            option = int(input("Opção: "))

            if option >= 1 and option <= len(pizzas):
                name = pizzas[option - 1].get_name()
                cost = pizzas[option - 1].get_cost()
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
        print("\npizzas adicionadas: ", pizzaList)
        print("preço: R$ ", totalCost)
      
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
                    print("preço: R$", totalCost)
                    return
                elif option == 3:
                    print("Saindo...")
                    return
                else:
                    print("Opção não existe! Tente novamente.")
                
            except (ValueError, TypeError):
                print("Entrada inválida! Tente novamente.")



if __name__ == "__main__":
    main()
