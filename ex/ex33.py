# i = 0
# numbers = []
# while i < 6:
# 	print "At the top i is %d" % i
# 	numbers.append(i)
# 	i = i + 1
# 	print "Numbers now:",numbers
# 	print "At the bottom i is %d " % i
# print "The numbers:"
# for num in numbers:
# 	print num

def number_loop(a,b):
	i = 0	
	while i < a:
		print "At the top i is",i
		numbers.append(i)
		i = i + b
		print "Numbers now:",numbers
		print "At the bottom i is ",i	
def print_loop(number):
	print "The numbers:"
	for num in number:
		print num
a = input("Enter a best number :")
b = input("Enter a number incease:")
numbers = []
number_loop(a,b)
print_loop(numbers)