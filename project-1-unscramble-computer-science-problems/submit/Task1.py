"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

telephones = set()
all_records = zip(texts, calls)

for text, call in all_records:
    for i in range(0, 2):
        telephones.update(text[i])
        telephones.update(call[i])

print(f"There are {len(telephones)} different telephone numbers in the records.")
