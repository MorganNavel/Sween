def total_price(price_1:int,price_2:int)->str:
    return f"Your total bill is USD {price_1+price_2}"
        

price=total_price(30,40)
print(price)


new_price: list[int] = [14,902,898]
new_immutable_price: tuple[int,int,int] = (388,392,299)
new_price_dict: dict[str,int] = {
    "item_1":240,
    "item_2":490,
}

from typing import List,Union

x: List[int|float] = [2,3,4.1,5,6.2]  #newer syntax in python 3.10+
dic: dict[str,int|str] = {"0":0,"1":1,"2":"tell"}
print(x)
print(dic)


def eur_to_won(val:float)->Union[float,None]:
    try:
        fact = 1419.95
        return val*fact
    except TypeError:
        return None
print(eur_to_won(15))

Image = List[List[int]]
def image_processing(img:Image,val:int)->int:
    sum=0
    for l in img:
        for c in l:
            if c==val:
                sum+=1
    return sum
img:List[List[int]] = [[0,15,252],[1,85,66],[66,55,78]]

print(image_processing(img,66))

from typing import Callable
def smart_divide(func:Callable[[int,int],float]):#func = la fonction qui était censé être appelé
    def inner(a,b): #appelle cette fonction
        if b == 0:
            print("Whoops! Division by 0")
            return None

        return func(a, b) #si pa de division par 0 renvoie le retour de func
    return inner #retourne le résultat de inner


@smart_divide #appelle la fonction smart_divide avant l'appelle de divide
def divide(a, b):
    print(a/b)

divide(9, 0)
#Generators
price = [210,300,400,500]

price_iter = price.__iter__()

print(price_iter.__next__())
print(price_iter.__next__())
print(price_iter.__next__())
    
    