from pylab import∗
from scipy.integrate import odeint
from s ci p y.optimize import brentq
import sys

##########################################################

#function definition
#def V(x):
  #Potential in which the particle exists.
#  L=1
 # if x<1.0:
  #  return 0  #square well
#  else:
 #   return v0
# We can then define the ODE for solution with odeint():
#def SE(y,x):
 # g0 = y [ 1 ]
 # g1 = 2.0∗(V(x)−E)∗y[0]
 # return array ([g0, g1])

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
#Calculates psi for this value of E , and
#returns the value of psi at point b to c heck divergence .
#####################################
  global y
  global E
  E = energy
  y = odeint(SE, yo, x )
  return y[−1, 0]                     # returnfinal value(psi at b)
y = zeros ([steps ,2])
yo = array([1.0 , 0.0])       # i n i t i a l p s i and p s i−d o t .
x = linspace(0, b ,steps)
E1 = float(sys.argv[ 1 ])
E2 = float(sys.argv[ 2 ])
answer = brentq( Final_Value, E1, E2 )     # use brentq to solve for E−> psi=0 at b.

print("Eigenvalue found at E = %.8 f" % answer)
plot(x , y[ : , 0 ])
xlabel(" Position(Units of L) ")
show()
  
    
