# Zadeklaruj klasę `Person`
# * Klasa przyjmuje dwa argumenty `name` i `surname` podczas
#   instancjonowania
# * Obiekt posiada dwa atrybuty `name` i `surname` odpowiadające
#   co do wartości parametrom przekazanym podczas instancjonowania

class Person():
  def __init__(self, name, surname):
    self.name = name
    self.surname = surname
