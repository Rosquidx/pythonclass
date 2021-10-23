# print (type("Hello"))
# print (type(4))

# #definir una función
# #  -> bool significa que retorna un falso o verdadero pero no hay necesidad de ponerlo
# # pero por buenas practicas.
# def impar(n: int) -> bool:
#     return n % 2 != 0
# # print(impar(4))
# # print(impar(8))
# # print(impar(1))
# # print(impar(6))

# def main():
#     print(impar("hol"))

#SELF: Variable de la instancia, se convirte en el objeto que esten llamando a resetear.

import math
from mostrar import App
class Punto:
    def __init__(self, x:float = 0, y: float = 0) -> None:
        self.x = x
        self.y = y

    def resetear(self):
        self.x = 0.0
        self.y = 0.0

    def moverse(self, x:float, y:float) -> None:
        self.x = x
        self.y = y

    def distancia(self, punto : "Punto") -> float:
        return math.hypot(self.x - punto.x, self.y - punto.y)


p1 = Punto(10, 56)

app = App()
app.print(f"Los resultado del p1 son: x: {p1.x}, y: {p1.y}. \n \n \nLa hipotenusa es el lado de un triángulo rectángulo que se encuentra al \nfrente del ángulo recto o de 90º. ... La hipotenusa es entonces el lado de \nun triángulo rectángulo que tiene mayor medida  \nque los otros dos lados, a los que se le denomina catetos. \n \n                      ¡ESTAMOS CERCA DE LOGRARLO!!")


'''
# p1.x la X es un atributo de ese objeto.
p1.x = 5.3
p1.y = 10.2

p2.x = 2
p2.y = 56.2

print (p1.x, " + ", p1.y)
print (p2.x, " + ", p2.y)

p1.resetear()
p2.moverse(8.9,2.4)
p1.moverse(2.5,6.9)
# print("Distancia: ",{d})

print (p1.x, " + ", p1.y)
print (p2.x, " + ", p2.y)

p3 = Punto()
p3.resetear()

print (p3)

# asssert sirve para hacer pruebas funciona como un IF.
assert p1.distancia(p2) == p2.distancia(p1)
d = p1.distancia(p2)
d = p1.distancia(p1)
print("Distancia: ",{d})
'''