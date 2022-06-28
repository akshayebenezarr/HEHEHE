heros=['spider man','thor','hulk','iron man','captain america']
heros.append('im')
heros.remove('im')
heros.insert(2,'black')
heros= heros[:1]+['yoloooooo']+heros[+2:]
print(dir(heros))
heros.sort(reverse=True)
print(heros)