class Text:

	def __init__(self, filename):
		self.filename = filename

	def pangram_check(self):
		file_data = open(f'{self.filename}.txt', 'r').read()
		letters = [letter.lower() for letter in file_data
		if letter.isalpha()]
		if len(set(letters)) == 26:
			print('პანგრამია')
		else:
			print('არაა პანგრამი')

	def isogram_check(self):
		file_data = open(f'{self.filename}.txt', 'r').read()
		letters = [letter for letter in file_data]
		if len(set(letters)) == len(letters):
			print('იზოგრამია')
		else:
			print('არაა იზოგრამი')


our_text = Text('check_if')
our_text.pangram_check()
our_text.isogram_check()