def main():
	text = get_book_text("./books/frankenstein.txt")
	word_count = count_words(text)	
	char_count = count_characters(text)
	print_report(word_count, char_count)

def get_book_text(path):
	with open(path) as f:
		return f.read()		
		
def count_words(text):	
	words = text.split()		
	return len(words)

def count_characters(text):
	character_count = {}
	for char in text:
		lower_char = char.lower()
		if lower_char not in character_count:
			character_count[lower_char] = 1
		else:
			character_count[lower_char] += 1

	return character_count

def print_report(word_count, char_count):
	print("--- Begin report of books/frankenstein.txt ---")
	print(f"{word_count} words found in the document")
	for key in char_count:
		if key.isalpha():
			print(f"The '{key}' character was found {char_count[key]} times")

main()