# Zadeklaruj klasę `Adder`
# * Klasa przyjmuje dwa argumenty `x` i `y` podczas
#   instancjonowania
# * Obiekt posiada metodę `calculate` zwracającą rezultat
#   dodawania argumentów podanych przy instancjonowaniu

class Adder():
  def __init__(self, x, y):
    self.x = x
    self.y = y
    
  def calculate(self):
    return self.x + self.y
