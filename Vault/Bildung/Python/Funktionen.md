Was geht
```
def test():
	return 42,43

test()[42]

a=test
a()
```

Funktionen können ebenso vordefinierte Parameter haben

```
def test(a,b=42):
	print("a=",a)
	print("b=",b)

test(12) 
test(12,33) 
test(12,b=33)
test(a=13, b=44)
```

Manche Funktionen unterstützen auch vordefinierte Keyword-Parameter. Alle zusätzliche Parameter werden in ein Dictionary gepackt
```
def test(a,b=42, **kwargs): 
	print("a=",a) 
	print("b=",b) 
	if len(kwargs)>0: 
		if "c" in kwargs: 
			print("c=",kwargs["c"]) 
	print('kwargs (dictionary):',kwargs) 
	
test(12) → a=12,b=42 
test(12,33) → a=12, b=33 
test(12,b=33) → a=12, b=33 
test(12,33,c=43) → a=12, b=33, c=43, kwargs (dictionary): {'c': 43} 
test(12,33,c=43,d=99) → a=12, b=33, c=43, kwargs (dictionary): {'c': 43, 'd': 99}
```
Es gibt nicht nur ** kwargs sondern auch * args
```
def test2(*args, **kwargs): 
	print("args=",args) 
	print("kwargs=",kwargs) 
	
test2(3) → args= (3,); kwargs= {} 
test2(3,5) → args= (3,5); kwargs= {} 
test2(3,b=5,c=42) → args= (3,); kwargs= {'b': 5, 'c': 42}
```
Der Unterschied zwischen args und kwargs ist das Variable mit Keywords in das Kwargs in einem Dictonary vorkommen

Ebenso existieren Lambda-Funktionen. Man setzt Lambda-Funktionen ein wo es "schnell" gehen soll.
(Wozu werden diese eingesetzt?)

```
miau=lambda: print("miau") 
miau()
```

Ebenso existieren Lambdas mit Parameter
```
miau=lambda x: print(x) 
miau("miaumiau")
```