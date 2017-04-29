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
	
	def addSpaces(self, string):
		#Здравствуйте, здравствуйте дорогие друзья
		#В эфире радио "Щиткод FM" и наша постоянная передача
		#Костыль FM. И сегодня мы с вами будем бегать циклом по строке
		#Зато работает
		tempstr = ''
		for i in string:
			if not i == ' ':
				tempstr += i + ' '
		return tempstr
		
	def sortByLenght(self, string):
		def SBL(str):
			return len(str)
		templst = string.split(' ')
		templst.sort(key=SBL)
		return ' '.join(templst)
		


SF = StringFormatter()
print(SF.delNLines('123 123456 1234 1234567 12345', 5))
print(SF.replaceNumbers('Кошка мыла 4 лапы и 1 морду'))
print(SF.addSpaces('Hello, mister Anderson'))
print(SF.sortByLenght('Привет, я Дед Лайн, и я пришёл, чтобы забрать у тебя твою бесполезную жизнь'))