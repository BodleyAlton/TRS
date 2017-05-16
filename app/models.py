from . import db
from flask.ext.login import UserMixin

class Clientdb(db.Model, UserMixin):
	__tablename__ = 'client'
	userCID= db.Column('userCID', db.Unicode, primary_key=True)
	cfname= db.Column('cfname', db.Unicode)
	clname= db.Column('clname', db.Unicode)
	ccontact= db.Column('ccontact', db.Integer)
	cemail= db.Column('cemail',db.Unicode, unique=True)
	cadd1=db.column('cadd1', db.Unicode)
	cadd2=db.Column('cadd2',db.Unicode)
	ccity= db.Column('city', db.Unicode)
	cparish= db.Column('parish', db.Unicode)
<<<<<<< HEAD
    
	
	def __init__(self,userCID,cfname,clname,ccontact,cemail,cpassword,cadd1,cadd2,ccity,cparish):
=======
	cstatus= db.Column('cstatus', db.Unicode)
    
	
	def __init__(self,userCID,cfname,clname,ccontact,cemail,cadd1,cadd2,ccity,cparish,cstatus):
>>>>>>> 9e73187e62be015af08a826396d91677698616db
		self.userCID= userCID
		self.cfname= cfname
		self.clname= clname
		self.ccontact= ccontact
		self.cemail= cemail
		self.cadd1=cadd1
		self.cadd2=cadd2
		self.ccity= ccity
		self.cparish= cparish
		self.cstatus= cstatus

		# def is_authenticated(self):
		# 	return True
		# def is_active(self):
		# 	return True
		# def is_anonymous(self):
		# 	return False
		# def get_id(self):
		# 	try:
		# 		return unicode(self.userCID)
		# 	except NameError:
		# 		return str(self.userCID)
		def __repr__(self):
			return '<Client %r>' % self.userCID

class Driverdb(db.Model):
	__tablename__ = 'driver'
<<<<<<< HEAD
	dID= db.Column('dID',db.Unicode, primary_key= True)
=======
	userDID= db.Column('userDID',db.Unicode, primary_key= True)
>>>>>>> 9e73187e62be015af08a826396d91677698616db
	dtrn= db.Column('dtrn', db.Integer, unique= True)
	dfname= db.Column('dfname', db.Unicode)
	dlname= db.Column('dlname', db.Unicode)
	dcontact= db.Column('dcontact',db.Integer)
	demail= db.Column('demail',db.Unicode)
	daddr1= db.Column('daddr1', db.Unicode)
	daddr2= db.Column('daddr2', db.Unicode)
	dcity= db.Column('dcity', db.Unicode)
	dparish= db.Column('dparish', db.Unicode)

<<<<<<< HEAD
	def getIdValue(did):
    		newId=''
    		newId= cid.split('d')
    		newID=int(newId[1])
    		return(newID)

	def uniqueDID(did):
    		newId=''
    		newId= did.split('d')
    		fchar= newId[0]
    		uID=int(newId[1]) + 1
    		return('d' + str(uID))



	def __init__(self,dtrn,dfname,dlname,dcontact,demail,dpassword,daddr1,daddr2,dcity,dparish):
=======


	def __init__(self,userDID,dtrn,dfname,dlname,dcontact,demail,daddr1,daddr2,dcity,dparish):
		self.userDID=userDID
>>>>>>> 9e73187e62be015af08a826396d91677698616db
		self.dtrn= dtrn
		self.dfname= dfname
		self.dlname= dlname
		self.dcontact=dcontact
		self.demail=demail
		self.daddr1 =daddr1
		self.daddr2=daddr2
		self.dcity= dcity
		self.dparish= dparish

		def __repr__(self):
			return '<Client %r>' % self.userDID


class Operatordb(db.Model):
	__tablename__ = 'operator'
<<<<<<< HEAD
	opID= db.Column('opID', db.Unicode, primary_key=True)
=======
	userOID= db.Column('userOID', db.Unicode, primary_key=True)
>>>>>>> 9e73187e62be015af08a826396d91677698616db
	ofname= db.Column('ofname', db.Unicode)
	olname= db.Column('olname', db.Unicode)
	oadd1=db.Column('oadd1',db.Unicode)
	oadd2=db.Column('oadd2',db.Unicode)
	ocity= db.Column('ocity', db.Unicode)
	oparish= db.Column('oparish', db.Unicode)
	otrn= db.Column('otrn', db.Integer)

<<<<<<< HEAD
	def getIdValue(oid):
    		newId=''
    		newId= cid.split('o')
    		newID=int(newId[1])
    		return(newID)

	def uniqueID(oid):
    		newId=''
    		newId= oid.split('o')
    		fchar= newId[0]
    		uID=int(newId[1]) + 1
    		return('o' + str(uID))


	def __init__(self,ofname,olname,oadd1,oadd2,otrn,ocity,oparish):
=======

	def __init__(self,userOID,ofname,olname,oadd1,oadd2,otrn,ocity,oparish):
		self.userOID=userOID
>>>>>>> 9e73187e62be015af08a826396d91677698616db
		self.ofname= ofname
		self.olname= olname
		self.otrn= otrn
		self.oadd1=oadd1
		self.oadd2=oadd2
		self.ocity= ocity
		self.oparish= oparish


class Vehicle(db.Model):
	__tablename__ ='vehicle'
	platenum= db.Column('platenum', db.Unicode, primary_key=True)
	vmodel= db.Column('vmodel', db.Unicode)
	vmake= db.Column('vmake', db.Unicode)
	vcolour= db.Column('vcolour', db.Unicode)
	seat_cap= db.Column('seat_cap', db.Integer)
	vclass= db.Column('class', db.Integer)

	def __init__(self,platenum,vmodel,vmake,vcolour,seat_cap,vclass):
		self.platenum= platenum
		self.vmodel= vmodel
		self.vmake= vmake
		self.vcolour= vcolour
		self.seat_cap= seat_cap
		self.vclass=vclass

class View(db.Model):		#Report that the operator would see from viewing the driver
 	__tablename__= 'views'
 	dtrn= db.Column('dtrn',db.Integer, primary_key=True)
	cid=db.Column('cid',db.Unicode, primary_key=True)
	plateNum=db.Column('plate',db.Integer,primary_key=True)
	opID=db.Column('opID',db.Integer,primary_key=True)
	job_date= db.Column('date',db.Date)
 	job_time= db.Column('time',db.Time)
 	job_status= db.Column('job_status',db.Unicode)

 	def __init__(self,dtrn,date,time,job_status):
		self.dtrn= dtrn
		self.date= date
		self.time= time
		self.job_status= job_status


class Carry(db.Model):
 	__tablename__= 'carry'
 	dtrn= db.Column('dtrn',db.Integer, primary_key=True)
 	time= db.Column('time',db.Time)
 	p_loc= db.Column('p_loc',db.Unicode) #Pick up location
 	d_loc= db.Column('d_loc',db.Unicode)	#drop off location

 	def __init__(self,dtrn,time,p_loc,d_loc):
		self.dtrn= dtrn
		self.time= time
		self.p_loc= p_loc
		self.d_loc= d_loc

class Operates(db.Model):
	__tablename__= 'operates'
 	dtrn= db.Column('dtrn', db.Integer, primary_key= True)
 	platenum= db.Column('time',db.Time, primary_key= True)

 	def __init__(self,dtrn,platenum):
		self.dtrn= dtrn
		self.platenum=platenum

class Users(db.Model):
 	__tablename__= 'users'
<<<<<<< HEAD
 	userID= db.Column('userID',db.Unicode, primary_key=True)
=======
 	id= db.Column('id',db.Unicode, primary_key=True)
>>>>>>> 9e73187e62be015af08a826396d91677698616db
 	email= db.Column('email',db.Unicode)
 	password= db.Column('password',db.Unicode) 
 	utype= db.Column('utype',db.Unicode)	

<<<<<<< HEAD
 	def __init__(self,userID,email,password,utype):
		self.userID= userID
=======
 	def __init__(self,id,email,password,utype):
		self.id= id
>>>>>>> 9e73187e62be015af08a826396d91677698616db
		self.email= email
		self.password= password
		self.utype= utype

<<<<<<< HEAD
=======
	def is_authenticated(self):
			return True
	def is_active(self):
		return True
	def is_anonymous(self):
		return False
	def get_id(self):
		try:
			return unicode(self.id)
		except NameError:
			return str(self.id)

>>>>>>> 9e73187e62be015af08a826396d91677698616db
class Driver_Location(db.Model):
 	__tablename__= 'driver_location'
 	dID= db.Column('dID',db.Unicode, primary_key=True)
 	lat= db.Column('lat',db.Float)
 	longi= db.Column('longi',db.Float) 
 	pos= db.Column('pos',db.Float)	

 	def __init__(self,userID,email,password,utype):
		self.dID= dID
		self.lat= lat
		self.longi= longi
		self.pos= pos

class IdValue(db.Model):
 	__tablename__= 'idvalue'
 	idV= db.Column('idV',db.Integer, primary_key=True)
 	cValue= db.Column('cValue',db.Integer)
 	dValue= db.Column('dValue',db.Integer) 
 	oValue= db.Column('oValue',db.Integer)	