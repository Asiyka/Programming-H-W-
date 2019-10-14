arr = []
count_item = int(input("Введіть кількість елементів: "))

for i in range(count_item):
    el = input("Введіть елементи: ")
    arr.append(int(el))

while True: 
    print("1.Вивести всі елементи які меньші за середнє арифметичне")
    print("2.Вивести найбільший елемент")
    print("3.Вивести найменьший елемент")
    print("4.Поміняти 3 і 4 елементи місцями")

    menu_switcher = input("Виберіть: ") 
    if menu_switcher == "1":
      x = sum(arr) / count_item
      for el in arr:
        if el < x:
            print(el)
    elif menu_switcher == "2":
        print(max(arr))
    elif menu_switcher == "3":
        print(min(arr))
    elif menu_switcher == "4":
        arr[2],arr[3]=arr[3],arr[2]
        print(arr)
else:
    print("Такого немає")
