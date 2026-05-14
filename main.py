# import random
#
# rekord = 999
#
# def oyin():
#     global rekord
#
#     print(" SON TOPISH O‘YINI")
#     ism = input("Ismingizni kiriting: ")
#
#     print("\nQiyinchilik tanlang:")
#     print("1. Oson (1-10)")
#     print("2. O‘rta (1-50)")
#     print("3. Qiyin (1-100)")
#
#     tanlov = input("Tanlov: ")
#
#     if tanlov == "1":
#         max_son = 10
#     elif tanlov == "2":
#         max_son = 50
#     else:
#         max_son = 100
#
#     sirli = random.randint(1, max_son)
#
#     urinishlar = []
#     urinish_soni = 0
#
#     print(f"\nMen 1 dan {max_son} gacha son o‘yladim.")
#
#     while True:
#         taxmin = int(input("Son kiriting: "))
#
#         urinishlar.append(taxmin)
#         urinish_soni += 1
#
#         if taxmin > sirli:
#             print(" Kichikroq son kiriting")
#
#         elif taxmin < sirli:
#             print(" Kattaroq son kiriting")
#
#         else:
#             print("\n TABRIKLAYMAN,", ism)
#             print(" Siz yutdingiz!")
#
#             print(" Urinishlar soni:", urinish_soni)
#             print(" Kiritilgan sonlar:", urinishlar)
#
#             if urinish_soni < rekord:
#                 rekord = urinish_soni
#                 print(" YANGI REKORD!")
#
#             print(" Rekord:", rekord)
#
#             break
#
#
# while True:
#     oyin()
#
#     yana = input("\nyana  o‘ynaysizmi? (ha/yoq): ")
#
#     if yana != "ha":
#         print("oyin tugadi")
#         break
