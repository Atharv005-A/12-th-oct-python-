filename = "D:/abc/sample.txt"

f = open(filename, 'r')
text = f.read()
f.close()

words = text.split()

print(f"Total words: {len(words)}")
print(words)