def generaPares(limite):
	
	num=1

	while num<limite:

		yield num*2

		num=num+1

devuelvepares=generaPares(10)

print(next(devuelvepares))

print("mas codigo")

print(next(devuelvepares))

print("mas codigo")

print(next(devuelvepares))

print("mas codigo")