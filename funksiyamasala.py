# ######1-MODUL######
# ##1-masala
# def hisobla(x):
#     return f"Sonning kvadrati: {x*x}"
# x = int(input("Sonni kiriting: "))

# print(hisobla(x))
# ##2-masala
# def takrorla(matn,son):
#     return f"{matn*son}"
# matn = input("Matnni kiriting: ").lower()
# son = int(input("Takrorlash sonini kiring: "))
# print(takrorla(matn,son))
# ##3-masala
# def aniqla(son):
#     if son % 2 == 0:
#         print('Juft!')
#     else:
#         print('Toq!')
# son = int(input('Sonni kiriting: '))
# print(aniqla(son))
# ##4-masala
# def hisobla(x,y):
#     return f"Yig;indi {x+y}"
# x = int(input("x sonni kiriting: "))
# y = int(input("y sonni kiriting: "))
# print(hisobla(x,y))
# ##5-masala
# def uzunlik(matn):
#     hisob = 0
#     for harf in matn:
#         hisob += 1
#     return f"Uzunlik: {hisob}"
# matn = input("Matnni kiritin: ")
# print(uzunlik(matn))
# ##6-masala
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
# ##7-masala
# def modul(son):
#     if son < 0:
#         print(-son)
#     else:
#         return son
# son = int(input("Sonni kiriting: "))
# print(modul(son))
# ##8-masala
# def teskari(matn):
#     return f"Teskari qildim: {matn[::-1]}"
# matn = input("Matinni kiriting: ")
# print(teskari(matn))
# ######2-MODUL######
# ##1-masala
# def faktorial(son):
#     if son == 0 or son == 1:
#         return 1
#     return son * faktorial(son - 1)
# print(faktorial(5))
# ##2-masala
# def juftson(sonlar):
#     yigindi = 0
#     for son in sonlar:
#         if son % 2 == 0:
#             yigindi += son
#     return yigindi
# sonlar = [1,2,3,4,5,6]
# print(juftson(sonlar))
# ##3-masala
# def unlilar_soni(matn):
#     unlilarni_sanash = 0
#     unlilar = 'aeiouAEIOU'
#     for harf in matn:
#         if harf in unlilar:
#             unlilarni_sanash += 1
#     return f"Unlilar soni: {unlilarni_sanash}ta"
# matn = input('Matinni kiriting: ').lower()
# print(unlilar_soni(matn))
# ##4-masala
# def daraja(x,y):
#     return f"Sonning darajasi: {x ** y}"
# x = int(input("X - sonni kiriting: "))
# y = int(input("Y - sonni kiriting: "))
# print(daraja(x,y))
# ##5-masala
# x = [4,2,9,1]
# def katta_son(x):
#     for y in x:
#         return max(x)
# print(katta_son(x))
# ####################################################################
# ####################################################################
# ####################################################################
# ##1-masala
# yil = int(input("Yil kabisa yilimi topamiz: "))
# if yil % 4 == 0 and yil % 100 != 0 or yil % 400 == 0:
#     print("Yil kabisa yili!")
# else:
#     print("Yil kabisa yili emas!")
# ##2-masala
# jihozlar = int(input("Jihozlar sonini kiriting: "))
# vaqt = int(input("Ishlatilgan vaqtini kiriting: "))
# if jihozlar < 5 and vaqt < 8:
#     print("Tejamkor!")
# elif jihozlar < 5 and vaqt >= 8:
#     print("O'rtacha istemol!")
# elif jihozlar >= 5 and vaqt < 8:
#     print("Ko'p istemol!")
# elif jihozlar >= 5 and vaqt >= 8:
#     print("Haddan tashqari istemol!")
# else:
#     print("XATOLIK!")
# ##3-masala
# gradus = int(input("Haroratni kiriting: "))
# if gradus >= 60:
#     print("Ogoh bo'ling juda issiq!")
# elif 30 < gradus < 60:
#     print("Ideal!")
# elif 0 < gradus < 30:
#     print("Sovib qolgan!")
# elif gradus < 0:
#     print("Izdevatsiya qilyapsizmi?")
# else:
#     print("Ichib o'tirmang!")
# ##4-masala
# foiz = int(input("Telefon quvvatini kiriting: "))
# if 0 < foiz <= 10:
#     print("Zaryadlash zarur!")
# elif 10 < foiz <= 50:
#     print("Yana biroz ishlatish mumkin!")
# elif 50 < foiz <= 100:
#     print("Zaryad yetali!")
# else:
#     print("ERROR!!!")
# ##5-masala
# kod = int(input("Telefon raqamingizni bosh kodini kiriting: "))
# if kod == +99890 or kod == +99891 or kod == +99820:
#     print("Beeline")
# elif kod == +99893 or kod == +99894 or kod == +99850:
#     print("Ucell")
# elif kod == +99888 or kod == +99897 or kod == +99887:
#     print("Mobiuz")
# elif kod == +99899 or kod == +99877:
#     print("Uzmobile")
# elif kod == +99833 or kod == +99855:
#     print("Humans")
# elif kod == +99898:
#     print("Perfectum")
# else:
#     print("Noma’lum operator")
# ##6-masala
# email = input("Emailni kiriting: ")
# if "@" in email and "." in email:
#     print("Email to'g'ri!")
# else:
#     print("Email noto'g'ri!")
# ##7-masala
# ball = int(input("Ballni kiriting: "))
# if ball < 56: 
#     print("Qoniqarsiz!")
# elif 56 <= ball < 70:
#     print("Qoniqarli!")
# elif 71 <= ball < 85:
#     print("Yaxshi!")
# elif 85 <= ball < 100:
#     print("A'lo!")
# else:
#     print("Error!")
# ##8-masala
# yosh = int(input("Yoshingizni kiriting: "))
# if yosh < 7:
#     print("Kirish bepul!")
# elif 7 <= yosh < 18:
#     print("Kirish 5000 so'm!")
# elif 18 <= yosh < 59:
#     print("Kirish 10000 so'm!")
# elif yosh <= 59:
#     print("Kirish 7000 so'm!")
# else:
#     print("Ko'zimga ko'rimang!!")
# ##9-masala
# matn = input("Matnni kiriting: ")
# if matn == ' ':
#     print("False!")
# else:
#     print("True!")
# ##10-masala
# karta_raqmi = int(input("Karta raqmingizni kiriting: "))
# if karta_raqmi.len(karta_raqmi) == 16:
#     print("Karta raqmi to'g'ri!")
# else:
#     print("Karta raqmi noto'g'ri!")
# ##11-masala
# narx = int(input("Narxi kiriting: "))
# if narx < 50000:
#     print("Chegirma yo'q!")
# elif 50000 <= narx < 100000:
#     print("Chegirma 5%!")
# elif 100000 <= narx < 200000:
#     print("Chegirma 10%!")
# elif narx >= 200000:
#     print("Chegirma 15%!")
# else:
#     print("Error!")
# ##12-masala
# masofa = int(input("Masofani kiriting: "))
# if 0 < masofa <= 5:
#     print("7000 so'm!")
# elif 6 < masofa < 15:
#     print(f"{7000 + 1000 } so'm!")
# elif masofa >= 15:
#     print(f"{7000 + 1000 * 10 + 2000 * (masofa - 15)} so'm!")
# else:
#     print("Error!")   
# ##13-masala
# togrijavoblar = 0
# javob = input("Javob to'g'rimi? (ha/yoq): ")
# if javob == 'ha':
#     print(f"Qo'shildi: {togrijavoblar + 2}")
# elif javob == 'yoq':
#     print(f"Ayrildi: {togrijavoblar - 1}")
# else:
#     print(f"Baholanmadi: {togrijavoblar + 0}")
# ##14-masala
# soat = float(input("Soatni kiriting: "))
# if soat >= 9.00 and soat <= 18.00:
#     print("Ishlash vaqti!")
# elif soat > 18.01 and soat < 23.59:
#     print("Dam olish vaqti!")
# elif soat == 0.00 and soat < 8.59:
#     print("Uyqu vaqti!")
# else:
#     print("XATOLIK!")
# ##15-masala
# tajriba = int(input("Tajriba yilini kiriting: "))
# loyiha = int(input("Loyihalar soni: "))
# if tajriba < 3:
#     print("Boshlovchi")
# elif 3 <= tajriba <= 5:
#     print("O‘rta daraja")
# elif tajriba > 5 and loyiha >= 1:
#     print("Tajribalilar")
# else:
#     print("Tajriba yetarli emas")
# ##16-masala
# temp = float(input("Harorat: "))
# if temp < 36:
#     print("Past harorat")
# elif 36 <= temp <= 37:
#     print("Normal")
# elif 37 < temp <= 38:
#     print("Yengil isitma")
# else:
#     print("Yuqumli kasallik ehtimoli bor")
# ##17-masala
# taom = input("Taom: ")
# ichimlik = input("Ichimlik: ")
# if taom == "lavash" and ichimlik == "cola":
#     print("Combo: chegirma!")
# elif taom == "lavash" or ichimlik == "cola":
#     print("Yaxshi tanlov!")
# else:
#     print("Oddiy buyurtma.")
# ##18-masala
# kod = input("Karta kodini kiriting: ")
# if kod == "8600":
#     print("UzCard")
# elif kod == "9860":
#     print("Humo")
# elif kod == "4000":
#     print("Visa")
# else:
#     print("Noma’lum karta")
# ##19-masala
# yosh = int(input("Yoshingiz: "))
# if yosh < 6:
#     print("Go‘dak")
# elif yosh <= 12:
#     print("Bola")
# elif yosh <= 17:
#     print("O‘smir")
# elif yosh <= 25:
#     print("Yosh")
# elif yosh <= 59:
#     print("Katta yoshli")
# else:
#     print("Qariya")
# ##20-masala
# oy = int(input("Necha oylik depozit: "))
# if oy == 3:
#     print("5%")
# elif oy == 6:
#     print("10%")
# elif oy == 12:
#     print("20%")
# else:
#     print("Noto‘g‘ri tanlov")
# ##21-masala
# w = float(input("Vazn: "))
# if w < 1:
#     print(5000)
# elif w <= 3:
#     print(8000)
# elif w <= 5:
#     print(12000)
# else:
#     print(20000)
# ##22-masala
# yosh = int(input("Yosh: "))
# talaba = input("Talaba (ha/yo'q): ")
# if yosh < 7:
#     print("Bepul")
# elif yosh < 18:
#     print(10000)
# elif talaba == "ha":
#     print(12000)
# else:
#     print(15000)
# ##23-masala
# f1 = int(input("Fan1: "))
# f2 = int(input("Fan2: "))
# f3 = int(input("Fan3: "))
# marks = [f1, f2, f3]
# if marks.count(5) == 3:
#     print("1 000 000 so‘m")
# elif marks.count(4) == 1:
#     print("800 000 so‘m")
# elif marks.count(4) == 2:
#     print("600 000 so‘m")
# else:
#     print("Stipendiya yo‘q")
# ##24-masala
# kod = int(input("Telefon raqamingizni bosh kodini kiriting: "))
# if kod == +99890 or kod == +99891 or kod == +99820:
#     print("Beeline")
# elif kod == +99893 or kod == +99894 or kod == +99850:
#     print("Ucell")
# elif kod == +99888 or kod == +99897 or kod == +99887:
#     print("Mobiuz")
# elif kod == +99899 or kod == +99877:
#     print("Uzmobile")
# elif kod == +99833 or kod == +99855:
#     print("Humans")
# elif kod == +99898:
#     print("Perfectum")
# else:
#     print("Noma’lum operator")
# ##25-masala
# turi = input("Pitsa turi (kichik/o‘rta/katta): ")
# narx = 30000 if turi == "kichik" else 45000 if turi == "o‘rta" else 60000
# pishloq = input("Pishloq qo‘shilsinmi? (ha/yo‘q): ")
# ichimlik = input("Ichimlik? (ha/yo‘q): ")
# if pishloq == "ha": narx += 5000
# if ichimlik == "ha": narx += 10000
# print(narx)
# ##26-masala
# tolov = input("To‘lov turi: ")
# summa = int(input("Summani kiriting: "))
# if tolov == "naqd":
#     print(summa)
# elif tolov == "plastik":
#     print(summa * 0.95)
# elif tolov == "onlayn":
#     print(summa * 0.90)
# else:
#     print("Xato")
# ##27-masala
# bp = input("Qon bosimi normalmi? (ha/yo‘q): ")
# hr = input("Yurak urishi yuqorimi? (ha/yo‘q): ")
# if bp == "yo‘q":
#     print("Qon bosimi muammosi")
# elif hr == "ha":
#     print("Tachikardiya")
# else:
#     print("Sog‘lom")
# ##28-masala
# fasl = input("Fasl: ")
# if fasl == "Bahor":
#     print("Samarqand")
# elif fasl == "Yoz":
#     print("Chorvoq")
# elif fasl == "Kuz":
#     print("Xiva")
# else:
#     print("Beldersoy")
# ##29-masala
# turi = input("Avto turi: ")
# sharoit = input("Sharoit: ")
# if turi == "yengil" and sharoit == "shahar":
#     print("10l/100km")
# elif turi == "yengil" and sharoit == "trassa":
#     print("7l/100km")
# elif turi == "yuk" and sharoit == "shahar":
#     print("20l/100km")
# else:
#     print("15l/100km")
# ##30-masala
# a = int(input("1-xizmat: "))
# b = int(input("2-xizmat: "))
# c = int(input("3-xizmat: "))
# print("Eng katta:", max(a, b, c))
# print("Eng kichik:", min(a, b, c))
# ##31-masala
# kvt = int(input("Elektr: "))
# if kvt <= 100:
#     print(kvt * 350)
# elif kvt <= 200:
#     print(kvt * 450)
# else:
#     print(kvt * 600)
# ##32-masala
# boy = int(input("Bo‘y: "))
# vazn = int(input("Vazn: "))
# if 100 <= boy <= 130 and 20 <= vazn <= 40:
#     print("Sog‘lom")
# else:
#     print("Tekshiruv kerak")
# ##33-masala
# gb = int(input("GB: "))
# if gb == 1:
#     print(9000)
# elif gb == 5:
#     print(25000)
# elif gb == 10:
#     print(45000)
# elif gb == 30:
#     print(90000)
# else:
#     print("Xato")
# ##34-masala
# a = int(input("1-ball: "))
# b = int(input("2-ball: "))
# c = int(input("3-ball: "))
# if a == b == c:
#     print("Durrang")
# else:
#     print("G‘olib balli:", max(a,b,c))
# ##35-masala
# ish = input("Ishlaydimi? (ha/yo‘q): ")
# oylik = int(input("Oylik: "))
# if ish == "ha" and oylik > 5000000:
#     print("Yaroqli")
# else:
#     print("Yaroqsiz")
# ##36-masala
# ram = int(input("RAM: "))
# gpu = input("Video karta bormi? (ha/yo‘q): ")
# if ram >= 8 and gpu == "ha":
#     print("O‘yin ishlaydi")
# else:
#     print("Tizim talabiga javob bermaydi")
# ##37-masala
# f1 = int(input("Fan1: "))
# f2 = int(input("Fan2: "))
# f3 = int(input("Fan3: "))
# if f1 == f2 == f3 == 5:
#     print("A’lochi")
# elif 4 in [f1, f2, f3]:
#     print("Yaxshi")
# else:
#     print("O‘rtacha")
# ##38-masala
# s = int(input("Xarid summasi: "))
# if s < 100000:
#     print(s)
# elif s <= 200000:
#     print(s * 0.95)
# else:
#     print(s * 0.90)
# ##39-masala
# km = float(input("Masofa: "))
# kun = input("Dam olish kuni? (ha/yo‘q): ")
# narx = km * 3000
# if kun == "ha":
#     narx *= 1.2
# print(narx)
# ##40-masala
# raqam = input("Hisob raqami: ")
# if len(raqam) == 16 and raqam.isdigit():
#     print("Yaroqli")
# else:
#     print("Xato")
# ##41-masala
# lavozim = input("Lavozim: ")
# if lavozim == "Direktor":
#     print("A")
# elif lavozim == "Menejer":
#     print("B")
# elif lavozim == "Ishchi":
#     print("C")
# else:
#     print("Noma’lum")
# ##42-masala
# hudud = input("Hudud: ")
# xona = int(input("Xonalar soni: "))
# if hudud == "Shahar" and xona == 3:
#     print(450_000_000)
# elif hudud == "Shahar" and xona == 2:
#     print(300_000_000)
# elif hudud == "Qishloq":
#     print(150_000_000)
# else:
#     print("Xato")
# ##43-masala
# mato = input("Mato turi: ")
# ifl = input("Ifloslik: ")
# if mato == "Paxta" and ifl == "Yengil":
#     print("Rejim 1")
# elif mato == "Sintetik" and ifl == "Og‘ir":
#     print("Rejim 3")
# else:
#     print("Rejim 2")
# ##44-masala
# nom = input("Kitob nomi: ").lower()
# if "sir" in nom or "jinoyat" in nom:
#     print("Detektiv")
# elif "sevgi" in nom or "romantika" in nom:
#     print("Romantik")
# elif "kosmos" in nom or "kelajak" in nom:
#     print("Fantastik")
# else:
#     print("Boshqa")
# ##45-masala
# turi = input("Chipta turi (VIP/Oddiy): ")
# yosh = int(input("Yosh: "))
# if turi == "VIP" and yosh > 60:
#     print(50000)
# elif turi == "Oddiy" and yosh < 18:
#     print(20000)
# else:
#     print(30000)
# ##46-masala
# kun = input("Kun: ")
# soat = int(input("Soat: "))
# if kun in ["Dushanba","Sesh","Chors","Pays","Juma"] and 9 <= soat <= 18:
#     print("Ochiq")
# elif kun in ["Shanba","Yakshanba"] and 10 <= soat <= 16:
#     print("Ochiq")
# else:
#     print("Yopiq")
# ##47-masala
# tur = input("O‘simlik turi: ")
# fasl = input("Fasl: ")
# if tur == "Gul" and fasl == "Bahor":
#     print("Haftada 3 marta sug‘oring")
# elif tur == "Daraxt" and fasl == "Yoz":
#     print("Har kuni sug‘oring")
# elif tur == "Gul" and fasl == "Qish":
#     print("Haftada 1 marta sug‘oring")
# else:
#     print("Haftada 2 marta sug‘oring")
# ##48-masala
# yosh = int(input("Yosh: "))
# oylik = int(input("Oylik: "))
# tarix = input("Tarix: ")
# if 21 <= yosh <= 65 and oylik > 3000000 and tarix == "Yaxshi":
#     print("Kredit beriladi")
# elif 21 <= yosh <= 65 and oylik > 3000000 and tarix == "Qoniqarli":
#     print("Qo'shimcha hujjat kerak")
# else:
#     print("Kredit berilmaydi")
# ##49-masala
# budjet = int(input("Budjet: "))
# vip = input("VIP kerakmi? (ha/yo‘q): ")
# korinish = input("Yaxshi ko‘rish kerakmi? (ha/yo‘q): ")
# if budjet > 100000 and vip == "ha":
#     print("Birinchi qator VIP")
# elif budjet > 100000 and vip == "yo‘q":
#     print("Birinchi qator oddiy")
# elif budjet <= 100000 and korinish == "ha":
#     print("O‘rta qatorlar")
# else:
#     print("Orqa qatorlar")
# ##50-masala
# x = int(input("Xotira foizi: "))
# if x >= 95:
#     print("Xotira to‘la! Tozalash kerak")
# elif x >= 80:
#     print("Xotira kam qoldi")
# elif x >= 50:
#     print("Xotira yetarli")
# else:
#     print("Xotira bo‘sh")
# ##51-masala
# h = int(input("Harorat: "))
# y = int(input("Yomg‘ir: "))
# if h < 0:
#     print("Qish kiyimi")
# elif 0 <= h < 15 and y > 50:
#     print("Kuz kiyimi va soyabon")
# elif 15 <= h < 25:
#     print("Bahor kiyimi")
# else:
#     print("Yoz kiyimi")
# ##52-masala
# b1 = int(input("1-bosqich: "))
# b2 = int(input("2-bosqich: "))
# b3 = int(input("3-bosqich: "))
# hammasi = b1 + b2 + b3
# if hammasi >= 90:
#     print("Ustoz")
# elif hammasi >= 70:
#     print("Malakali")
# elif hammasi >= 50:
#     print("O‘rta")
# else:
#     print("Boshlang‘ich")
# ##53-masala
# harorat = int(input("Harorat: "))
# if harorat < 0:
#     print("Juda sovuq")
# elif harorat < 15:
#     print("Salqin")
# elif harorat < 30:
#     print("Iliq")
# else:
#     print("Issiq")
# ##54-masala
# ball = int(input("Umumiy ball: "))
# if ball >= 90:
#     print("5 baxo")
# elif ball >= 71:
#     print("4 baxo")
# elif ball >= 60:
#     print("3 baxo")
# else:
#     print("Ball yetarli emas!")
# ##55-masala
# yosh = int(input("Yosh: "))
# talaba = input("Talabamisiz? (ha/yo'q): ")
# if yosh < 7:
#     print("Bepul")
# elif talaba == "ha":
#     print("5000 so‘m")
# elif yosh >= 60:
#     print("Chegirma: 3000 so‘m")
# else:
#     print("7000 so‘m")
# ##56-masala
# oy = int(input("Oy raqami: "))
# if oy in (12, 1, 2):
#     print("Qish")
# elif oy in (3, 4, 5):
#     print("Bahor")
# elif oy in (6, 7, 8):
#     print("Yoz")
# else:
#     print("Kuz")
# ##57-masala
# model = input("Model (iphone/samsung): ")
# holat = input("Holati (yangi/ishlatilgan): ")
# if model == "iphone" and holat == "yangi":
#     print("1200$")
# elif model == "iphone":
#     print("800$")
# elif model == "samsung" and holat == "yangi":
#     print("900$")
# else:
#     print("600$")
# ##58-masala
# yosh = int(input("Yosh: "))
# ball = int(input("Test ball: "))
# if yosh >= 6 and ball >= 70:
#     print("Qabul qilindi")
# else:
#     print("Qabul qilinmadi")
# ##59-masala
# t = int(input("Tezlik: "))
# if t < 5:
#     print("Juda sekin")
# elif t < 20:
#     print("O‘rtacha")
# elif t <= 100:
#     print("Tez")
# else:
#     print("Juda tez")
# ##60-masala
# vaqt = input("Vaqtingiz (ko‘p/kam/o‘rtacha): ")
# joy = input("Joy (ko‘p/kam): ")
# sabr = input("Sabr (ha/yo‘q): ")
# if vaqt == "kam" and joy == "kam":
#     print("Baliq")
# elif vaqt == "ko‘p" and sabr == "ha":
#     print("It")
# else:
#     print("Mushuk")
# ##61-masala
# yosh = int(input("Yosh: "))
# taj = int(input("Tajriba: "))
# ing = input("Ingliz tili (yaxshi/o‘rta/yomon): ")
# if yosh >= 22 and taj >= 2 and (ing == "yaxshi" or ing == "o‘rta"):
#     print("Qabul qilindi")
# else:
#     print("Qabul qilinmadi")
# ##62-masala
# yil = int(input("Yil: "))
# if (yil % 4 == 0 and yil % 100 != 0) or yil % 400 == 0:
#     print("Kabisa")
# else:
#     print("Kabisa emas")
# ##63-masala
# dar = int(input("Daromad: "))
# if dar <= 1_000_000:
#     print("0%")
# elif dar <= 3_000_000:
#     print("10%")
# else:
#     print("20%")
# ##64-masala
# ball = int(input("Ball: "))
# if ball >= 85:
#     print("Zo‘r natija!")
# elif ball >= 70:
#     print("Yaxshi!")
# elif ball >= 50:
#     print("O‘rtacha")
# else:
#     print("O‘tmadingiz")
# ##65-masala
# yosh = int(input("Yosh: "))
# tur = input("Mahsulot turi (oziq-ovqat/boshqa): ")
# if yosh < 12:
#     print("20%")
# elif yosh > 60:
#     print("15%")
# elif tur == "oziq-ovqat":
#     print("Chegirma yo‘q")
# else:
#     print("Chegirma yo‘q")
# ##66-masala
# y = int(input("Yosh: "))
# if 5 <= y <= 10:
#     print("Bolalar velosipedi")
# elif y <= 17:
#     print("Sport velosipedi")
# else:
#     print("Shahar velosipedi")
# ##67-masala
# ob = input("Ob-havo (issiq/boshqa): ")
# vaqt = input("Vaqt (tush/boshqa): ")
# if ob == "issiq" and vaqt == "tush":
#     print("Tavsiya qilinadi")
# else:
#     print("Keyinroq")
# ##68-masala
# yosh = int(input("Yosh: "))
# mun = input("Munosabat (yaqin/do‘st/boshqa): ")
# if mun == "yaqin" and yosh >= 18:
#     print("Chaqirilgan")
# elif mun == "do‘st" and yosh >= 25:
#     print("Chaqirilgan")
# else:
#     print("Chaqirilmagan")
# ##69-masala
# pul = input("Pul (ko‘p/kam): ")
# ob = input("Ob-havo (yaxshi/yomon): ")
# uzoqlik = input("Uzoqlik (yaqin/uzoq): ")
# if pul == "kam":
#     print("Mahalliy")
# elif ob == "yaxshi" and uzoqlik == "yaqin":
#     print("Tog‘")
# else:
#     print("Plyaj")
# ##70-masala
# tur = input("Tandir turi (elektr/gaz): ")
# vaqt = int(input("Vaqt (minut): "))
# if tur == "elektr" and vaqt < 30:
#     print("180°C")
# elif tur == "gaz" and vaqt >= 30:
#     print("200°C")
# else:
#     print("160°C")
# ##71-masala
# daraja = input("Daraja (bakalavr/magistr): ")
# baho = int(input("Baho: "))
# if daraja == "bakalavr" and baho >= 85:
#     print("Beriladi")
# elif daraja == "magistr" and baho >= 90:
#     print("Beriladi")
# else:
#     print("Berilmaydi")
# ##72-masala
# parol = input("Parol: ")
# raqam = any(ch.isdigit() for ch in parol)
# belgi = any(not ch.isalnum() for ch in parol)
# uzun = len(parol)
# if uzun >= 8 and raqam and belgi:
#     print("Xavfsiz")
# elif uzun >= 8 or raqam:
#     print("O‘rtacha")
# else:
#     print("Xavfli")
# ##73-masala
# tur = input("Tur (shahar/sport): ")
# soat = int(input("Soat: "))
# if tur == "shahar":
#     narx = 10000 * soat
# else:
#     narx = 15000 * soat
# if soat > 5:
#     narx *= 0.8
# elif soat > 3:
#     narx *= 0.9
# print(int(narx))
# ##74-masala
# og = int(input("Og‘irlik: "))
# kor = input("Korinishi (yaxshi/yomon): ")
# if og > 200 and kor == "yaxshi":
#     print("Premium")
# elif 100 <= og <= 200 and kor == "yaxshi":
#     print("Standart")
# elif kor == "yomon":
#     print("Past sifat")
# elif og < 100:
#     print("Rad etiladi")
# else:
#     print("Standart")
# ##75-masala
# summ = int(input("Summasi: "))
# vaqt = int(input("Soat (0–23): "))
# if summ > 100000 and 18 <= vaqt <= 22:
#     print("15% chegirma")
# elif 50000 <= summ <= 100000 and 10 <= vaqt < 18:
#     print("10% chegirma")
# else:
#     print("Chegirma yo‘q")
# ##76-masala
# rang = input("Rang (qizil/sariq/yashil): ")
# yol = input("Yo‘l (bo‘sh/band): ")
# if rang == "qizil":
#     print("To‘xtang")
# elif rang == "yashil" and yol == "bo‘sh":
#     print("Yuring")
# elif rang == "yashil":
#     print("Kuting")
# else:
#     print("Tayyorlaning")
# ##77-masala
# tur = input("Kitob turi (ilmiy/badiiy): ")
# kun = int(input("Kun: "))
# if tur == "ilmiy":
#     narx = 2000 * kun
# else:
#     narx = 1000 * kun
# if kun > 14:
#     narx *= 0.7
# elif kun > 7:
#     narx *= 0.8
# print(int(narx))
##78-masala
# yosh = int(input("Yoshingizni kiriting: "))
# holat = input("Holatni kiriting (ogir/oddiy): ").lower
# if 10 > yosh > 70:
#     print("ZUDLIK BILAN!")
# elif yosh > 10 and holat == 'ogir':
#     print("Navbat 1-soat ichida!")
# elif yosh > 10 and holat == 'oddiy':
#     print("Navbat 3-soat ichida!")
# else:
#     print("Ma'lumotlar xato kiritilgan!")
##79-masala
# osimlik = input("O'simlik turini kiriting: ").lower
# tuproq = input("tuproq turini kiriting: ").lower
# if osimlik == 'gul' and tuproq == 'qumoloq':
#     print("Har 2 kunda sug'oring!")
# elif osimlik == 'daraxt' and tuproq == 'loy':
#     print("Haftada 1 marta sug'oring!")
# else:
#     print("Har 3 kunda sug'oring!")
##80-masala
# xizmat = input("Xizmat turi (ta’mirlash/o‘rnatish): ")
# soat = float(input("Ishlagan soat: "))
# if xizmat.lower() == "ta’mirlash":
#     narx = 50000 * soat
#     if soat > 5:
#         narx = narx * 0.9
#     print("Jami narx:", int(narx))
# elif xizmat.lower() == "o‘rnatish":
#     narx = 30000 * soat
#     if soat > 5:
#         narx = narx * 0.9
#     print("Jami narx:", int(narx))
# else:
#     print("Noto‘g‘ri xizmat turi")
##81-masala
# sinf = int(input("Sinf: "))
# ogirlik = float(input("Sumka og‘irligi (kg): "))
# if 1 <= sinf <= 4:
#     if ogirlik > 2:
#         print("Og‘ir, kamaytiring")
#     else:
#         print("Normal")
# elif 5 <= sinf <= 9:
#     if ogirlik > 4:
#         print("Og‘ir, kamaytiring")
#     else:
#         print("Normal")
# else:
#     print("Normal")
##82-masala
# turi = input("Buyurtma turi (kofe/choy): ")
# miqdor = int(input("Nechta dona: "))
# if turi.lower() == "kofe":
#     narx = 15000 * miqdor
#     if miqdor > 5:
#         narx = narx * 0.9
#     print("Jami narx:", int(narx))
# elif turi.lower() == "choy":
#     narx = 5000 * miqdor
#     if miqdor > 5:
#         narx = narx * 0.9
#     print("Jami narx:", int(narx))
# else:
#     print("Noto‘g‘ri buyurtma turi")
##83-masala
# transport = input("Transport turi (piyoda/velosiped/avtobus): ")
# masofa = float(input("Masofa (km): "))
# if transport.lower() == "piyoda":
#     vaqt = 12 * masofa
#     print("Safar vaqti:", int(vaqt), "daqiqa")
# elif transport.lower() == "velosiped":
#     vaqt = 4 * masofa
#     print("Safar vaqti:", int(vaqt), "daqiqa")
# elif transport.lower() == "avtobus":
#     vaqt = 2 * masofa
#     print("Safar vaqti:", int(vaqt), "daqiqa")
# else:
#     print("Noto‘g‘ri transport turi")
##84-masala
# foiz = float(input("Batareya foizi (%): "))
# soat = float(input("Foydalanish vaqti (soat): "))
# if foiz < 20 and soat > 1:
#     print("Zudlik bilan zaryadlang")
# elif 20 <= foiz <= 50 and soat < 1:
#     print("Tezroq zaryadlang")
# elif foiz == 50:
#     print("Yaxshi holat")
# else:
#     print("Normal holat")
##84-masala
# mijoz = input("Mijoz turi (doimiy/yangi): ")
# summasi = float(input("Xarid summasi (so‘m): "))
# if mijoz.lower() == "doimiy" and summasi > 50000:
#     print("Bonus: 5000 so‘m")
# elif mijoz.lower() == "yangi" and summasi > 100000:
#     print("Bonus: 3000 so‘m")
# else:
#     print("Bonus yo‘q")
##86-masala
# harorat = float(input("Harorat (°C): "))
# yomgir = float(input("Yomg‘ir ehtimoli (%): "))
# if harorat < 5:
#     print("Issiq kiyining")
# elif yomgir > 70:
#     print("Soyabon oling")
# elif 5 <= harorat <= 25 and yomgir < 30:
#     print("Yengil kiyining")
# else:
#     print("Normal kiyim")
##87-masala
# ball = float(input("Ball: "))
# kvota = input("Kvota bor/yo‘q: ")
# if ball >= 90 and kvota.lower() == "bor":
#     print("Qabul qilindi")
# elif 70 <= ball < 90 and kvota.lower() == "yo‘q":
#     print("Navbat kuting")
# elif ball < 70:
#     print("Qabul qilinmadi")
# else:
#     print("Shartlarga mos emas")
##88-masala
# tur = input("Mashq turi (Kardio/Og‘irlik): ").lower
# tajriba = float(input("Tajriba (yil): "))
# if tur == "kardio" and tajriba < 1:
#     print("20 daqiqa yengil")
# elif tur == "og‘irlik" and tajriba >= 2:
#     print("60 daqiqa intensiv")
# else:
#     print("30 daqiqa o‘rtacha")
##89-masala
# korsatuv_turi = input("Ko'rsatuv turini kiriting: ").lower
# soat = float(input("Vaqtni kiriting: "))
# if korsatuv_turi == 'yangiliklar' and 18.00 < soat < 20.00:
#     print("Tomosha qiling!")
# elif korsatuv_turi == "serial" and 20.00 < soat < 22.00:
#     print("Qayta koring!")
# else:
#     print("Boshqa ko'rsatuv tomosha qiling!")
##90-masala
# tur = input("Skuter turini kiriting: ").lower
# masofa = int(input("Masofani kiriting: "))
# if tur == 'elektr' and masofa <= 1:
#     print("Sizdan 2000 so'm")
# elif tur == 'oddiy' and masofa <= 1:
#     print("Sizdan 1000 so'm")
# elif tur == 'oddiy' and masofa > 10 or tur == 'elektor' and masofa > 10:
#     print("Sizga 15% chegirma!")
# else:
#     print("Uzir xatolik yuz berdi!")
##91-masala
# muammo_turi = input("Muammoni kiriting: ").lower
# qism_narxi = int(input("Qism narxini kiriting: "))
# if muammo_turi == 'dastury':
#     print("Sizdan 50 000so'm")
# elif muammo_turi == 'uskunaviy' and qism_narxi > 100_000:
#     print("Sizdan 150 000so'm")
# elif muammo_turi == 'uskunaviy' and qism_narxi <= 100_000:
#     print("Sizdan 80 000")
# else:
#     print("Sizdan 100 000")
##92-masala
# ifloslanish = int(input("Ifloslanish darajasi: "))
# shamol = int(input("Shamol tezligi (km/s): "))
# if ifloslanish > 50 and shamol < 5:
#     print("Maska kiying")
# elif ifloslanish <= 50 and shamol > 10:
#     print("Sof havo")
# else:
#     print("Oddiy holat")
##93-masala
# kurs = input("Kurs turi (akvarel/yogli): ")
# oy = int(input("Davomiylik (oy): "))
# if kurs == "akvarel" and oy == 1:
#     narx = 200000
# elif kurs == "yogli" and oy == 1:
#     narx = 300000
# else:
#     narx = 0

# if oy > 3:
#     narx = narx * 0.9
# print("Narx:", narx, "so'm")
##94-masala
# tur = input("Qulf turi (elektron/mexanik): ")
# yosh = int(input("Qulf yoshi (yil): "))
# if tur == "elektron" and yosh < 2:
#     print("Yuqori xavfsizlik")
# elif tur == "mexanik" and yosh < 5:
#     print("O‘rtacha xavfsizlik")
# else:
#     print("Past xavfsizlik")
##95-masala
# joy = input("Joylashuvi (markaz/chet): ")
# xona = int(input("Xonalar soni: "))
# if joy == "markaz" and xona == 3:
#     print("5 000 000 so'm")
# elif joy == "chet" and xona == 2:
#     print("3 000 000 so'm")
# else:
#     print("2 000 000 so'm")
##96-masala
# quvvat = int(input("Quvvat (%): "))
# masofa = int(input("Bosiladigan masofa (km): "))
# if quvvat < 20 and masofa > 5:
#     print("Zaryadlang")
# elif 20 <= quvvat <= 50 and masofa < 3:
#     print("Ehtiyot bo‘ling")
# elif quvvat > 50:
#     print("Yaxshi holat")
# else:
#     print("Oddiy holat")
##97-masala
# ruxsat = int(input("Ruxsat (MP): "))
# yoruglik = input("Yorug'lik (yaxshi/o'rtacha/yomon): ")
# if ruxsat >= 12 and yoruglik == "yaxshi":
#     print("Yuqori sifat")
# elif 8 <= ruxsat < 12 and yoruglik == "o'rtacha":
#     print("O‘rtacha sifat")
# else:
#     print("Past sifat")
##98-masala
# masofa = int(input("Masofa (km): "))
# obhavo = input("Ob-havo (yaxshi/o'rtacha/yomon): ")
# if masofa < 5 and obhavo == "yaxshi":
#     print("Piyoda")
# elif 5 <= masofa <= 20 and obhavo == "o'rtacha":
#     print("Velosiped")
# else:
#     print("Avtobus")
##99-masala
# email = input("Emailni kiriting: ")
# uzunlik = len(email)
# if "@gmail.com" in email:
#     domen = "@gmail.com"
# elif "@yahoo.com" in email:
#     domen = "@yahoo.com"
# else:
#     domen = ""
# if uzunlik >= 10 and domen == "@gmail.com":
#     print("Qabul qilindi")
# elif uzunlik < 10 and domen == "@yahoo.com":
#     print("Qisqa email")
# else:
#     print("Noto‘g‘ri email")
##100-masala
# ovqat = input("Ovqat turi (salat/gosht): ")
# porsiya = int(input("Porsiya (gramm): "))
# if ovqat == "salat" and porsiya == 100:
#     kal = 50
# elif ovqat == "gosht" and porsiya == 100:
#     kal = 200
# else:
#     kal = 0
# if porsiya > 300:
#     kal = kal * 1.1
# print("Kaloriya:", kal)












