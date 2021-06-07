from app.models import Atom,Location,Spin
R_MIN=0
R_MAX=50


atom1=Atom(id=1,x=0,y=0,z=0,spin_x=3,spin_y=4,spin_z=1)
atom2=Atom(id=2,x=12,y=4,z=3,spin_x=1,spin_y=2,spin_z=3)

print(atom1)
print(atom2)
print(f'distanse : {atom1.distance(atom2)}')
print(f'  scalar : {atom1.auto_correlation(atom2)}')

# output
# id= 1 ,location = (0,0,0) , spins = (3,4,1)
# id= 2 ,location = (12,4,3) , spins = (1,2,3)
# distanse : 13.0
#   scalar : 14
