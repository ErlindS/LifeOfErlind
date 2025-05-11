# What is Numpy 
• Numpy ist eine numerische Bibliothek 
• Sie gehört nicht zum Standardumfang von Python, ist jedoch sehr populär 
• Seit 1995 in Entwicklung (noch als „Numeric“), seit 2006 als NumPy 
• Datenstruktur in Numpy ist das (NumPy)-Array

# Numpy Array
Numpy bietet ein- oder mehrdimensionale Arrays an. Diese Arrays sind auf schnelle Verarbeitung ausgelegt und können vielfältig eingesetzt werden.

Eindimensionales Array:
```
import numpy as np
x=np.array([1,2,3])
```

Mehrdimensionales Array:
```
x=np.array([1,2,3],[3,4,5])
```
Menge von Nullen oder Einsen
```
x=np.zeros(3)
x=np.zeros((2,3))
x=np.ones((2,3,4))
```
Arrays mit einer range erzeugen

```
x=np.array(range(3,8))
y=np.linspace(1,4,num=10,endpoint=True)
```

Ebenso kann man Zufallszahlen erzeugen
```
np.random.rand(10) → erzeugt 10 Zufallszahlen von 0..1 
np.random.rand(10,20)→ erzeugt eine Matrix mit 10x20 (Zeilen x Spalten) Zufallszahlen von 0..1
np.random.randint → integer Zufallszahlen
np.random.choice → Zufällige Elemente aus Array auswählen
```

Ebenso kann aus zwei 1D-Arrays ein 2D-Array erzeugen

```
xvalues = np.array([0, 1, 2, 3, 4]) 
yvalues = np.array([0, 1, 2, 3, 4]) 
xx, yy = np.meshgrid(xvalues, yvalues) 
xx Out[107]: 
array([ [0, 1, 2, 3, 4], 
		[0, 1, 2, 3, 4], 
		[0, 1, 2, 3, 4], 
		[0, 1, 2, 3, 4], 
		[0, 1, 2, 3, 4]]) 
yy 
Out[108]: 
array([ [0, 0, 0, 0, 0], 
		[1, 1, 1, 1, 1], 
		[2, 2, 2, 2, 2], 
		[3, 3, 3, 3, 3], 
		[4, 4, 4, 4, 4]])
```