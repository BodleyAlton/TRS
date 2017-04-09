from app import app,db,login_manager
from flask import render_template, request, redirect, url_for, jsonify,flash
from forms import *
from flask_sse import sse
from models import *
from flask_login import LoginManager
from flask_login import login_user, logout_user, current_user, login_required
from Req import *
from sqlalchemy.sql import select
from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root@localhost/trs', echo=True)

def getCIdValue(cid):
    newId=''
    newId= cid.split('c')
    newID=int(newId[1])+ 1
    return(newID)

def uniqueCID(cid):
    return('c' + str(cid))



def getDIdValue(did):
    newId=''
    newId= did.split('d')
    newID=int(newId[1])+ 1
    return(newID)

def uniqueDID(did):
    return('d' + str(did))



def getOIdValue(oid):
    newId=''
    newId= oid.split('o')
    newID=int(newId[1])+ 1
    return(newID)

def uniqueOID(oid):
    return('o' + str(oid))

# engine = create_engine('mysql+pymysql://root@localhost/trs', echo=True)
pickup=''
dest=''
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ))
@app.route('/')
#@login_required
def home():
    return render_template('home.html')

@app.route('/map/new_request')
@login_required
def new_request():    
    return render_template('map.html')

@app.route('/add-client', methods=['POST','GET'])
def add_client():
    cform=clientForm()
    if request.method=='POST':
        if cform.validate_on_submit():
            prevID=db.engine.execute('select cValue from idValue')
            for pID in prevID:
                oldID= pID['cValue']
            specialID=uniqueCID(oldID)
            specIdValue=getCIdValue(specialID)
            cfname=cform.cfname.data
            clname=cform.clname.data
            ccontact=cform.ccontact.data
            cemail=cform.cemail.data
            cpassword=cform.cpassword.data
            cadd1=cform.cadd1.data
            cadd2=cform.cadd2.data
            ccity=cform.ccity.data
            cparish=cform.cparish.data
            usertype="client"
            cstatus="active"
            client= Clientdb(specialID,cfname,clname,ccontact,cemail,cadd1,cadd2,ccity,cparish,cstatus)
            db.session.add(client)
            db.session.commit()
            db.engine.execute('update idValue set cValue=' + str(specIdValue))
            db.session.commit()
            user=Users(specialID,cemail,cpassword,usertype)
            db.session.add(user)
            db.session.commit()
            flash('User added sucessfully','success')
            return redirect (url_for('home'))
    flash_errors(cform)
    return render_template('add_client.html',form=cform)

@app.route('/add-driver', methods=['POST','GET'])
def add_driver():
    dform=driverForm()
    if request.method=='POST':
        if dform.validate_on_submit():
            prevDID=db.engine.execute('select dValue from idValue')
            for pDID in prevDID:
                oldDID= pDID['dValue']
            specialDID=uniqueDID(oldDID)
            specDIdValue=getDIdValue(specialDID)
            dfname=dform.dfname.data
            dlname=dform.dlname.data
            dcontact=dform.dcontact.data
            demail=dform.demail.data
            dpassword=dform.dpassword.data
            dadd1=dform.dadd1.data
            dadd2=dform.dadd2.data
            dcity=dform.dcity.data
            dparish=dform.dparish.data
            dtrn=dform.dtrn.data
            usertype="driver"
            driver= Driverdb(specialDID,dtrn,dfname,dlname,dcontact,demail,dadd1,dadd2,dcity,dparish)
            db.session.add(driver)
            db.session.commit()
            db.engine.execute('update idValue set dValue=' + str(specDIdValue))
            db.session.commit()
            user=Users(specialDID,demail,dpassword,usertype)
            db.session.add(user)
            db.session.commit()
            flash('User added sucessfully','success')
            return redirect (url_for('home'))
    flash_errors(dform)
    return render_template('add_driver.html',form=dform)

@app.route('/add-operator', methods=['POST','GET'])
def add_operator():
    oform=operatorForm()
    if request.method=='POST':
        if oform.validate_on_submit():
            ofname=oform.ofname.data
            olname=oform.olname.data
            oadd1=oform.oadd1.data
            oadd2=oform.oadd2.data
            ocity=oform.ocity.data
            oparish=oform.oparish.data
            oemail=oform.oemail.data
            opassword=oform.opassword.data
            otrn=oform.otrn.data
            usertype="operator"
            prevOID=db.engine.execute('select oValue from idValue')
            for pOID in prevOID:
                oldOID= pOID['oValue']
            specialOID=uniqueOID(oldOID)
            specOIdValue=getOIdValue(specialOID)
            operator= Operatordb(specialOID,ofname,olname,oadd1,oadd2,ocity,oparish,otrn)
            db.session.add(operator)
            db.session.commit()
            db.engine.execute('update idValue set oValue=' + str(specOIdValue))
            db.session.commit()
            user=Users(specialOID,oemail,opassword,usertype)
            db.session.add(user)
            db.session.commit()
            flash('User added sucessfully','success')
            return redirect (url_for('home'))
    flash_errors(oform)
    return render_template('add_operator.html',form=oform)

@app.route('/add-vehicle', methods=['POST','GET'])
def add_vehicle():
    vform=vehicleForm()
    if request.method=='POST':
        if vform.validate_on_submit():
            platenum=vform.platenum.data
            vmodel=vform.vmodel.data
            vmake=vform.vmake.data
            vcolour=vform.vcolour.data
            seat_cap=vform.seat_cap.data
            vclass=vform.vclass.data
            vehicle= Vehicle(platenum,vmodel,vmake,vcolour,seat_cap,vclass)
            db.session.add(vehicle)
            db.session.commit()
            flash('User added sucessfully','success')
            return redirect (url_for('home'))
    flash_errors(vform)
    return render_template('add_vehicle.html',form=vform)

@app.route('/login',methods=['POST','GET'])
def login():
    lform=LoginForm()
    if request.method=='POST':
        if lform.validate_on_submit():
            un = lform.username.data
            pw = lform.password.data
            print un
            print pw;
            userr = Users.query.filter_by(email=un,password = pw).first()
            print userr;
            login_user(userr)
            # if current_user.id[0]=="D":
                #push id to javascript
            #return redirect(url_for ('new_request'))
            print "Loged In"
            next=request.args.get('next')
            # if not is_safe_url(next):
            #     return abort(400)
            # return redirect(next or url_for('home'))
        else:
            print 'FAIL'
            #if statement to validate which template to render
            # if current_user.id[0]=='C':
            #     return render_template('')
    return render_template('login.html',form=lform)

@login_manager.user_loader
def load_user(id):
    return Users.query.get(id)

@app.route("/logout")
@login_required
def logout():
    # Logout the user and end the session
    logout_user()
    flash('You have been logged out.', 'danger')
    return redirect(url_for('login'))

@app.route("/request", methods=["POST","GET"])
def request_cab():
    if request.method=="POST":
        seat = request.form['seat']
        vtype= request.form['vehicle']
        wfactor= request.form['wfac']
        driver= request.form['dname']
        cid = current_user.id
        global pickup
        pickup= request.form['pickup']
        global dest
        dest= request.form['dest']
        fNResult= db.engine.execute("select cfname from client where userCID= %s", cid)
        lNResult= db.engine.execute('select clname from client where userCID= %s',cid)
        cResult= db.engine.execute('select ccontact from client where userCID= %s',cid)
        for fname in fNResult:
            fname = fname['cfname']
        for lname in lNResult:
            lname = lname['clname']
        for contact in cResult:
            contact = contact['ccontact']
        global creq
        creq=Client(seat,vtype,wfactor,cid,driver,pickup,dest,fname,lname,contact)
        print "SEAT: "+ str(creq.seat)
        print "TYPE: "+ creq.vtype
        print "FACTOR: "+creq.wfactor
        print "ID: "+ str(creq.cid)
        print "DRIVER: "+creq.driver
        print "PICK UP: "+creq.pickup
        print "DEST:"+creq.dest
        print "FNAME: "+ creq.fname
        print "LNAME: "+ creq.lname
        print "CONTACT: "+ str(creq.contact)
        print "DIST: "+ str(creq.dist())
        cdist=creq.dist()
        alist=getDrivers(seat,vtype,driver,cdist)
        print "REQUEST ROUTE"
        return alist
        # return creq.dest() #consider making a global variable and pass to function responsible for p.queue

def getDrivers(seat,vtype,driver,cdist):
    drivers=[]
    pdrivers=[]
    i=0
    j=0
    if driver != '':
        print driver #driver= Put query here using driver(return name,platereg,make,model and color of vchl){Zaavan}
    #drivers=  #query ID and pos
    drivers=[[123,6],[456,10],[789,7.5],[3412,7],[345,7.67],[678,1],[901,4],[234,5],[567,3],[890,2],[4794,15],[54536,11],[5773,14],[47789,12],[7540,13]] #List produced by database query
    sdrivers=sorted(drivers,key=getKey)
    print sdrivers
    #cpos=binary_search(sdrivers, cdist, 0, len(sdrivers)-1)
    cpos=5 #stub
    print "CPOS"
    print cpos
    j=cpos
    x=cpos+1
    while j > (cpos-5) and j != 0:
        pdrivers.append(sdrivers[j])
        j-=1

    while x < (cpos+6) and x != len(sdrivers):
        pdrivers.append(sdrivers[x])
        x+=1
    print "PDRIVERS"
    print pdrivers
    #query for the location of each driver[i][0]
    loc=[ [18.024583,-76.761250],[18.030585,-76.765521],[18.030801,-76.773276],[18.031141,-76.761521],[18.019688,-76.765046],[18.026336,-76.757449],[18.026572,-76.771523],[18.020625,-76.774054],[18.017870,-76.757470],[18.030816,-76.765507] ]
    i=0
    while (i < len(pdrivers)):
        pdrivers[i].append(loc[i])
        i+=1
    print "loc"
    print pdrivers
    print "GET DRIVERS"
    return str(pdrivers)

# @app.route('/save-coord', methods=['GET', 'POST'])
# def save_coord():
#     pickup=request.form['pickUpLoc']
#     dest=request.form['destLoc']
#     print  "PICKUP: "+pickup+", "+"DEST: "+ dest

@app.route('/report', methods=["GET"])
@login_required
def report():
    # store all vehicles from database in this variable vehiclesss=
    return render_template("report.html")
    
@app.route('/view_driver', methods=["GET"])
@login_required
def view_driver():
    # store all drivers from database in this variable driversss=
    return render_template("view_driver.html")
    
@app.route('/view_vehicle', methods=["GET"])
@login_required
def view_vehicles():
    # store all vehicles from database in this variable vehiclesss=
    return render_template("view_vehicles.html")
    
@app.route('/view_clients', methods=["GET"])
@login_required
def view_clients():
    # store all clients from database in this variable clientsss=
    return render_template("view_clients.html")
    
@app.route("/operator", methods=["GET"])
@login_required
def opp_main():
    return render_template("operator_main.html")
    
@app.route("/operates", methods=["POST","GET"])
@login_required
def operates():
    opform=OperatesForm()
    if request.method=="POST":
        if opform.validate_on_submit():
            #Add queries to check if plate number and trn are already in database
            return render_template("operator_main.html")
    return render_template('operates.html',form=opform)
    
    
@app.route("/customer_notification", methods=["GET"])
def customer_notification():
    dfname= "" #received from database
    dlname= ""
    vcolour= ""
    platenum= ""
    eta_driver= ""
    d_loc= ""
    eta= ""
    return render_template("customer_notif.html", dfname=dfname,dlname=dlname, vcolour=vcolour, platenum=platenum, eta_driver=eta_driver, d_loc=d_loc, eta=eta )
