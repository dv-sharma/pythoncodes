
def amazingnumber(str):
	vowels= 'aeiouAEIOU'
	count=0
	for index,chara in enumerate(str):
		if chara in vowels:
			count+=len(str)-index
	return count

if  __name__=='__main__':
	str='abrab'
	
	print(amazingnumber(str))
