# 4. Написать свой модуль utils и перенести в него функцию currency_rates() из предыдущего задания. Создать скрипт,
# в котором импортировать этот модуль и выполнить несколько вызовов функции currency_rates(). Убедиться, что ничего
# лишнего не происходит.
# ---------Решение------------------


from GeekBrainsLesson_4_2_and_4_3 import currency_rates
# я не стал создавать модуль utils поскольку модуль уже создан и называется он GeekBrainsLesson_4_2_and_4_3
# выполняем несколько вызовов функции currency_rates() в цикле.
# Убеждаемся, что ничего лишнего не происходит.
currency_list = ('AUD', 'GBP', 'AMD', 'USH')
for currency in currency_list:
    rate = currency_rates(currency)
    print(currency, rate[0], rate[1])
