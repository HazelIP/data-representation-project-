use data_representation;

create table employee(
    -> eid int PRIMARY KEY,
    -> firstn varchar(250),
    -> lastn varchar(250),
    -> gender enum ("M","F"),
    -> dcode varchar(10),
    -> startdate date(250),
    );

create table dept(
    -> dcode varchar(10) PRIMARY KEY,
    -> name varchar(250),
    );