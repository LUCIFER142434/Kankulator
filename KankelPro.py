class Standart:
    def minus(self,a,b):
        return a - b
    def plus(self,a,b):
        return a + b
class Pro(Standart):
    def delit(self,a,b):
        return a / b
    def umn(self,a,b):
        return a * b

def inputi(num1,num2):
    try:
        num1 = int(input("Number1 : "))
        num2 = int(input("Number2 : "))
        return num1,num2
    except:
        print("Не тупи пиши целое число")
        inputi()

def kupi_pro():
    global kankul
    vibor = input("Купите про версию чтобы купить напишите Pro : ")
    if vibor == "Pro":
        kankul = Pro()
        recurs()
    else:
        kankul = Standart()
        print("Чего? вот тебе стандарт!")
        
def recurs():
    global kankul
    try:
        deystvie = input("Deystvie +, -, /, * : ")
        if deystvie in ["+","-","/","*"]:
            num1,num2 = inputi(int(),int())
            if num1 == int(num1) and num2 == int(num2):
                if deystvie == "+":
                    print(kankul.plus(num1,num2))
                elif deystvie == "-":
                    print(kankul.minus(num1,num2))
                elif deystvie == "*":
                    print(kankul.umn(num1,num2))
                elif deystvie == "/":
                    print(kankul.delit(num1,num2))
            elif num1 != int(num1) or num2 != int(num2):
                print("Не тупи пиши целые числа!")
        else:
            print("Нет такого действия")
            recurs()
    except:
        print("Ошибка если вы ввели / или * то купите про версию!")
        # if kankul in Pro():
        #     print('Hello')
        # else:
        #     kupi_pro()
        kupi_pro()
        recurs()

kupi_pro()