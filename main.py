#Read and print the file
eyes = open("sample.ini")
data = eyes.read()
print(data)
print(data.capitalize())
eyes.close()
print("---------------------------------")
#Count the words and output the amount
words = (data.split())
eyes = open("sample.ini")
counter = 0
for word in words:
    counter += 1
print(f"The total word count is {counter}")
eyes.close()
#Print the result to a txt doc
new_entry = open("counts.txt", "a")
new_entry.write(f"\nWe just did a count, the result was {counter} words in this document")
new_entry.close()
print("Log entered! Please check the counts.txt file for updates.")
