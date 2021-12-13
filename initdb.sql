use data_representation;

create table employees(
    -> eid int NOT NULL PRIMARY KEY,
    -> fname varchar(250),
    -> lname varchar(250),
    -> gender enum ("M","F"),
    -> dcode varchar(20),
    -> startdate DATE
    -> );

create table dept(
    -> dcode varchar(10) NOT NULL PRIMARY KEY,
    -> dname varchar(250)
    -> );