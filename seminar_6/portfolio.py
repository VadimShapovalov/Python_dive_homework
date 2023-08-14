# Задача: Расчет финансовых показателей портфеля акций
#
# Описание задачи:
# Вы являетесь инвестором и хотите создать программу для расчета нескольких финансовых показателей вашего
# портфеля акций. Создайте модуль Python под названием "portfolio.py",
# который будет содержать функции для выполнения следующих операций:
#
#
# Расчет общей стоимости портфеля акций: Функция calculate_portfolio_value(stocks: dict, prices: dict) -> float
# принимает два аргумента: stocks - словарь, где ключами являются символы акций (например, "AAPL" для Apple Inc.),
# и значениями - количество акций каждого символа. prices - словарь, где ключами являются символы акций,
# а значениями - текущая цена каждой акции. Функция должна вернуть общую стоимость портфеля акций на основе
# количества акций и их текущих цен. Пример: Пришло
# stocks = {"AAPL": 10, "GOOGL": 5, "MSFT": 8}
# prices = {"AAPL": 150.25, "GOOGL": 2500.75, "MSFT": 300.50}
#
# Вышло:
# 16410,25

_highest_profit: str

def calculate_portfolio_value(stocks: dict, prices: dict) -> float:
    cost = 0
    for count, price in zip(stocks.values(), prices.values()):
        cost += count * price
    return cost


# Расчет доходности портфеля: Функция calculate_portfolio_return(initial_value: float, current_value: float) -> float
# принимает два аргумента: initial_value - начальная стоимость портфеля акций. current_value -
# текущая стоимость портфеля акций. Функция должна вернуть процентную доходность портфеля. Пример:
# Пришло:
# 10000.0
# 15000.0
# Вышло:
# 50%


def calculate_portfolio_return(initial_value: float, current_value: float) -> str:
    return f'{str(round((current_value / initial_value) * 100 - 100, 2))}%'


# Определение наиболее прибыльной акции: Функция get_most_profitable_stock(stocks: dict, prices: dict) -> str
# принимает два аргумента: stocks - словарь с акциями и их количеством. prices - словарь с акциями и их текущими ценами.
# Функция должна вернуть символ акции (ключ), которая имеет наибольшую прибыль по сравнению с ее начальной стоимостью.
# Начальная стоимость - первый вызов calculate_portfolio_value,
# данные из этого вызова следует сохранить в защищенную переменную на уровне модуля.

# Пример:
# Пришло:
# stocks = {"AAPL": 10, "GOOGL": 5, "MSFT": 8}

prices = {"AAPL": 150.25, "GOOGL": 2500.75, "MSFT": 300.50}
# Вышло:
# MSFT

def get_most_profitable_stock(stocks: dict, prices_2: dict) -> str:
    dic_start, dic_end, result = {}, {}, {}
    for key, val in prices.items():
        dic_start[key] = val * stocks[key]
    for key, val in prices_2.items():
        dic_end[key] = val * stocks[key]
    for key, val in prices.items():
        result[key] = dic_end[key] - dic_start[key]
    return sorted(result.items(), key=lambda x: x[1])[-1][0]


if __name__=='__main__':
    stocks = {"AAPL": 10, "GOOGL": 5, "MSFT": 8}
    prices = {"AAPL": 150.25, "GOOGL": 2500.75, "MSFT": 300.50}
    prices_2 = {"AAPL": 155.25, "GOOGL": 2600.75, "MSFT": 800.50}
    initial_value = 12007.0
    current_value = 15000.0

    print(calculate_portfolio_value(stocks, prices))
    print(calculate_portfolio_return(initial_value, current_value))
    _highest_profit = get_most_profitable_stock(stocks, prices_2)
    print(_highest_profit)



