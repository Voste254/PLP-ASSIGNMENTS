class automobile:
  def __init__(self,color,wheels):
    self.color=color
    self.wheels=wheels
    

    
#implementing inheritance
class cars(automobile):
    def move(self): #method
     return "swish"

class aeroplanes(automobile):
  def move(self):
    return "Flyyyyyy awaaaaaaay"

#objects
ferrari=cars("black",4)
tricycle=cars("gray",3)
boeing=aeroplanes("white",6)

print(ferrari.move())
print(boeing.move())