# Данные о товарах на складе хранятся в словаре
itemss = [
    {
        "name": "Кроссовки",
        "brand": "adidas",
        "price": 3440
    },
    {
        "name": "Кепка",
        "brand": "reebok",
        "price": 3500
    },
    {
        "name": "Рюкзак",
        "brand": "reebok",
        "price": 4800
    },
    {
        "name": "Шорты",
        "brand": "puma",
        "price": 2500
    },
    {
        "name": "Шорты",
        "brand": "adidas",
        "price": 2750
    },
    {
        "name": "Футболка",
        "brand": "puma",
        "price": 1700
    },
]
brands=[]
prices=0
prices_brend=""
for i in itemss:
    brands.append(i["brand"])
    if i["price"]>prices:
        prices=i["price"]
        prices_brend=i["brand"]
        


quantity_brand=0   # Ищем - На складе больше всего товаров брэнда(ов) 
name_brand=""
for k in set(brands):
    if brands.count(k) > quantity_brand:
        quantity_brand=brands.count(k)
        name_brand=k

print("Товары на складе представлены брэндами: ",set(brands) )
print("На складе больше всего товаров брэнда(ов): ",name_brand)
print("На складе самый дорогой товар брэнда(ов): ", prices_brend)

    
"""  
# Найдите:
print("Товары на складе представлены брэндами: ")

# TODO: your code here

print("На складе больше всего товаров брэнда(ов): ")

# TODO: your code here

print("На складе самый дорогой товар брэнда(ов): ")

# TODO: your code here
