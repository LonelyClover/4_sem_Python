args = input().split(' ')
amount = int(args[0])
period_month = int(args[1]) * 12
rate_month = float(args[2]) / 12.0 / 100.0

with open('output.csv', 'w') as f:
	print("Месяц,Сумма на вкладе,Начисление", file=f)
	for i in range(period_month):
		income = amount * rate_month
		amount += income
		print(f"{i + 1},{amount:0.2f},{income:0.2f}", file=f)
