class Pangram:

	def __init__(self, filename):
		self.filename = filename

	def check(self):
		file_data = open(f'{self.filename}.txt', 'r').read()
		letters = [letter.lower() for letter in file_data
		if letter.isalpha()]
		if len(set(letters)) == 26:
			print('პანგრამია')
		else:
			print('არაა პანგრამი')


pangram = Pangram('check_if')
pangram.check()