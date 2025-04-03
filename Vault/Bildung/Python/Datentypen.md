In Python sind Datentypen implizit. Das heißt diese müssen nicht explizit angegeben werden. 

Man kann Zahlen in Variablen speichern
```
	A = -3
	A = 3.14
	A = 3+5j 
```
Ebenso können Strings in Variablen gespeichert werden. Der letzte Ausdruck erzeugt einen String mit dem Wert von A. Dies wird als F String betitelt.
```
	B = "Hallo Welt"
	b = f"Folgender Wert steckt in a: {a}"
``` 
In Booleans kann der Wert Wahr oder Flasch zugewiesen werden:
```
a=True
a=False
```
In Listen können unterschiedliche Zahlen und Datentypen gespeichert werden, sogar gemischte Datentypen, einschließlich Listen:
```
a=[1,2,3,4,5]
a=["a","test","b"]
a=[3.14,"test",-3,True]
a=[3.14,["test",1,-1],-3, True]
```
In Tupeln können ebenso unterschiedliche Werte abgespeichert werden. Diese sind aber immutable. Das heißt nicht veränderbar.

```
a=(3.14,"test",-3, True)
```
In einem Set können ebenso Daten abgespeichert werden. Der Unterschied zu einer List besteht darin, dass die Werte nur einmal vorkommen können wie in einer "Menge".
```
a={'a','b','c',1,2,3}
```
Ein Dictionary ist ein Paar aus einem Schlüssel und einem Wert
```
a={"Wert":23,42:"Antwort","Liste":[1,2,3]}
```
Ebenso muss kein Wert zugewiesen werden
```
a= None
```
Mithilfe den folgenden Zeilen Code kann man sich ein File-Objekt erzeugen.

```
f = open("file.txt", "w")
f.write("Text in File speichern")
f.close()
```
Wenn man sich den Datentyp abfragen möchte, so kann man das mit type() machen.
```
a=5
type(a)
-> int
```

Es existieren optionale Deklaration seit Version 3.5 
```
alter:int
alter=5
alter="test"
```
In diesem Beispiel ist die Zuweisung von "test" kein Fehler, aber der Typechecker würde etwas anmerken.
Zudem kann man den Rückgabetyp von Funktionen mithilfe eines Pfeiles definieren:
```
def f(x:int)->int:
	return x+3
```

