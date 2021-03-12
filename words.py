x = 0
listgood = []

with open("words.txt") as file:
  lines = [i.strip() for i in file]

for i in lines:
    if "STRING" in lines[x]:
        listgood.append(lines[x])
    x += 1

# make array into string, optional
listgoodstr = ' '.join([str(elem) for elem in listgood]) 

print(listgoodstr)
