from p5 import *

def drawVector(Ox, Oy, V):
  # Origin x, Origin y, Vector
  line(Ox, Oy, Ox+V.x, Oy+V.y)
  push()
  noStroke()
  translate(Ox, Oy)
  rotate(V.heading())
  translate(V.mag(), 0)
  scale(sqrt(V.mag())/30)
  triangle(0, 10, 0, -10, 10, 0)
  pop()
def setup():
  createCanvas(1000,1000)
  global position, vel1, k
  position = createVector(1,1)
  k   =  -0.001
  vel1 = createVector(3,5)
  # acc1 = p5.Vector.mult(position,k)

# p5.Vector.mult(v, scalar)
# v.mult(scalar)

# define x
# (2*x)//2

def draw():
  background("black")
  translate(width/2,height/2)
  drawTickAxes()
  stroke('white')
  drawVector(0,0,position)
  fill("red")
  circle(position.x,position.y,10)
  position.add(vel1)
  acc1 = p5.Vector.mult(position,k)
  vel1.add(acc1)
# x, use velX
# y, use velY

# tuples, vectors
# x, y -> v1 (position)

# Velcoity is constant (magnitude, direction) -> acceleration is zero
