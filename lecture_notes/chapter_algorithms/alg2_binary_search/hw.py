def binary_search_loop(x, lst):
	lo = 0 
	hi = len(lst) -1 
	while lo <= hi:
		mid = (lo + hi) // 2
		if lst[mid] == x:
			return mid
		elif x < lst[mid]:
			hi = mid - 1
		else:
			lo = mid + 1
	return -1
def main():
	words = open(r'words.txt')
	input = input('What word would you like to check? ')
	lst = words.readlines().strip()
	if binary_search_loop(input.lower(), lst) != -1:
		return f'{input} IS an English word'
	else:
		return f'{input} IS NOT an English word'
main()