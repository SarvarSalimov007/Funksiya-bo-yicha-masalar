######1-MODUL######
##1-masala
# def hisobla(x):
#     return f"Sonning kvadrati: {x*x}"
# x = int(input("Sonni kiriting: "))
#
# print(hisobla(x))
##2-masala
# def takrorla(matn,son):
#     return f"{matn*son}"
# matn = input("Matnni kiriting: ").lower()
# son = int(input("Takrorlash sonini kiring: "))
# print(takrorla(matn,son))
##3-masala
# def aniqla(son):
#     if son % 2 == 0:
#         print('Juft!')
#     else:
#          print('Toq!')
# son = int(input('Sonni kiriting: '))
# print(aniqla(son))
##4-masala
# def hisobla(x,y):
#     return f"Yig;indi {x+y}"
# x = int(input("x sonni kiriting: "))
# y = int(input("y sonni kiriting: "))
# print(hisobla(x,y))
##5-masala
# def uzunlik(matn):
#     hisob = 0
#     for harf in matn:
#         hisob += 1
#     return f"Uzunlik: {hisob}"
# matn = input("Matnni kiritin: ")
# print(uzunlik(matn))
##6-masala
# def aniqla(son):
#     if son < 0:
#         print('Manfiy!')
#     elif son > 0:
#         print("Musbat!")
#     elif son == 0:
#         print("Nol!")
#     else:
#         print("XATOLIK")
#         return f"XATOLIK!"
# son = int(input("Sonni kiriting: "))
# print(aniqla(son))
##7-masala
# def modul(son):
#     if son < 0:
#         print(-son)
#     else:
#         return son
# son = int(input("Sonni kiriting: "))
# print(modul(son))
##8-masala
# def teskari(matn):
#     return f"Teskari qildim: {matn[::-1]}"
# matn = input("Matinni kiriting: ")
# print(teskari(matn))
######2-MODUL######
##1-masala
# def faktorial(son):
#     if son == 0 or son == 1:
#         return 1
#     return son * faktorial(son - 1)
# print(faktorial(5))
##2-masala
# def juftson(sonlar):
#     yigindi = 0
#     for son in sonlar:
#         if son % 2 == 0:
#             yigindi += son
#     return yigindi
# sonlar = [1,2,3,4,5,6]
# print(juftson(sonlar))
##3-masala
# def unlilar_soni(matn):
#     unlilarni_sanash = 0
#     unlilar = 'aeiouAEIOU'
#     for harf in matn:
#         if harf in unlilar:
#             unlilarni_sanash += 1
#     return f"Unlilar soni: {unlilarni_sanash}ta"
# matn = input('Matinni kiriting: ').lower()
# print(unlilar_soni(matn))
##4-masala
# def daraja(x,y):
#     return f"Sonning darajasi: {x ** y}"
# x = int(input("X - sonni kiriting: "))
# y = int(input("Y - sonni kiriting: "))
# print(daraja(x,y))
##5-masala
# x = [4,2,9,1]
# def katta_son(x):
#     for y in x:
#         return max(x)
# print(katta_son(x))



