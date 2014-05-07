import json, sys, os.path

#put words into dict with sorted word as key
def initialize(word_list_file, dict_json_file):
	table = {}

	#if dictionary has previously been written to filesystem, load json file
	if os.path.isfile(dict_json_file):
		with open(dict_json_file) as data_file:
			return json.load(data_file)

	#load words from file into list
	with open(word_list_file) as f:
		lst = [line.rstrip() for line in f]

	#put words in dictionary, where key is sorted word
	for word in lst:
		sorted_word = ''.join(sorted(word))
		if sorted_word not in table:
			table[sorted_word] = []
		table[sorted_word].append(word)

	#save dictionary to file system
	with open(dict_json_file, 'w') as f: f.write(json.dumps(table))
	return table

#search table for list of valid words
def unjumble(word, table):
	key = ''.join(sorted(word))
	if key in table.iterkeys():
		return table[''.join(sorted(word))]
	else:
		return []

def main():
	dct = initialize('words.txt', 'dictionary.json')

	while (True):
		print 'Enter a word. Type "exit" to exit.'
		input = raw_input()
		if (input.lower() == 'exit'):
			break

		result = unjumble(input ,dct)
		print "Found the following matches:" if result else "No words found."
		for word in result:
			print word

if __name__ == "__main__":
    sys.exit(main())