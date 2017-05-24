total = 0
def process_order(x_list):
    global total

    order = x_list.pop() #modifies the list. Even outside variables will be impacted
    print(order[1], order[0], "at $", order[2], "each")
    total += order[1]*order[2]




x = [("oranges", 4, 3.22),("gummy bears",1,1.99),("sour bites", 3, 2.33), ("antacid", 1, 5.33)]
while(len(x)>0):
    process_order(x)
print("total price: ", total)
