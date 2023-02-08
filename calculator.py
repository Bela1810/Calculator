from abc import ABC
class Operaciones(ABC):

def Sumar(self, Num1, Num2):
    return Num1 + Num2

def Multiplicar(self, Num1, Num2):
    return Num1 * Num2

class Menu_Calculadora(Operaciones):
  def menu_calculadora():
    print("1. Sumar")
    print("2. Restar")
    print("3. Dividir")
    print("4. Multiplicar")
    print("5. Potenciacion")
    opcion = input("Elige opcion:  ")
    return opcion







