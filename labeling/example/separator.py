import json

f = open(input("input path to json annotation file: "), 'r')
data = json.load(f)
for filename, labeling in data.items():
    with open(labeling['filename'] + '.json', 'w') as fout:
        json.dump({filename: labeling}, fout)
f.close()