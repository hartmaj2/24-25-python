# Mars rover mission solutions

## Mission 3
```py
switch = 1
rover.forward(335)
for i in range(7):
   rover.left(90*switch)
   rover.forward(48)
   rover.left(90*switch)
   switch *= -1
   rover.forward(335)
```

## Mission 4
```py
distance = 335
rover.forward(distance)
for i in range(7):
   for i in range(2):
      rover.left(90)
      rover.forward(distance)
   distance -= 48
```

## Mission 5
```py
rover.left(17)
rover.forward(230)
rover.left(45)
rover.forward(150)
rover.left(107)
rover.forward(205)
rover.left(80)
rover.forward(250)
```

## Mission 6
```py
rover.right(85)
rover.forward(340)
rover.left(100)
rover.forward(320)
rover.left(87)
rover.forward(240)
```

## Mission 7
```py
for i in range(12):
   rover.forward(92)
   rover.left(30)
```