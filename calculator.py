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

  while True:
    opcion = menu_calculadora()
    Numero1 = float(input('Introduce numero: '))
    Numero2 = float(input('Introduce numero: '))

    if opcion == '1':
      print("Calculadora de Suma")
      resultado = Sumar(Numero1, Numero2)
    elif opcion == '2':
      print("Calculadora de Resta")
      resultado = Restar(Numero1, Numero2)
    elif opcion == '3':
      print("Calculadora de Dividir")
      resultado = Dividir(Numero1, Numero2)
    elif opcion == '4':
      print("Calculadora de Multiplicar")
      resultado = Multiplicar(Numero1, Numero2)
    elif opcion == '5':
      print("Calculadora de Potenciacion")
      resultado = Potenciacion(Numero1, Numero2)

    print("Resultado: ", resultado)

    N1 = resultado

    seguir = input('Seguir operando? si/no')
    if seguir == "no":
      break




