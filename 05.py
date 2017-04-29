class StringFormatter:
	def delNLines(self, string, n):
		wordslist = string.split(' ')
		for i in wordslist:
			if len(i) < n:
				wordslist.remove(i)
		return ' '.join(wordslist)
		
	def replaceNumbers(self, string):
		tempstr = string.translate(str.maketrans('0123456789', '**********'))
		return tempstr


SF = StringFormatter()
print(SF.delNLines('123 123456 1234 1234567 12345', 6))
print(SF.replaceNumbers('Кошка мыла 4 лапы и 1 морду'))