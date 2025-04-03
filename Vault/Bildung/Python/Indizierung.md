Listen, Tuple, Strings können indiziert werden und fangen bei 0 an.
Beispiel:
```
a="Hallo" 
l=[3,6,9] 
print(a[0]) 
print(l[1])
```
Listen, Strings, Set (keine Tupel) können verändert werden
Beispiel:
```
l=[3,6,9] 
l[1]=17 
print(l)
```
Es kann gelesen, modifiziert, aber auch angehängt werden mit append.
```
l=[] #leere Liste 
l=[1,2] #Liste mit 1,2 
l.append(3) #Liste mit 1,2,3
```
Listen können von Hinten gelesen werden.
```
l = [1,2] 
print(l[-1]) #Ergebnis 2
print(l[-2]) #Ergebnis 1
```
Mithilfe von Slicing kann man auf Teile einer Liste zugreifen indem man eine Reichweite angibt. `[ start:ende:schrittweite ]
Beispiel:
```
l=[1,2,3,4,5,6,7,8,9] 
print(l[1:3]) 
print(l[1:8:2])
```
Statts einen Doppelpunkt kann man auch slice schreiben
```
l[slice(1,8,2)]
```
weiteres Beispiel:
```
l=[[1,2,3],[4,5,6],[7,8,9]] 
print(l[1]) 
print(l[1][1:])
```