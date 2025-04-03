Beim Erstellen von komplexeren Datentypen wie Listen oder strings werden Iteratoren zurückgegeben auf das erste Element. Mithilfe von next() kann das weitere Element angegeben werden.
Beispiel:
```
l=[1,2,3,4,5,6] li=reversed(l) print(next(li)) print(next(li)) print(next(li)) 
• Ergebnis: 6, 5, 4
```
Weiteres Beispiel worin Map eine Funktion auf eine Liste anwendet:
```
li=map(round,[1.1,2.2,3.3,4.4]) print(next(li)) print(next(li)) 
• Ergebnis: 1 , 2
```

Wenn man durch eine Liste iterieren möchte, so muss man keinen Iterator benutzen, sondern kann auch "Range" benutzen
Beispiel:
```
list(range(0,5)) Ergebnis: [0, 1, 2, 3, 4]
```
```
list(range(2,8,2)) Ergebnis: [2, 4, 6]
```