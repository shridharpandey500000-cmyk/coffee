from coffee_material import resources
from coffee_material import MENU
from coffee_material import logo

def report(resourse_left):
    print("\n"*100)
    print("Available resources in the coffee machine are-")
    for content in resourse_left:
        a=content
        b=resourse_left[content]
        if content=="coffee powder":
            print(f"{a}={b}g")
        elif content=="balance":
            print(f"{a}=${b}")
        else:
            print(f"{a}={b}ml")
    statement=input("")
    if statement=="off":
        off()
    elif statement=="report":
        report(resources)
    print("\n"*100)
    machine_on()


def add(x,y,z):
    resources["water"]+=x
    resources["milk"]+=y
    resources["coffee powder"]+=z
    for content in resources:
        a=content
        b=resources[content]
        if content=="coffee powder":
            print(f"{a}={b}g")
        else:
            print(f"{a}={b}ml")

def off():
    print("\n"*100)
    print("⚙️ ")
    a=input("Do you want to fill resources in coffee machine?(y/n)")
    if a=="y":
        water=int(input("How much water do you want to add?="))
        milk=int(input("How much milk would you like to add?="))
        coffee=int(input("How much coffee would you like to add="))
        add(water,milk,coffee)
        statement=input("")
        if statement=="off":
            off()
        elif statement=="report":
            report(resources)
        print("\n"*100)
        machine_on()
    else:
        print("\n"*100)
        machine_on()

def money(x):
    low_money=True
    total_amount=0
    while low_money==True:
        a=int(input("\nHow much penny($0.01)="))
        b=int(input("How much Dime($0.1)="))
        c=int(input("How much Nickel($0.05)="))
        d=int(input("How much Quarter($0.25)="))
        total_amount+=(a*0.01+b*0.1+c*0.05+d*0.25)
        if total_amount<((MENU[str(x)]["cost"])*g):
            e=input("\nNot enough money- 'add more' or 'withdraw'\n")

            if e=="add more":
                low_money=True
            elif e=="withdraw":
                low_money=False
                print("Your money is refunded, Thank You")
                f=input("")
                if f=="":
                    machine_on()
        elif total_amount>=((MENU[x]["cost"])*g):
            if x=="espresso":
                resources["water"]=resources["water"]-MENU[x]["ingredients"]["water"]
                resources["coffee powder"]=resources["coffee powder"]-MENU[x]["ingredients"]["coffee powder"]
            else:
                resources["water"]=resources["water"]-MENU[x]["ingredients"]["water"]
                resources["milk"]=resources["milk"]-MENU[x]["ingredients"]["milk"]
                resources["coffee powder"]=resources["coffee powder"]-MENU[x]["ingredients"]["coffee powder"]

            low_money=False
            change=total_amount-((MENU[x]["cost"])*g)
            resources["balance"]+=((MENU[x]["cost"])*g)
            print(f"\nYour total is ${((MENU[x]["cost"])*g)}\nHere is your {g} {x} ☕\nYour change=${change}\nThank You, Enjoy your coffee!!!")
            statement=input("")
            if statement=="off":
                off()
            elif statement=="report":
                report(resources)
            else:
                print("\n"*100)
                machine_on()



def machine_on():
    print(logo)
    print("Welcome to our coffee machine!!!!!🤖")
    statement=input("")
    if statement=="off":
         off()
    elif statement=="report":
         report(resources)
    a=input("What would you like to have-\nespresso=$1.5\nlatte=$2.5\ncappuccino=$3.0\n")
    global g
    g=int(input("How much do you want?="))
    
    if a=="espresso":
        if resources["water"]<(50*g) or resources["milk"]<(0*g) or resources["coffee powder"]<(18*g):
            print("Not enough resources!")
            statement=input("")
            if statement=="off":
                off()
            elif statement=="report":
                report(resources)   
            else:
                print("\n"*100)
                machine_on()

        else:
            money(a)
    elif a=="latte":
        if resources["water"]<(200*g) or resources["milk"]<(150*g) or resources["coffee powder"]<(24*g):
            print("Not enough resources!")
            statement=input("")
            if statement=="off":
                off()
            elif statement=="report":
                report(resources)
            else:
                print("\n"*100)
                machine_on()
        else:
            money(a)
    elif a=="cappuccino":
        if resources["water"]<(250*g) or resources["milk"]<(100*g) or resources["coffee powder"]<(24*g):
            print("Not enough resources!")
            statement=input("")
            if statement=="off":
                off()
            elif statement=="report":
                report(resources)
            else:
                print("\n"*100)
                machine_on()
        else:
            money(a)        


machine_on()