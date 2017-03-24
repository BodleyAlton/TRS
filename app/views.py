from app import app,db,login_manager
from flask import render_template, request, redirect, url_for, jsonify,flash
from forms import clientForm, RequestForm, driverForm, operatorForm, vehicleForm,LoginForm
from models import Clientdb, Driver, Operator, Vehicle
from flask_login import LoginManager
from flask_login import login_user, logout_user, current_user, login_required
from Req import *
from sqlalchemy.sql import select
from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root@localhost/trs', echo=True)
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
@login_required
def home():
    rform=RequestForm()
    return render_template('map.html',form=rform)

@app.route('/add-client', methods=['POST','GET'])
def add_client():
    cform=clientForm()
    if request.method=='POST':
        if cform.validate_on_submit():
            cfname=cform.cfname.data
            clname=cform.clname.data
            ccontact=cform.ccontact.data
            cemail=cform.cemail.data
            cpassword=cform.cpassword.data
            cadd1=cform.cadd1.data
            cadd2=cform.cadd2.data
            ccity=cform.ccity.data
            cparish=cform.cparish.data
            client= Clientdb(cfname,clname,ccontact,cemail,cpassword,cadd1,cadd2,ccity,cparish)
            db.session.add(client)
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
            driver= Driver(dfname,dlname,dcontact,demail,dpassword,dadd1,dadd2,dcity,dparish,dtrn)
            db.session.add(driver)
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
            otrn=oform.otrn.data
            operator= Operator(ofname,olname,oadd1,oadd2,ocity,oparish,otrn)
            db.session.add(operator)
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
            print pw;
            userr = Clientdb.query.filter_by(cemail=un,cpassword = pw).first()
            print userr;
            login_user(userr)
            return redirect(url_for ('home'))
            print "Loged In"
            next=request.args.get('next')
            # if not is_safe_url(next):
            #     return abort(400)
            # return redirect(next or url_for('home'))
        else:
            print 'FAIL'
    return render_template('login.html',form=lform)

@login_manager.user_loader
def load_user(id):
    return Clientdb.query.get(int(id))

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
        fNResult= db.engine.execute('select cfname from client where id='+str(cid))
        lNResult= db.engine.execute('select clname from client where id='+str(cid))
        cResult= db.engine.execute('select ccontact from client where id='+str(cid))
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
        getDrivers(seat,vtype,driver,cdist)
        return "success"
        # return creq.dest() #consider making a global variable and pass to function responsible for p.queue


def getDrivers(seat,vtype,driver,cdist):
    drivers=[]
    pdrivers=[]
    i=0
    j=0
    if driver != '':
        print driver #driver= Put query here using driver(return name,platereg,make,model and color of vchl){Zaavan}
    #drivers=  #query name,loc, v.color,v.model,v.make,v.regnum where seat>seatCap,vtype=vtype
    drivers=[[123,6],[456,10],[789,7.5],[3412,7],[345,7.67],[678,1],[901,4],[234,5],[567,3],[890,2],[4794,15],[54536,11],[5773,14],[47789,12],[7540,13]] #List produced by database query
    # for driver in drivers:
    #         driverss.append(driver.name,driver.regnum,driver.model,driver.make,driver.color, driver.loc)
    # while (i < len(driverss)):
    #     name=driverss[i][0]
    #     regnum=driverss[i][1]
    #     model=driverss[i][2]
    #     make=make[i][3]
    #     color=driverss[i][4]
    #     loc=driverss[i][5]
    # pdriver=Driver(name,regnum,make,model,color,loc)
    # return pdriver.dest() #Consider passing to another function where the priority list will be populated.
    print "DRIVER SEAT: "+str(seat)
    print "DRIVER VTYPE: "+ vtype
    print drivers
    sdrivers=sorted(drivers,key=getKey)
    print "Sorted"
    print sdrivers
    #cpos=binary_search(sdrivers, cdist, 0, len(sdrivers)-1)
    cpos=5
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
    getEta(pdrivers)

def getEta(drivers):
    print "here"
    print pickup
    drv=drivers
    print "ETA"
    print drv
    return render_template('eta.html',drivers=drv)

@app.route('/save-coord', methods=['GET', 'POST'])
def save_coord():
    pickup=request.form['pickUpLoc']
    dest=request.form['destLoc']
    print  "PICKUP: "+pickup+", "+"DEST: "+ dest
