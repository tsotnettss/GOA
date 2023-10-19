from turtle import *
speed (100)
width (7)
#house square
color("green")
forward (200)
left (90)

forward (200)
left (90)

forward (200)
left (90)

forward (200)
left (90)

forward (70)

#dor
begin_fill()
color ("orange")
left (90)
forward (120)
right (90)
forward (60)
right (90)
forward (120)
end_fill()

penup()
#house roof
goto(200, 200)
pendown ()

begin_fill ()
color ("red")
right(150)
forward( 200)
left (120)
forward(200)
end_fill ()

penup()
goto (15,50)
pendown()
 
#left window
begin_fill ()
left (120)
forward(40)

left(90)
forward (60)

left (90)
forward(40)

left (90)
forward (60)
end_fill ()



penup()
#right window
goto (185, 50)
pendown ()
begin_fill ()
right (90)
forward (40)

right (90)
forward (60)

right (90)
forward (40)
right (90)
forward (60)
end_fill ()
penup ()


goto(-1000,0)
pendown()
#meadow
color ("green")
begin_fill ()
left(90)
forward (2000)

right(90)
forward(500)
right(90)
forward(2000)
right(90)
forward(500)
end_fill ()



#tree1
penup ()
goto(-250,0)
width(12)
color ("brown")
pendown()
forward(50)

color ("green")
begin_fill ()
right(90)
forward(60)

left (110)
forward(180)

left(140)
forward(180)

left (110)
forward(60)
end_fill ()

penup()

#tree2

goto(350,0)
width(12)
color ("brown")
pendown()
left (90)
forward(50)

color ("green")
begin_fill ()
right(90)
forward(60)

left (110)
forward(180)

left(140)
forward(180)

left (110)
forward(60)
end_fill ()

penup()

#tree3

goto(-385,0)
width(12)
color ("brown")
pendown()
left (90)
forward(50)

color ("green")
begin_fill ()
right(90)
forward(60)

left (110)
forward(180)

left(140)
forward(180)

left (110)
forward(60)
end_fill ()
penup()

#cloud1

color ("blue")
goto(-450, 350)
pendown()
begin_fill ()
forward (40)

right(90)
forward(30)

left(90)
forward(50)

left(90)
forward(40)

right(90)
forward(60)

right(90)
forward (30)

left(90)
forward(40)

left(90)
forward(30)

right(90)
forward(30)

left(90)
forward(40)

left(90)
forward (70)

right(90)
forward (30)

left (90)
forward(70)

left(90)
forward (35)

right (90)
forward (40)

right(90)
forward(15)

left(90)
forward(30)

left(90)
forward(15)

right(90)
forward(10)

left(90)
forward(40)
end_fill()

penup()

#cloud2

color ("blue")
goto(350, 350)
pendown()
begin_fill ()
left(90)
forward (40)

right(90)
forward(30)

left(90)
forward(50)

left(90)
forward(40)

right(90)
forward(60)

right(90)
forward (30)

left(90)
forward(40)

left(90)
forward(30)

right(90)
forward(30)

left(90)
forward(40)

left(90)
forward (70)

right(90)
forward (30)

left (90)
forward(70)

left(90)
forward (35)

right (90)
forward (40)

right(90)
forward(15)

left(90)
forward(30)

left(90)
forward(15)

right(90)
forward(10)

left(90)
forward(40)

end_fill()
penup()
#car
#tyre1
color("black")
begin_fill()
goto(-450, -250)
pendown()

left (90)
forward(10)


left (30)
forward(10)
left (30)
forward(10)
left (30)
forward(10)
left (30)
forward(10)
left (30)
forward(10)
left (30)
forward(10)
left (30)
forward(10)
left (30)
forward(10)
left (30)
forward(10)
left (30)
forward(10)
left (30)
forward(10)

end_fill()
penup()

#tyre1

color("black")
begin_fill()
goto(-150, -245)
pendown()

left (90)
forward(10)


left (30)
forward(10)
left (30)
forward(10)
left (30)
forward(10)
left (30)
forward(10)
left (30)
forward(10)
left (30)
forward(10)
left (30)
forward(10)
left (30)
forward(10)
left (30)
forward(10)
left (30)
forward(10)
left (30)
forward(10)

end_fill()
penup()

#Car body

goto(-420, -220)
pendown()
begin_fill()
right(30)
forward(340)

left(90)
forward (45)

left(80)
forward(120)

right (35)
forward (45)

left(45)
forward(140)

left(25)
forward(70)

right(20)
forward(50)

left(83)
forward(60)

left(90)
forward(20)
penup()
end_fill ()


exitonclick ()

