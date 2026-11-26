# 1. Tomendegi listtegi barliq miywelerdi birewden ekranqa shiqariw
fruits = ['apple', 'banana', 'orange', 'kiwi']
for fruit in fruits:
  print(fruit)

# 2. Barliq atlardi ulken hariplerde ekranqa shiqariw
names = ['ali', 'vali', 'hasan', 'husan']
for name in names:
  print(name.upper())

# 3. Mashina atlarinin tek birinshi haribin ekranqa shiqariw
cars = ['bmw', 'mers', 'nexia', 'malibu', 'cobalt']
for car in cars:
  print(car[0])

# 4. Mamleket atlarin kishi hariplerde ekranqa shiqariw
countries = ['UZBEKISTAN', 'RUSSIA', 'TURKEY', 'USA']
for country in countries:
  print(country.lower())

# 5. Harbir esim neshe haripten ibarat ekenligin shiqariw
names = ['ali', 'sardor', 'abdulloh', 'aziz']
for name in names:
  print(f'{name} - {len(name)} ta harf')

# 6. [0, 1, 2, 3] ornina range() qollaniw
animals = ['cat', 'dog', 'lion', 'tiger']
for i in range(4):
  animals[i] = animals[i].upper()
print(animals)

# 7. List ishindegi barliq atlardi ulken hariplerge ozgertiw
names = ['ali', 'vali', 'sardor', 'aziz']
for i in range(len(names)):
  names[i] = names[i].upper()
print(names)

# 8. Harbir attin tek birinshi haribin ulken etip ozgertiw
names = ['ali', 'hasan', 'husan', 'sardor']
for i in range(len(names)):
  names[i] = names[i].capitalize()
print(names)

# 9. Tek jup indekste turqan atlardi ekranqa shiqariw
names = ['ali', 'vali', 'hasan', 'husan', 'sardor', 'aziz']
for i in range(0, len(names), 2):
  print(names[i])

# 10. Harbir haywan atinin birinshi ham aqirqi haribin shiqariw
animals = ['tiger', 'lion', 'elephant', 'rabbit']
for animal in animals:
  print(f'{animal[0]} - {animal[-1]}')

# 11. Harbir sozdin birinshi ham aqirqi haribin bas haripke ozgertiw
words = ['python', 'programming', 'computer', 'developer']
for i in range(len(words)):
  words[i] = words[i][0].upper() + words[i][1:-1] + words[i][-1].upper()
print(words)

# 12. Qolda jazilqan indeksler ornina range() ham len() dan paydalaniw
cars = ['bmw', 'nexia', 'malibu', 'cobalt', 'damas']
for i in range(len(cars)):
  cars[i] = cars[i].upper()
print(cars)

# 13. Atin takirarlaw
ism = input('Ism kiriting: ')
n = int(input('Necha marta chiqarilsin: '))
for i in range(n):
  print(ism)

# 14. Miyweler dizimi
miyweler = []
n = int(input('Nechta meva kiritmoqchisiz: '))
for i in range(1, n + 1):
  miywe = input(f'{i}-mevani kiriting: ')
  miyweler.append(miywe)
print('Mevalar:', miyweler)

# 15. Jaqsi koretuqin renler
renler = []
for i in range(1, 6):
  ren = input(f'{i}-rangni kiriting: ')
  renler.append(ren)

print('\nSizning sevimli ranglaringiz:')
for ren in renler:
  print(ren)