"""""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        print(f"Hola, mi nombre es {self.name} y tengo {self.age} años")

person1 = Person("Ana", 30)
person2 = Person("Luis", 25)

person1.greet()
person2.greet()


print("----------------------------------------------")
"""
class BankAccount:
    def __init__(self, account_holder, balance ):
        self.account_holder = account_holder
        self.balance = balance
        self.is_active = True
        
        def deposit(self, amount):
            if self.is_active:
                self.balance += amount
                print(f"se ha depositado{amount}.")
            else:
                print("No se puede depositar, cuenta incativa")
        def withdraw(self, amount):
            if self.active <= self.balance:
                self.balance -= amount
                print(f"Se ha retirado {amount}. Saldo actual {self.balance}")
                
        def deactivate_account(self):
            self.is_active = False
            print(f"La cuenta ha sido desactivada")

        def activate_account(self):
            self.is_active = True
            print(f"La cuenta ha sido activada")
account1 = BankAccount("Ana", 700)
account2 = BankAccount("Poi",1000)
account1.deactivate_account()
account1.deposit(50)