list0 = [{"to": "jest", "pierwszy": "slownik"}, {"a": "to", "juz": "drugi"}]

output = ""

for i in list0:
    for p in i:
        output = output + "_" + p + "_" + i[p]

print(output.replace("_", " "))
