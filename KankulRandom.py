# from random import randrange
# def rand():
#     num1 = randrange(1,10)
#     num2 = randrange(1,10)
#     deystvie = randrange(0,2)
#     otv = 0
#     if deystvie == 0:
#         deystvie = "-"
#         otv = num1 - num2
#     elif deystvie == 1:
#         deystvie = "+"
#         otv = num1 + num2
#     elif deystvie == 2:
#         deystvie = "/"
#         otv = num1 / num2
#     elif deystvie == 3:
#         deystvie = "*"
#         otv = num1 * num2
#     user_otv = int(input(f"{num1} {deystvie} {num2} = "))
#     if user_otv == otv:
#         print("Правильно!")
#     elif user_otv != otv:
#         print("Ты что совсем тупой?!")
#         rand()
# rand()