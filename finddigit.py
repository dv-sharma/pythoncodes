import re
def finddigit(str):
	digit_list=[]
	for word in str.split():
		if word.isdigit():
			digit_list.append(word)
	return digit_list
def finddigitdecimal(str):
	finalstr=re.findall('\d*\.?\d+',str)
	return finalstr
			
		
	



if  __name__=='__main__':
	str='Nancy is 90 years old. She wants 120 toffees.'
	print(finddigit(str))
	print(finddigitdecimal(str))