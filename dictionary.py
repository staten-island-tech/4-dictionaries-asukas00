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
for index, item in enumerate(items):
    print(index, ":", item["name"])
x= input("what do you want?")
for item in items:
    if item["name"] ==x:
        print(item["name"])
        cart.append(x)
        print(cart)
y= input("do you need anything else? y/n")
if ('y') == y:
    print("what else")
else:
    print(f"here is your total {item["price"]}")
