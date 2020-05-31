def read_file(file):
    with open(file, 'r') as f:
        return [l.strip() for l in f.readlines()]


def gc_content(seq):
    return round((seq.count('C') + seq.count('G')) / len(seq) * 100)


FASTAFile = read_file("test_data\gc_content_ex.txt")
# Dictionary for Labels + Data
FASTADict = {}
# String for holding the current label
FASTALabel = ""

print('FASTAFile: ')
print(FASTAFile, '\n')


for line in FASTAFile:
    if '>' in line:
        FASTALabel = line
        FASTADict[FASTALabel] = ""
    else:
        FASTADict[FASTALabel] += line

print('RESULTDict: ')
RESULTDict = {key: gc_content(value) for (key, value) in FASTADict.items()}
print(RESULTDict)
print('\n')

MaxGCKey = max(RESULTDict, key=RESULTDict.get)
print(MaxGCKey)
print('\n')

print(f'{MaxGCKey[1:]}\n{RESULTDict[MaxGCKey]}')
