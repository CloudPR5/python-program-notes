#can you change the value inside a list which is contaained in set S?
S={8,7,12,"harry", [1,2]}

'''In Python, sets are mutable, but they cannot contain mutable elements
 like lists. This is because sets require their elements to be hashable,
   and lists are not hashable since they are mutable.

So, in your case, the set S cannot directly contain a list like [1, 2].
 If you attempt to add a list to a set, Python will raise a TypeError.

'''