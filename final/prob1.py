def Frequency_analytic(s) :

	dic = {}
	for char in s :
		if char in dic :
			dic[char] += 1
		else :
			dic[char] = 1
	dic2 = dict(sorted(dic.items()))
	for key, value in dic2.items() :
		if key.islower() :
			print(key, value)
	for key, value in dic2.items() :
		if key.isupper() :
			print(key, value)

if __name__ == "__main__" :
	msg = input('input your message : ')
	Frequency_analytic(msg)
