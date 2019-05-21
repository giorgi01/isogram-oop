class Isogram:

	def __init__(self, filename):
		self.filename = filename

	def check(self):
		file_data = open(f'{self.filename}.txt', 'r').read()
		letters = [letter for letter in file_data]
		if len(set(letters)) == len(letters):
			print('იზოგრამია')
		else:
			print('არაა იზოგრამი')

lumberjack = Isogram('check_if')
lumberjack.check()