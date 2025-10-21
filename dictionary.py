items = [
{
    "name": "apple",
    "price": 0.99,
    "department": "fruits"},
{
    "name": "strawberry",
    "price": 4.99,
    "department": "fruits"},
{
    "name": "banana",
    "price": 0.50,
    "department": "fruits"},
{
    "name": "cat",
    "price": 670,
    "department": "pet"},
{
    "name": "dog",
    "price": 500,
    "department": "pet"},
{
    "name": "airpod",
    "price": 129,
    "department": "technology"},
{
    "name": "iphone17-pro-max",
    "price": 1670,
    "department": "technology"}

                                                                                                                                                                                                                                                                                                                                                                 
]



cart = []
total = 0
for index, item in enumerate(items):
    print(index, ":", item["name"])
while True:
    x= input("what do you want?")
    item_in_stock = False
    for item in items:
        if item["name"] ==x:
                item_in_stock = True
                cart.append(x)
                print(cart)
                total += item["price"]
                
                   
            
    y = input("Do you need anything else? (y/n) ")
    if y.lower() != 'y':
            print(f"your total is {total} and here is your cart {cart}")
            break

