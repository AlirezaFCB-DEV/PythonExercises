class Dog :
  material = "German Shepherd"
  
  def __init__(self , name):
     self.name = name
     
aliDog = Dog("Wolf")
RezaDog = Dog("BigLion")

print(aliDog.material)
print(RezaDog.material)

print(aliDog.name)
print(RezaDog.name)