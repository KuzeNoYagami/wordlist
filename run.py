input_text = "ade"  # Replace "your input text" with your actual input text
wordlist = []
for i in range(1, 20001):
    wordlist.append(input_text + str(i))
with open("result.txt", "w") as file:
    file.write("\n".join(wordlist))
print("Wordlist created and saved to result.txt.")