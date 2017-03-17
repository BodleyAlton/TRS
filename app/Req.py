import math

class Client():
    def __init__(self,seat,vtype,wfactor,cid,driver,pickup,dest,name,contact):
        self.seat=seat
        self.vtype=vtype
        self.wfactor=wfactor
        self.cid=cid
        self.driver=driver
        self.pickup=pickup
        self.dest=dest
        self.name=name
        self.contact=contact

    def dist(self):
        x1= float(self.pickup[0:10])
        y1= float(self.pickup[11:])
        x2= 0
        y2= 0
        sqx= ((x2-x1)**2)
        sqy= ((y2-y1)**2)
        val=math.sqrt( sqx + sqy )
        return val

class Driver():
    def __init__(self,name,regnum,make,model,color,loc):
        self.name=name
        self.regnum=regnum
        self.make=make
        self.model=model
        self.color=color
        self.loc=loc

class Job():
    def __init__(self, c,d):
        self.driver=d
        self.client=c

    def drive(self):
        return self.driver.name
