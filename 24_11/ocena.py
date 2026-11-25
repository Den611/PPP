def sprawdzenie(liczba, wyl):
    wylosowana=wyl.copy()
    porown=[]
    for i in range(len(wylosowana)):
        if liczba[i]==wylosowana[i]:
            porown.append('+')
            wylosowana[i]=None
            przesuniecie+=1
        else:
            porown.append('-')
    for i in range(len(wylosowana)):
        if porown[i]=='-' and liczba[i] in wylosowana:
            wylosowana[wylosowana.index(liczba[i])]=None
            porown[i]='/'
    return porown