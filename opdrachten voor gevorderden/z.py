from re import finditer
x = [{'short': 'EcoRI','name': 'Escherichia coli','seq': 'GAATTC','offset': 1},{'short': 'EcoRII','name': 'Escherichia coli','seq': 'CCWGG','offset': 0},{'short': 'BamHI','name': 'Bacillus amyloliquefaciens','seq': 'GGATCC','offset': 1},{'short': 'HindIII','name': 'Haemophilus influenzae','seq': 'AAGCTT','offset': 1},{'short': 'NotI','name': 'Nocardia otitidis','seq': 'GCGGCCGC','offset': 2}]
for z in x:print(z['name'], '('+z['short']+')', 'sequence:'+z['seq'])
c = int(input('selecteer eiwit\n'))-1
for m in finditer(x[c]['seq'], open(input('path:\n')).read().upper()):print(x[c]['name'], m.start()+x[c]['offset'])