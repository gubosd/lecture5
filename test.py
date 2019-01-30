l = ['1','2','three',4,5]
s = 0
for i in l:
	try:
		s += int(i)
		print(int(i))
	except:
		print('error... %s' % i)

print(s)