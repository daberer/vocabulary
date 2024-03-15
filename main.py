import pandas as pd


vocabulary = {}
df = pd.read_csv("spanish_words.txt")

for i, row in df.iterrows():
    ind = input(row.words + ' ')
    if ind == 'quit':
        break
    vocabulary[row.words] = ind




print(vocabulary.items())