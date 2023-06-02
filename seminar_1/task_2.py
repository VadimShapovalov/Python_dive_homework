# Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке

print("                          ТАБЛИЦА УМНОЖЕНИЯ", end="\n\n")
for i in range(2, 11):
    for j in range(2, 6):
        print(f"{j:2} x {i:^2} = {j * i:2}", end="\t\t")
    print()
print()
for i in range(2, 11):
    for j in range(6, 10):
        print(f"{j:2} x {i:^2} = {j * i:2}", end="\t\t")
    print()
