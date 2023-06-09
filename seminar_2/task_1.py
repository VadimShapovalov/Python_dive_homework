# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег

def cash_machine():
    account = 0
    operation = 1
    try:
        with open('account.txt', 'r') as acc:
            account = int(acc.readline())
            operation = int(acc.readline())
    except Exception:
        print("У Вас не было счета в нашем банке! Мы открыли Вам счет!")
    flag = True
    print("Добро пожаловать!")
    while flag:
        print("Введите действие, которое хотите совершить:")
        print("1. Пополнить счет.\n2. Cнять деньги со счета.\n3. Узнать баланс счета\n4. Закончить операции со счетом.")
        action = input()
        if account > 5_000_000:
            print(f"Вы слишком богатый!. На Вашем счету {account} руб. Банк вынужден снять с Вашего счета 10%.")
            account = account * 0.90
            print(f"Теперь на Вашем счету {account} руб. Спасибо за заботу о бедных!")
        match action:
            case "1":
                add_money = refill(operation)
                if add_money != 0:
                    operation += 1
                    account += add_money
                    print(f"Теперь на Вашем счету {account:.2f} руб.")
            case "2":
                withdrawal = withdraw(account, operation)
                if withdrawal != 0:
                    operation += 1
                    account -= withdrawal
            case "3":
                print(f"На Вашем счету {account:.2f} руб")
            case "4":
                print("До новых встреч!")
                with open('account.txt', 'w') as acc:
                    acc.write(str(account) + '\n')
                    acc.write(str(operation))
                flag = False
            case _:
                print("Вы ввели некорректные данные. Пожалуйста, повторите попытку.")
                continue

def refill(operation):
    while True:
        print("Вложите купюры в купюроприемник. Сумма пополнения должна быть кратна 50 рублям.")
        print("Если хотите вернуться в главное меню. Нажмите 'Y'.")
        entered_data = input().lower()
        if entered_data == 'y':
            return 0  # break
        else:
            try:
                money = int(entered_data)
                if money % 50 != 0:
                    print("Введенная сумма не кратна 50 рублям. Пожалуйста, повторите попытку.")
                    continue
                else:
                    if operation % 3 != 0:
                        print(f"Вы положили на счет {money} рублей.")
                        return money
                    else:
                        print(f"Вы положили на счет {money} рублей. На за каждую третью операция взимается 3 %")
                        money = money * 0.97
                        print(f"Таким образом на Ваш счет зачислено {money} руб.")
                        return money
            except ValueError:
                print("Вы ввели некорректные данные. Пожалуйста, повторите попытку.")
                continue

def withdraw(account, operation):
    while True:
        print("Введите сумму, которую хотите снять. За снятие взимается комиссия - 1,5%, но не менее 30 руб. и не более 600 руб.")
        print("Если хотите вернуться в главное меню, нажмите 'Y'.")
        entered_data = input().lower()
        if entered_data == 'y':
            return 0
        else:
            try:
                money = int(entered_data)
                if money * 1.015 > account or money + 30 > account:
                    print("Ваших средств недостаточно. Пожалуйста, повторите попытку.")
                    continue
                else:
                    commission = money * 0.015
                    ex_commission = money * 0.03
                    if commission < 30:
                        commission = 30
                    elif commission > 600:
                        commission = 600
                if money % 50 != 0:
                    print("Введенная сумма не кратна 50 рублям. Пожалуйста, повторите попытку.\n")
                    continue
                else:
                    if operation % 3 != 0:
                        print(f"Вы сняли {money} рублей. Комиссия за операцию составила {commission:.2f} руб.")
                        return money + commission
                    else:
                        print(f"Вы хотели снять {money} рублей. Комиссия за операцию составила {commission:.2f} руб.")
                        print(f"За каждую 3-ю операцию доп. комиссия 3%. Вы получите {money - ex_commission} руб.")
                        return money + commission
            except ValueError:
                print("Вы ввели некорректные данные, либо сумма не кратна 50 рублям. Пожалуйста, повторите попытку.\n")
                continue


# refill()
cash_machine()

