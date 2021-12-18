# Computer asks for (x,y) coords
# Outputs a generalized parabolas equation
# Created: 30/07/20
# Author: Prabhjot Sodhi

# Variables
def parabolas():
    x = int(input("X value: "))
    y = int(input("Y value: "))
    h = int(input("H value: "))
    v = int(input("V value: "))
    yv = int(y-v)
    xh = int(x-h)

    # Output Working Out and Final Equation
    print("{} = a({}-{})^2 + {}".format(y,x,h,v))
    print("{} - {} = a({}-{})^2".format(y,v,x,h,))
    print(str(yv)+"/("+str(xh)+")^2=a")
    print("y="+str(yv)+"/("+str(xh)+")"+"^2"+"(x-"+str(h)+")^2+",str(v),"{",x,"< x <=",h,"}")

    # Output the Domain & Range
    print("Domain:",x,"< x",h)
    print("Range:",y,"< y",v)
while True:
    parabolas()
