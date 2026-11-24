def sprawdzenie(liczba, wylosowana):
    przesuniecie=0
    porown=[]

    for i in range(len(wylosowana)):
        if liczba[i]==wylosowana[i-przesuniecie]:
            porown.append('+')
            wylosowana.pop(i-przesuniecie)
            przesuniecie+=1
        else:
            porown.append('-')
    przesuniecie2=0
    for i in range(len(porown)):
        if porown[i]=='F':
            for j in range(len(wylosowana)):
                if liczba[i]==wylosowana[j-przesuniecie2]:
                    wylosowana.pop(j-przesuniecie2)
                    przesuniecie2+=1
                    porown[i]='/'
    return porown