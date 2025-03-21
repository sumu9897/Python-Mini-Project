item1="bread"
item2="pasta"
item3="fruits"

items=["bread","pasta","fruits","veggies"]
print(items)

print(items[0])

print(items[2])
items[0] = 'chips'
print(items)
print(items[-1])

items.append("butter")
print(items)
items.insert(1,"chiken")
print(items)

food=["bread","pasta","fruits"]
bathroom = ["shampoo", "soap"]

items=food + bathroom
print(items)

print('Items Length : ',len(items))

statement= "bread" in items
print(statement)