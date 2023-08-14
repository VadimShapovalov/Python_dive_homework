# Тестирование модуля:
# Напишите небольшую программу, которая импортирует модуль "portfolio.py" и демонстрирует использование всех трех функций.
# Создайте словари для акций и цен, запустите функции и выведите результаты.

from seminar_6.portfolio import calculate_portfolio_value, calculate_portfolio_return, get_most_profitable_stock

stocks = {"AAPL": 10, "GOOGL": 5, "MSFT": 8}
prices = {"AAPL": 150.25, "GOOGL": 2500.75, "MSFT": 300.50}
prices_2 = {"AAPL": 155.25, "GOOGL": 2600.75, "MSFT": 800.50}
initial_value = 12007.0
current_value = 15000.0

print(calculate_portfolio_value(stocks, prices))
print(calculate_portfolio_return(initial_value, current_value))
print(get_most_profitable_stock(stocks, prices_2))