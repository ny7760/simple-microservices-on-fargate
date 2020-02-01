-- create user ‘user’@‘%’ identified by ‘password’;
-- grant all on *.* to ‘user’@‘%’

-- create database DB01;
create table students (id varchar(4), name varchar(20), score int);
insert into students values ('1001', 'Alice', 60);
insert into students values ('1002', 'Bob', 80);
commit;

