/*-------Creating the Database-----*/
drop database if exists trs;
create database trs;
use trs;

/*----Creating the Tables----*/
create table client(
		userCID varchar(20) Not Null,
		cfname varchar(20),
		clname varchar(20),
		ccontact int(11),
    	-- cemail varchar(17),
    	-- cpassword varchar (20),
    	cadd1 varchar (30),
    	cadd2 varchar(30),
		city varchar(25),
		parish varchar(12),
		cstatus varchar(12),
		primary key(userCID)
		);
create table driver(
		userDID varchar(20) Not Null,
		dtrn int(9),
		dfname varchar(20),
		dlname varchar(20),
    	dcontact int(10),
    	-- demail varchar (15),
    	-- dpassword varchar(20),
    	dadd1 varchar(20),
    	dadd2 varchar(20),
		dcity varchar(20),
		dparish varchar(12),
		dstatus varchar(11),
		primary key(userDID)
		);
create table operator(
		userOID varchar(20) Not Null,
		ofname varchar(20),
		olname varchar(20),
		otrn int(10),
    	oadd1 varchar(20),
    	oadd2 varchar(20),
    	ocity varchar(20),
		oparish varchar(12),
		primary key(userOID)
		);
create table vehicle(
		plateNum varchar(8),
		vmodel varchar(10),
		vmake varchar(15),
		vcolour varchar(10),
		seat_cap int(1),
		class varchar(10),
		primary key(plateNum)
);
create table job_view(
	userDID varchar(20),
	userCID varchar(20),
	userOID varchar(20),
	plateNum varchar(6),
	job_date date,
	job_time time,
	job_status varchar(9),
	primary key(userDID,userCID,plateNum),
	foreign key (userDID) references driver(userDID) on update cascade on delete cascade,
	foreign key (userCID) references client(userCID) on update cascade on delete cascade,
	foreign key (userOID) references operator(userOID) on update cascade on delete cascade,
	foreign key (plateNum) references vehicle(plateNum) on update cascade on delete cascade
);
create table carry(
	userCID varchar(20),
	userDID varchar(20),
	plateNum varchar(6),
	primary key(userDID,userCID,plateNum),
	foreign key (userDID) references driver(userDID) on update cascade on delete cascade,
	foreign key (userCID) references client(userCID) on update cascade on delete cascade,
	foreign key (plateNum) references vehicle(plateNum) on update cascade on delete cascade
);
create table operates(
	userDID varchar(20),
	plateNum varchar(6),
	primary key(userDID,plateNum),
	foreign key (userDID) references driver(userDID) on update cascade on delete cascade,
	foreign key (plateNum) references vehicle(plateNum) on update cascade on delete cascade
);

create table users(
	id varchar(20),
	email varchar(17),
	password varchar(20),
	utype varchar(15),
	primary key(id)
);

create table driver_location(
	userDID varchar(20),
	lat varchar(10),
	longi varchar(10),
	pos varchar(10),
	primary key(userDID),
	foreign key (userDID) references driver(userDID) on update cascade on delete cascade
);

create table driver_pool(
	userDID varchar(20),
	lat varchar(10),
	longi varchar(10),
	pos varchar(10),
	eta time,
	primary key(userDID)
);

create table idvalue(
	idV int AUTO_INCREMENT NOT NULL,
	cValue int(5),
	dValue int(5),
	oValue int(5),
	primary key(idV)
);

insert into idvalue values(1,1,1,1);

insert into operator(userOID,ofname,olname,otrn,oadd1,oadd2,ocity,oparish) values('o54','Op1','lname',23435454,'last lane','threst','Denham Town','Kingston');	
insert into operator(userOID,ofname,olname,otrn,oadd1,oadd2,ocity,oparish) values('o34','Op2','lname',34435454,'fast lane','jist','Spanish Town','St. Catherine');	
insert into operator(userOID,ofname,olname,otrn,oadd1,oadd2,ocity,oparish) values('o64','Op3','lname',12335454,'past lane','hist','Tivoli','Kingston');	
insert into operator(userOID,ofname,olname,otrn,oadd1,oadd2,ocity,oparish) values('o44','Op4','lname',87935454,'thirst lane','vest','Almond Town','Kingston');	
insert into operator(userOID,ofname,olname,otrn,oadd1,oadd2,ocity,oparish) values('o65','Op5','lname',98435454,'lastly lane','hatt','Hannah Town','Kingston');	


insert into client(userCID,cfname,clname,ccontact,cadd1,cadd2,city,parish,cstatus) values('c64','Brad','Pitt',8768756789,'12 every thing','dere','city1','parish1','Active');
insert into client(userCID,cfname,clname,ccontact,cadd1,cadd2,city,parish,cstatus) values('c04','Janet','Pitt',8769765789,'16 every thing','dere','city1','parish1','Blocked');
insert into client(userCID,cfname,clname,ccontact,cadd1,cadd2,city,parish,cstatus) values('c98','Sandra','Pitt',8769059989,'19 every thing','dere','city1','parish1','Inactive');
insert into client(userCID,cfname,clname,ccontact,cadd1,cadd2,city,parish,cstatus) values('c74','Betty','Pitt',8767056789,'10 every thing','dere','city1','parish1','Blocked');
insert into client(userCID,cfname,clname,ccontact,cadd1,cadd2,city,parish,cstatus) values('c55','Patrice','Pitt',8764056789,'12 every thing','dere','city1','parish1','Active');


insert into driver(userDID,dtrn,dfname,dlname,dcontact,dadd1,dadd2,dcity,dparish,dstatus) values('d09',567890987,'Grace','Lawrence',8769087890,'87 Harley Drive','Lance','city2','parish2','Available');
insert into driver(userDID,dtrn,dfname,dlname,dcontact,dadd1,dadd2,dcity,dparish,dstatus) values('d91',987890987,'Frank','Lawrence',8769087890,'87 Harley Drive','Lance','city2','parish2','Busy');
insert into driver(userDID,dtrn,dfname,dlname,dcontact,dadd1,dadd2,dcity,dparish,dstatus) values('d78',347890987,'Jules','Lawrence',8769087890,'87 Harley Drive','Lance','city2','parish2','Offline');
insert into driver(userDID,dtrn,dfname,dlname,dcontact,dadd1,dadd2,dcity,dparish,dstatus) values('d67',767890987,'Louis','Lawrence',8769087890,'87 Harley Drive','Lance','city2','parish2','Busy');
insert into driver(userDID,dtrn,dfname,dlname,dcontact,dadd1,dadd2,dcity,dparish,dstatus) values('d02',237890987,'Olive','Lawrence',8769087890,'87 Harley Drive','Lance','city2','parish2','Available');


insert into vehicle(plateNum,vmodel,vmake,vcolour,seat_cap,class) values('HY1234','Corolla','Toyota','Black','1','Classic');
insert into vehicle(plateNum,vmodel,vmake,vcolour,seat_cap,class) values('OL1234','Lancer','Mitzubishi','Black','2','Regular');
insert into vehicle(plateNum,vmodel,vmake,vcolour,seat_cap,class) values('PI1234','Sunny','Nissan','Black','3','Any');
insert into vehicle(plateNum,vmodel,vmake,vcolour,seat_cap,class) values('MJ1234','Blue','Hyundai','Black','4','Any');
insert into vehicle(plateNum,vmodel,vmake,vcolour,seat_cap,class) values('UT1234','Long','Kia','Black','2','Classic');


insert into operates(userDID,plateNum) values('d09','HY1234');
insert into operates(userDID,plateNum) values('d91','OL1234');
insert into operates(userDID,plateNum) values('d78','PI1234');
insert into operates(userDID,plateNum) values('d67','MJ1234');
insert into operates(userDID,plateNum) values('d02','UT1234');

insert into carry(userCID,userDID,plateNum) values('c64','d09','HY1234');
insert into carry(userCID,userDID,plateNum) values('c04','d91','OL1234');
insert into carry(userCID,userDID,plateNum) values('c98','d78','PI1234');
insert into carry(userCID,userDID,plateNum) values('c74','d67','MJ1234');
insert into carry(userCID,userDID,plateNum) values('c55','d02','UT1234');



insert into job_view(userDID,userCID,userOID,plateNum,job_date,job_time,job_status) values('d09','c64','o65','HY1234','2017-09-09','08:09','Completed');
insert into job_view(userDID,userCID,userOID,plateNum,job_date,job_time,job_status) values('d91','c04','o65','OL1234','2017-09-10','09:09','In-Progress');
insert into job_view(userDID,userCID,userOID,plateNum,job_date,job_time,job_status) values('d78','c98','o65','PI1234','2017-09-04','07:09','Cancelled');
insert into job_view(userDID,userCID,userOID,plateNum,job_date,job_time,job_status) values('d67','c74','o65','MJ1234','2017-09-07','12:09','In-Progress');
insert into job_view(userDID,userCID,userOID,plateNum,job_date,job_time,job_status) values('d02','c55','o65','UT1234','2017-09-12','10:09','Completed');


insert into users(id,email,password,utype) values('c64','stacy@stacy.com','quer','client');
insert into users(id,email,password,utype) values('d09','jumpup@jump.com','quer','driver');
insert into users(id,email,password,utype) values('c04','dance@dance.com','quer','client');
insert into users(id,email,password,utype) values('o65','love@love.com','quer','operator');
insert into users(id,email,password,utype) values('d91','trust@trust.com','quer','driver');


insert into driver_location(userDID,lat,longi,pos) values('d09',18.019506,-76.760675,94.780181);
insert into driver_location(userDID,lat,longi,pos) values('d91',18.015109,-76.753336,94.768445);
insert into driver_location(userDID,lat,longi,pos) values('d78',18.015569,-76.799849,94.815418);
insert into driver_location(userDID,lat,longi,pos) values('d67',18.019506,-76.760675,94.840181);
insert into driver_location(userDID,lat,longi,pos) values('d02',18.019587,-76.777875,94.797462);
