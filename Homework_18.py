# 1. Jas boyinsha tekseriw
def task_1():
    jasi = int(input("Yoshingizni kiriting: "))
    if jasi >= 18:
        print("Siz voyaga yetgansiz!")
    else:
        print("Siz voyaga yetmagansiz!")

# 2. Paroldi tekseriw
def task_2():
    parol = input("Parolni kiriting: ")
    if parol == "python123":
        print("Xush kelibsiz!")
    else:
        print("Parol naduris!")

# 3. 10% shegirme esaplaw
def task_3():
    baha = float(input("Mahsulot narxini kiriting: "))
    if baha > 500000:
        shegirme = baha * 0.10
        juwmaqlawshi = baha - shegirme
        print(f"Chegirma: {int(shegirme)} so'm")
        print(f"Yakuniy narx: {int(juwmaqlawshi)} so'm")
    else:
        print("Chegirma yo'q")
        print(f"Yakuniy narx: {int(baha)} so'm")

# 4. Araliq boyinsha jol haqin esaplaw
def task_4():
    araliq = int(input("Araliqti kirgizin: "))
    if araliq > 10:
        km_baha = 3000
    else:
        km_baha = 2000
    uliwma = araliq * km_baha
    print(f"1 km bahasi: {km_baha} sum.")
    print(f"Uliwma bahasi: {uliwma} sum.")

# 5. Buyirtpa ham jetkerip beriw bahasi
def task_5():
    baha = int(input("Buyirtpa bahasi: "))
    if baha > 100000:
        print("Jetkiziw biypul!")
    else:
        jetkiziw = 15000
        print(f"Jetkerip beriw: {jetkiziw} sum.")
        print(f"Jami tolem: {baha + jetkiziw} sum.")

# 6. Ball boyinsha bahalaw
def task_6():
    ball = int(input("Ballingizni kiriting: "))
    if 90 <= ball <= 100:
        print("Sizning bahoyingiz: Alo")
    elif 75 <= ball <= 89:
        print("Sizning bahoyingiz: Yaxshi")
    elif 60 <= ball <= 74:
        print("Sizning bahoyingiz: Qoniqarli")
    elif 0 <= ball <= 59:
        print("Sizning bahoyingiz: Qoniqarsiz")
    else:
        print("Noto'g'ri ball kiritildi!")

# 7. Transport turin nomer arqali tanlaw
def task_7():
    transportlar = ["Avtobus", "Metro", "Taksi", "Velosiped"]
    narxlar = [2000, 1700, 15000, 1000]
    print("===== TRANSPORT TANLASH =====")
    for i in range(len(transportlar)):
        print(f"{i + 1}. {transportlar[i]}")
    tanlaw = int(input("\nTransportni tanlang: ")) - 1
    if 0 <= tanlaw < len(transportlar):
        print(f"\nSiz {transportlar[tanlaw]} transportini tanladingiz.")
        print(f"Narxi: {narxlar[tanlaw]} so'm")
    else:
        print("Noto'g'ri raqam tanlandi!")

# 8. Miyweler diziminen izlew
def task_8():
    mevalar = ["olma", "banan", "uzum", "anor", "shaftoli"]
    miywe = input("Meva nomini kiriting: ").lower()
    if miywe in mevalar:
        print(f"{miywe} ro'yxatda mavjud!")
    else:
        print(f"{miywe} ro'yxatda mavjud emas!")

# 9. Oqiwshilar diziminen izlew
def task_9():
    oquvchilar = ["Ali", "Vali", "Sardor", "Malika", "Madina"]
    ism = input("Ism kiriting: ")
    if ism in oquvchilar:
        print("O'quvchi ro'yxatda mavjud!")
        print(f"Birinchi harfi: {ism[0]}")
    else:
        print("O'quvchi ro'yxatda mavjud emas!")

# 10. Jup ham taq sanlardi ajiratiw
def task_10():
    numbers = [12, 5, 8, 17, 20, 3, 10, 7]
    for num in numbers:
        if num % 2 == 0:
            print(f"{num} - Juft son")
        else:
            print(f"{num} - Toq son")

# 11. List elementlerin ozgertiw
def task_11():
    numbers = [2, 5, 8, 11, 14, 17]
    for i in range(len(numbers)):
        if numbers[i] < 10:
            numbers[i] = numbers[i] * 2
        else:
            numbers[i] = numbers[i] + 5
    print(numbers)

# 12. Tovarlar dukani (nomer arqali tanlaw)
def task_12():
    products = ["Go'sht", "Non", "Sut", "Tuxum", "Guruch"]
    prices = [90000, 4000, 12000, 1800, 15000]
    print("Mahsulotlar:")
    for i in range(len(products)):
        print(f"{i + 1}. {products[i]} - {prices[i]} so'm")
    idx = int(input("\nQaysi mahsulot kerak? ")) - 1
    sani = int(input(f"{products[idx]} qancha kerak? "))
    uliwma = prices[idx] * sani
    print(f"\nMahsulot: {products[idx]}")
    print(f"Soni: {sani}")
    print(f"Umumiy summa: {uliwma} so'm")

# 13. Tovar ati boyinsha izlew
def task_13():
    products = ["Non", "Sut", "Go'sht", "Olma", "Banan"]
    prices = [4000, 12000, 90000, 8000, 15000]
    at = input("Qanday mahsulot olmoqchisiz? ")
    tabildi = False
    for i in range(len(products)):
        if products[i].lower() == at.lower():
            tabildi = True
            sani = int(input(f"{products[i]} qancha kerak? "))
            print(f"\nUmumiy summa: {prices[i] * sani} so'm")
            break
    if not tabildi:
        print("\nBunday mahsulot yo'q!")

# 14. Oqiwshilar bahasi (Nested for)
def task_14():
    grades = [,
 ,
        [3, 2, 4]
    ]
    for qatar in grades:
        for baha in qatar:
            print(baha, end=" ")
        print()
    for i in range(len(grades)):
        for j in range(len(grades[i])):
            if grades[i][j] == 5:
                grades[i][j] = 4
            elif grades[i][j] == 2:
                grades[i][j] = 3
    print(grades)

# 15. Skladtaqi tovarlardi tekseriw
def task_15():
    products = [
        ["Non", 4000, 10],
        ["Sut", 12000, 5],
        ["Go'sht", 90000, 2],
        ["Olma", 8000, 0]
    ]
    for i in range(len(products)):
        at = products[i][0]
        sani = products[i][2]
        if sani < 5:
            status = "Az qalqan"
        else:
            status = "Jetkilikli"
        print(f"{i + 1}. {at}, Sani: {sani}")
        print(f"Status: {status}\n")

# Menyu arqali iske tusiriw
tasks = {
    "1": task_1, "2": task_2, "3": task_3, "4": task_4, "5": task_5,
    "6": task_6, "7": task_7, "8": task_8, "9": task_9, "10": task_10,
    "11": task_11, "12": task_12, "13": task_13, "14": task_14, "15": task_15
}

while True:
    tanlaw = input("\nMasele nomerin kirgizin (1-15, shiqiw ushin 0): ")
    if tanlaw == "0":
        break
    elif tanlaw in tasks:
        print("-" * 30)
        tasks[tanlaw]()
        print("-" * 30)
    else:
        print("Qate nomer! 1 den 15 ke shekem san kirgizin.")
