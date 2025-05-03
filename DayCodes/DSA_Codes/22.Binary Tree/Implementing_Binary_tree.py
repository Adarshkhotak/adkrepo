'''                drink        
            HOT             Cold
      Tea      Cofee    Cloa     Fanta   '''

class Node:

    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
    
drink =Node("drink")
hot =Node("hot")
cold =Node("cold")
tea =Node("tea")
cofee =Node("cofee")
cola =Node("cola")
fanta =Node("fanta")

hot.left=tea
hot.right=cofee

cold.left=cola
cold.right=fanta

drink.left=hot
drink.right=cold

print(drink.left.left.value)
print(cold.left.value)