import math
class Location:
    def __init__(self,*args, **kwargs):
        self.x=0
        self.y=0
        self.z=0
        if 'x' in kwargs:
            self.x=kwargs['x']
        if 'y' in kwargs:
            self.y=kwargs['y']
        if 'z' in kwargs:
            self.z=kwargs['z']

    def __str__(self):
        return f"({self.x},{self.y},{self.z})"

    def distance(self,location2):
        r2=(self.x-location2.x)*(self.x-location2.x)+(self.y-location2.y)*(self.y-location2.y)+(self.z-location2.z)*(self.z-location2.z)
        return math.sqrt(r2)
    
class Spin:
    def __init__(self,*args, **kwargs):
        self.spin_x=0
        self.spin_y=0
        self.spin_z=0
        if 'spin_x' in kwargs:
            self.spin_x=kwargs['spin_x']
        if 'spin_y' in kwargs:
            self.spin_y=kwargs['spin_y']
        if 'spin_z' in kwargs:
            self.spin_z=kwargs['spin_z']
    def __str__(self):
        return f"({self.spin_x},{self.spin_y},{self.spin_z})"
    def auto_correlation(self,spin2):
        r=(self.spin_x*spin2.spin_x)+(self.spin_y*spin2.spin_y)+(self.spin_z*spin2.spin_z)
        return r
class Atom:
    def __init__(self,*args, **kwargs):
        self.id=0
        if 'id' in kwargs:
            self.id=kwargs['id']
        self.location=Location(*args, **kwargs)
        self.spin=Spin(*args, **kwargs)
    
    def distance(self,atom2):
        return self.location.distance(atom2.location)
    def auto_correlation(self,atom2):
        return self.spin.auto_correlation(atom2.spin)
    
    def __str__(self):
        return f"id= {self.id} ,location = {self.location} , spins = {self.spin}"