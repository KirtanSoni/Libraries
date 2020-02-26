import math
from vec import Vec3


"""self made class/incomplete"""


class Quat:
    def __init__(self, w : float or 'Vec3' or 'Quat'  = 0,x :float = 0  , y: float = 0 ,z: float = 0 ):
        
        if hasattr(w, 'w'):
            # We have been given a vector. Copy it
            self.w = float(w.w)
            self.x = float(w.x) if hasattr(w, 'x') else 0
            self.y = float(w.y) if hasattr(w, 'y') else 0
            self.z = float(w.z) if hasattr(w, 'z') else 0
        else :
            if hasattr(w, 'x'): #vector and angle(rads) approach
                w=w.normalized()
                self.w = math.cos(x/2)*float(x)
                self.x = math.sin(x/2)*float(w.x) if hasattr(w, 'x') else 0
                self.y = math.sin(x/2)*float(w.y) if hasattr(w, 'y') else 0
                self.z = math.sin(x/2)*float(w.z) if hasattr(w, 'z') else 0
            else:
                self.w = float(w)
                self.x = float(x)
                self.y = float(y)
                self.z = float(z)

    def Vec_2_quat(self,other:'Vec3')->'Quat': #returns quat from vec3 with w = 0 
        return Quat( 0 , other.x , other.y , other.z)
    
    def __add__(self, other: 'Quat') -> 'Quat':
        return Quat( self.w + other.w ,self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other: 'Quat') -> 'Quat':
        return Quat(self.w - other.w, self.x - other.x, self.y - other.y, self.z - other.z)

    def __neg__(self):
        return Quat(-self.w,-self.x, -self.y, -self.z)
    
    def __invert__(self)->'Quat':
        return Quat(self.w , -self.x , -self.y , -self.z)
    
    def __mul__(self,other: 'Quat') -> 'Quat':
        return Quat( self.w*other.w   -  self.x*other.x  -  self.y*other.y  -  self.z*other.z, 
                     self.w*other.x   +  self.x*other.w  +  self.y*other.z  -  self.z*other.y, 
                     self.w*other.y   -  self.x*other.z  +  self.y*other.w  +  self.z*other.x,
                     self.w*other.z   +  self.x*other.y  -  self.y*other.x+    self.z*other.w)
    
    def Eular_to_Quat(self,pitch,yaw,roll)->'Quat':
        x = math.sin(roll/2) * math.cos(pitch/2) * math.cos(yaw/2) - math.cos(roll/2) * math.sin(pitch/2) * math.sin(yaw/2)
        y = math.cos(roll/2) * math.sin(pitch/2) * math.cos(yaw/2) + math.sin(roll/2) * math.cos(pitch/2) * math.sin(yaw/2)
        z = math.cos(roll/2) * math.cos(pitch/2) * math.sin(yaw/2) - math.sin(roll/2) * math.sin(pitch/2) * math.cos(yaw/2)
        w = math.cos(roll/2) * math.cos(pitch/2) * math.cos(yaw/2) + math.sin(roll/2) * math.sin(pitch/2) * math.sin(yaw/2)

        return Quat( w , x, y, z)
    
    def Quat_to_Eular(self)-> float :
        t0 = +2.0 * (self.w * self.x + self.y * self.z)
        t1 = +1.0 - 2.0 * (self.x * self.x + self.y * self.y)
        X = (math.atan2(t0, t1))

        t2 = +2.0 * (self.w * self.y - self.z * self. x)
        t2 = +1.0 if t2 > +1.0 else t2
        t2 = -1.0 if t2 < -1.0 else t2
        Y =(math.asin(t2))

        t3 = +2.0 * (self.w * self.z + self.x * self.y)
        t4 = +1.0 - 2.0 * (self.y * self.y + self.z * self.z)
        Z = (math.atan2(t3, t4))

        return X, Y, Z
