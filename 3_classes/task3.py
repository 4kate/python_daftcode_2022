# Zadeklaruj klasę `Point`
# * Klasa przyjmuje dwa argumenty `x` i `y` podczas
#   instancjonowania
# * Obiekt posiada dwa atrybuty `x` i `y` odpowiadające
#   co do wartości parametrom przekazanym podczas instancjonowania
# * W kodzie nie można użyć identyfikatora `self`

class Point():
  def __init__(cls, x, y):
    Point.x = x
    Point.y = y
