import ast
lst1 = []
with open("expenses.txt","r") as f:
    val = f.readline()
    val2 = f.readline()
    if val.strip() and val2.strip() :
        lst1 = ast.literal_eval(val)
    else:
        lst1 = []
    print(lst1)
    print(val2)

#catergory and price addition
def add_expense(in1,in2,in4):
    for val in lst1 :
        if in2 in val["Category"]:
            val["price"] += in1
            val["amount"] += in4
            break
    else:
        dit = {}
        dit["Category"] = in2
        dit["amount"] = in4
        dit["price"] = in1
        lst1.append(dit)
#total expense
def show_total_expense(lst,tot):
    for data in lst:
        tot = tot + data["price"]*data["amount"]
    return tot

#expenses addition system
input0 = input("Do you want to add expenses?(Y/N)")
answer = input0.lower()
while answer == "y" :
    input1 = int(input("How much expenses?"))
    input2 = input("What is the category of expense?")
    input4 = int(input("What is the amount of product you consumed?"))
    add_expense(input1,input2,input4)
    input0 = input("Do you want to add expenses?(Y/N)")
    answer = input0.lower()

#data transfer system
with open("expenses.txt","w") as f:
    lst = str(lst1)
    f.write(lst + "\n")
    ans = show_total_expense(lst1,0)
    ans1 = str(ans)
    f.write("THE TOTAL EXPENSE IS" +" "+ans1)
with open("show_output.txt","w") as f:
    f.write("Personal expense tracker\n")
    f.write(f"{"Category":^15}{"Price":^10}{"Amount":^10}\n")
with open("expenses.txt","r") as f:
    val = f.readline()
    val1 = f.readline()
    lst2 = ast.literal_eval(val)
    for data in lst2:
        cat = data["Category"]
        price = data["price"]
        amt = data["amount"]
        with open("show_output.txt","+a") as f:
            f.write(f"{cat:^15}{price:^10}{amt:^10}"+"\n")
    with open("show_output.txt","+a") as f:
        f.write("THE TOTAL EXPENSE IS" +" "+ans1)