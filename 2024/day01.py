import pandas as pd

# Part 1
input = r"C:\Users\kunfu\OneDrive\Documents\input.txt"
df =  pd.read_csv(input, header=None, sep='  ', engine = 'python')

df.columns = ['col1','col2']

sorted_col1 = df['col1'].sort_values(ascending=True).reset_index(drop=True)
sorted_col2 = df['col2'].sort_values(ascending=True).reset_index(drop=True)

sorted_df = pd.DataFrame({'col1':sorted_col1, 'col2':sorted_col2})

difference = (sorted_df['col1'] - sorted_df['col2']).abs()
print("Part 1:", difference.sum())

# Part 2
sum = 0
for i in df['col1']:
    count_col2 = df['col2'].value_counts().get(i, 0)
    sum += i * count_col2

print("Part 2:", sum)

