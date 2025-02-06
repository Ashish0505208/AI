import random

i={'A':"at door",'B':"at floor",'C':"at window",'D':"no banana"}

g={'A':"at middle",'B':"on box",'C':"at middle",'D':"has banana"}
array1=['grasp','move']
array2=['grasp','push','move']
array3=['grasp','push','climb']
while True:
 if i['A']=="at door" and i['B']=="at floor" and i['C']=="at window" and i['D']=="no banana":
  k=random.choice(array1)
  if k=='move':
   print(f"move({i['A']},{k},at middle)")
   i['A']="at middle"
  else:
   array1.remove('grasp')
 elif i['A']=="at middle" and i['B']=="at floor" and i['C']=="at window" and i['D']=="no banana":
  k=random.choice(array2)
  if k=='push':
   print(f"move({i['C']},{k},at middle)")
   i['C']="at middle"
  elif k=='move':
   print(f"move({i['A']},{k},at door)")
   i['A']="at door"
   array2.remove('move')
  else:
   array2.remove('grasp')
 elif i['A']=="at middle" and i['B']=="at floor" and i['C']=="at middle" and i['D']=="no banana":
  k=random.choice(array3)
  if k=='push':
   print(f"move({i['C']},{k},at window)")
   i['C']="at window"
   array3.remove('push')
  elif k=='climb':
   print(f"move({i['B']},{k},on box)")
   i['B']="on box"
  else:
   array3.remove('grasp')
 elif i['A']=="at middle" and i['B']=="on box" and i['C']=="at middle" and i['D']=="no banana":
  array=['grasp']
  k=random.choice(array)
  if k=='grasp':
   print(f"move({i['D']},{k},has banana)")
   i['D']="has banana"
  if i==g:
   break
print("Final state is",i)
