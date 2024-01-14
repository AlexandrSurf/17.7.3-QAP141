per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = float(input('введите сумму вклада'))
percent =  per_cent.values() 
deposit = [num*money/100 for num in percent]
print(deposit)
print('Максимальная сумма, которую вы можете заработать — ',max(deposit))