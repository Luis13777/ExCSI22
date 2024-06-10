from abc import ABC, abstractmethod

# Componente (Classe Base Abstrata)
class Pizza(ABC):
    @abstractmethod
    def get_custo(self):
        pass

    @abstractmethod
    def get_descricao(self):
        pass

# ComponenteConcreto (Implementação da Classe Base)
class Massa(Pizza):
    def get_custo(self):
        return 10.0

    def get_descricao(self):
        return "Massa da Pizza"

# Decorador (Classe Base)
class IngredienteDecorator(Pizza):
    def __init__(self, pizza):
        self._decorated_pizza = pizza

    def get_custo(self):
        return self._decorated_pizza.get_custo()

    def get_descricao(self):
        return self._decorated_pizza.get_descricao()

# Decoradores Concretos
class QueijoDecorator(IngredienteDecorator):
    def get_custo(self):
        return self._decorated_pizza.get_custo() + 2.0

    def get_descricao(self):
        return self._decorated_pizza.get_descricao() + ", Queijo"

class CalabresaDecorator(IngredienteDecorator):
    def get_custo(self):
        return self._decorated_pizza.get_custo() + 3.0

    def get_descricao(self):
        return self._decorated_pizza.get_descricao() + ", Calabresa"

class FrangoDecorator(IngredienteDecorator):
    def get_custo(self):
        return self._decorated_pizza.get_custo() + 4.0

    def get_descricao(self):
        return self._decorated_pizza.get_descricao() + ", Frango"

class TomateDecorator(IngredienteDecorator):
    def get_custo(self):
        return self._decorated_pizza.get_custo() + 1.0

    def get_descricao(self):
        return self._decorated_pizza.get_descricao() + ", Tomate"

class CebolaDecorator(IngredienteDecorator):
    def get_custo(self):
        return self._decorated_pizza.get_custo() + 0.5

    def get_descricao(self):
        return self._decorated_pizza.get_descricao() + ", Cebola"

class AzeitonaDecorator(IngredienteDecorator):
    def get_custo(self):
        return self._decorated_pizza.get_custo() + 1.5

    def get_descricao(self):
        return self._decorated_pizza.get_descricao() + ", Azeitona"

# Interface de Terminal
def main():
    pizza = Massa()
    print("--------------------------------------------------")
    print("Bem vindo a Pizzaria em Python!")
    print("--------------------------------------------------")

    while True:
        print("\nPizza atual: ", pizza.get_descricao())
        print("Custo atual: R$", pizza.get_custo())
        print("\nEscolha uma opção:")
        print("1. Adicionar Queijo (R$ 2.0)")
        print("2. Adicionar Calabresa (R$ 3.0)")
        print("3. Adicionar Frango (R$ 4.0)")
        print("4. Adicionar Tomate (R$ 1.0)")
        print("5. Adicionar Cebola (R$ 0.5)")
        print("6. Adicionar Azeitona (R$ 1.5)")
        print("7. Finalizar pedido")
        print("8. Sair")
        
        opcao = input("Opção: ")
        
        if opcao == "1":
            pizza = QueijoDecorator(pizza)
        elif opcao == "2":
            pizza = CalabresaDecorator(pizza)
        elif opcao == "3":
            pizza = FrangoDecorator(pizza)
        elif opcao == "4":
            pizza = TomateDecorator(pizza)
        elif opcao == "5":
            pizza = CebolaDecorator(pizza)
        elif opcao == "6":
            pizza = AzeitonaDecorator(pizza)
        elif opcao == "7":
            print("\nPedido finalizado!")
            print("Pizza: ", pizza.get_descricao())
            print("Custo total: R$", pizza.get_custo())
            break
        elif opcao == "8":
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
