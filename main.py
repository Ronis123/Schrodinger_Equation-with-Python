from pylab import∗
from scipy.integrate import odeint
from s ci p y.optimize import brentq
import sys

##########################################################

#function definition
def V(x):
  #Potential in which the particle exists.
  L=1
  if x<1.0:
    return 0  #square well
  else:
    return v0
# We can then define the ODE for solution with odeint():
def SE(y,x):
  
#Returns derivs for the 1−D TISE, for use in odeint.
#Requires global value E to be set elsewhere .
#Note that we are using x as time here . . . Python doesn’t care !

  g0 = y [ 1 ]
  g1 = 2.0∗(V(x)−E)∗y[0]
  return array ([g0, g1])

  ############################################################

b = 2.0
Vo = 20.0     # Potential outsid e square well
steps = 100
E = 0.0       # global variable , changed by Final Value( )
def V( x ):
###############################
#Potential in which the particle exists .
  L = 1
###############################
if x <1.0:
  return 0     # square well
else:
  return Vo

def SE(y,x):
##################################  
#Returns derivs for the 1−D TISE, for use in odeint.
#Requires global value E to be set elsewhere .
#Note that we are using x as time here . . . Python doesn’t care !
####################################
  g0 = y[1]
  g1 = −2.0∗(E−V(x))∗y[0]
  return array([g0, g1])
def Final Value (energy):
###################################
#C a l c u l a t e s p s i f o r t h i s v a l u e o f E , and
#r e t u r n s t h e v a l u e o f p s i a t p o i n t b t o c heck d i v e r g e n c e .
#####################################
g loba l y
g loba l E
E = ene r gy
y = o d ei n t (SE , yo , x )
return y[ −1 , 0 ] # r e t u r n f i n a l v a l u e ( p s i a t b )
y = z e r o s ( [ s t e p s , 2 ] )
yo = a r r a y ( [ 1 . 0 , 0 . 0 ] ) # i n i t i a l p s i and p s i−d o t .
x = l i n s p a c e ( 0 , b , s t e p s )
E1 = f l o a t ( s y s . argv [ 1 ] )
E2 = f l o a t ( s y s . argv [ 2 ] )
answer = b ren tq ( Fi n al V al u e , E1 , E2 ) # use b r e n t q t o s o l v e f o r E−> p s i=0 a t b .

pr int ’ Ei g e n v al u e found a t E = %.8 f ’ % answer
pl o t ( x , y [ : , 0 ] )
x l a b e l ( ” P o si ti o n ( Uni t s o f L) ” )
show ( )
  
    
