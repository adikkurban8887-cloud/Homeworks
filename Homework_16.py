numbers = [10, 20, 30, 40, 50]

print(numbers[0])
print(numbers[-1])
print(numbers[2])


numbers = [10, 20, 30, 40, 50]

print(numbers[0])
print(numbers[-1])
print(numbers[2])


colors = ['red', 'green', 'blue', 'yellow']

colors[1] = 'black'
colors[3] = 'white'
print(colors)


students = ['Ali', 'Vali', 'Hasan', 'Husan', 'Olim']
print(len(students))


numbers = [10, 20, 30, 40, 50, 60, 70, 80]
print(numbers[2:5])



letters = ['a', 'b', 'c', 'd', 'e', 'f']
print(letters[::-1])


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[::2])


students = [
    ['Ali', 90, 'English'],
    ['Vali', 85, 'Math'],
    ['Hasan', 95, 'Python']
]

for item in students[0]:
    print(item)


students = [
    ['Ali', 90],
    ['Vali', 85],
    ['Hasan', 95]
]

students[0][1] = 100
print(students)


programming = [
    ['HTML', 'CSS'],
    ['Python', 'JavaScript'],
    ['Java', 'C++']
]

print(programming[1][0])
print(programming[1][1])


numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(numbers[1::3])


numbers = [12, 7, 8, 15, 20, 33, 44, 51, 60]
even_numbers = [n for n in numbers if n % 2 == 0]
print(even_numbers)


numbers = [1, 2, 3, 2, 4, 1, 5, 3, 6]
unique_numbers = []

for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)

print(unique_numbers)


numbers = [10, 20, 30, 40, 50, 60, 70, 80]
mid = len(numbers) // 2

list_1 = numbers[:mid]
list_2 = numbers[mid:]

print("1-list:", list_1)
print("2-list:", list_2)



numbers = [10, 20, 30, 40, 50]

numbers[1], numbers[3] = numbers[3], numbers[1]

print(numbers)



students = ['Ali', 'Vali', 'Hasan', 'Husan', 'Olim']

students[0], students[-1] = students[-1], students[0]

print(students)



students = [
    ['Ali', 85],
    ['Vali', 90],
    ['Hasan', 75],
    ['Husan', 95]
]

students[0], students[2] = students[2], students[0]

print(students)



fruits = ["Olma", "Uzum", "Banan", "Anor", "Shaftoli"]

print("Mevalar:")
for i, fruit in enumerate(fruits, start=1):
    print(f"{i}. {fruit}")

choice = int(input("\nQaysi mevani tanlaysiz? "))

if 1 <= choice <= len(fruits):
    selected_fruit = fruits[choice - 1]
    print(f"\nSiz {selected_fruit} mevasini tanladingiz!")
else:
    print("\nQate nomer kiritildi!")



fruits = ['Olma', 'Uzum', 'Banan', 'Anor', 'Shaftoli']
prices = [5, 8, 12, 10, 15]

print("========= FRUIT MARKET =========\n")


for i in range(len(fruits)):
    print(f"{i + 1}. {fruits[i]} - {prices[i]}$")

choice = int(input("\nQaysi mevani tanlaysiz? ")) - 1


selected_fruit = fruits[choice]
price_per_kg = prices[choice]


kg = float(input(f"\n{selected_fruit} mevasidan necha kg olasiz? "))


total_price = price_per_kg * kg


print("\n========= CHEK =========\n")
print(f"Meva: {selected_fruit}")
print(f"Miqdori: {kg} kg")
print(f"1 kg narxi: {price_per_kg}$")
print(f"\nUmumiy narx: {total_price:g}$")
print("\nXaridingiz uchun rahmat!")


fruits = ['apple', 'banana', 'orange']


fruits.append('mango')


fruits.insert(2, 'strawberry')

print(fruits)


fruits = ['apple', 'banana', 'orange']

fruits.append('mango')
fruits.insert(2, 'strawberry')

print(fruits)


cars = ['BMW', 'Mercedes', 'Audi', 'Tesla']

cars.remove('BMW')

print(cars)


numbers = [10, 20, 30, 40, 50]

ochirilgan = numbers.pop()

print("O'chirilgan element:", ochirilgan)
print("Qolgan list:", numbers)


fruits = ['apple', 'banana', 'apple', 'orange', 'apple', 'kiwi']

sani = fruits.count('apple')

print("apple soni:", sani)



languages = ['Java', 'C++', 'Python', 'JavaScript', 'PHP']

indeks = languages.index('Python')

print("Python indeksi:", indeks)




numbers = [45, 12, 89, 3, 21, 67, 10]

numbers.sort()

print(numbers)