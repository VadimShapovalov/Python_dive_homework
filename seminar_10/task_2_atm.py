import datetime


class Atm:

    def __init__(self):
        self.account = 0
        self.operation = 1
        self.operations = []

    def refill(self):
        """function replenishes the bank account."""
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
                        if self.operation % 3 != 0:
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

    def withdraw(self):
        """the function withdraws money from a bank account."""
        while True:
            print("Введите сумму, которую хотите снять."
                  " За снятие взимается комиссия - 1,5%, но не менее 30 руб. и не более 600 руб.")
            print("Если хотите вернуться в главное меню, нажмите 'Y'.")
            entered_data = input().lower()
            if entered_data == 'y':
                return 0
            else:
                try:
                    money = int(entered_data)
                    if money * 1.015 > self.account or money + 30 > self.account:
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
                        if self.operation % 3 != 0:
                            print(f"Вы сняли {money} рублей. Комиссия за операцию составила {commission:.2f} руб.")
                            return money + commission
                        else:
                            print(
                                f"Вы хотели снять {money} рублей. Комиссия за операцию составила {commission:.2f} руб.")
                            print(f"За каждую 3-ю операцию доп. комиссия 3%. Вы получите {money - ex_commission} руб.")
                            return money + commission
                except ValueError:
                    print(
                        "Вы ввели некорректные данные, либо сумма не кратна 50 рублям. Пожалуйста, повторите попытку.\n")
                    continue

    def cash_machine(self):
        """function simulates the operation of an atm. """
        # account = 0
        # operation = 1
        # operations = []
        try:
            with open('account.txt', 'r', encoding="utf-8") as acc:
                self.account = float(acc.readline())
                self.operation = int(acc.readline())
                self.operations = acc.readlines()
        except Exception:
            print("У Вас не было счета в нашем банке! Мы открыли Вам счет!")
        flag = True
        print("Добро пожаловать!")
        while flag:
            print("Введите действие, которое хотите совершить:")
            print(
                "1. Пополнить счет.\n2. Cнять деньги со счета.\n"
                "3. Узнать баланс счета\n4. Закончить операции со счетом.")
            action = input()
            if self.account > 5_000_000:
                print(f"Вы слишком богатый!. На Вашем счету {self.account} руб. "
                      f"Банк вынужден снять с Вашего счета 10%.")
                self.account = self.account * 0.90
                print(f"Теперь на Вашем счету {self.account} руб. Спасибо за заботу о бедных!")
            match action:
                case "1":
                    add_money = self.refill()
                    if add_money != 0:
                        self.account += add_money
                        print(f"Теперь на Вашем счету {self.account :.2f} руб.")
                        str_operat = f"операция со счетом №{self.operation}: пополнение счета;" \
                                     f"  сумма операции: {add_money} руб.;" \
                                     f" время: {datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S')};" \
                                     f" Счет: {self.account :.2f}"
                        self.operations.append(str_operat)
                        self.operation += 1
                case "2":
                    withdrawal = self.withdraw()
                    if withdrawal != 0:
                        self.account -= withdrawal
                        str_operat = f"операция со счетом №{self.operation}: снятие со счета; " \
                                     f" сумма операции: {withdrawal:.2f} руб.;" \
                                     f" время: {datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S')}; " \
                                     f"Счет: {self.account :.2f}"
                        self.operations.append(str_operat)
                        self.operation += 1
                case "3":
                    print(f"На Вашем счету {self.account :.2f} руб")
                    str_operat = f"справочная операция: информация по счету; время:" \
                                 f" {datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S')};" \
                                 f" Счет: {self.account :.2f}"
                    self.operations.append(str_operat)
                case "4":
                    print("До новых встреч!")
                    str_operat = f"операция с программой: окончание работы с программой;" \
                                 f" время: {datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S')};" \
                                 f" Счет: {self.account :.2f}"
                    self.operations.append(str_operat)
                    with open('account.txt', 'w', encoding="utf-8") as acc:
                        acc.write(str(self.account) + '\n')
                        acc.write(str(self.operation) + '\n')
                        for line in self.operations:
                            acc.write(line.strip() + '\n')
                    flag = False
                    print(self.operations)
                case _:
                    print("Вы ввели некорректные данные. Пожалуйста, повторите попытку.")
                    continue


if __name__ == '__main__':
    c_m = Atm()
    c_m.cash_machine()
