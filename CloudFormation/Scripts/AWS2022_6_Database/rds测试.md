[ec2-user@ip-10-1-11-132 ~]$ psql -U qytdbuser -d qytdb -h qytdbcluster.cluster-ckfrzyodllek.us-east-1.rds.amazonaws.com
Password for user qytdbuser: Cisc0123

psql (9.2.24, server 10.14)
WARNING: psql version 9.2, server version 10.0.
         Some psql features might not work.
SSL connection (cipher: ECDHE-RSA-AES128-GCM-SHA256, bits: 128)
Type "help" for help.

qytdb=> create table test1(t1 int, t2 varchar(40));
CREATE TABLE

qytdb=> insert into test1 (t1,t2) values (11, 'welcome to qytang');
INSERT 0 1

qytdb=> insert into test1 (t1,t2) values (12, 'welcome to python');
INSERT 0 1

qytdb=> select * from test1;
 t1 |        t2         
----+-------------------
 11 | welcome to qytang
 12 | welcome to python
(2 rows)
