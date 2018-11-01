# create table
CREATE TABLE NBA
(
Season varchar(20),
 TEAM varchar(20),
 win FLOAT,
 loss FLOAT,
 pct FLOAT,
 home varchar(30),
 away varchar(30),
 div varchar(30),
 conf varchar(30),
 ppg FLOAT,
 opp_ppg FLOAT,
 diff FLOAT,
 RK FLOAT,
 PLAYER varchar(30),
 GP INT,
 MPG FLOAT,
 TS FLOAT,
 AST FLOAT,
 Tur_Ratio FLOAT,
 USG FLOAT,
 ORR FLOAT,
 DRR FLOAT,
 REBR FLOAT,
 PER FLOAT,
 VA FLOAT,
 EWA FLOAT,
);

# input data
\copy NBA(Season,TEAM,win,loss,pct,home,away,div,conf,ppg,opp_ppg,diff,RK,PLAYER,GP,MPG,TS,AST,Tur_Ratio,USG,ORR,DRR,REBR,PER,VA,EWA) FROM '/home/chenjie/Desktop/Math564Project/final_table.csv' DELIMITER ',' CSV HEADER

# calculate the product of minutes played(mpg*gp)
create view add_MTP as 
SELECT *, GP*MPG*PER AS Min_Times_Per
FROM NBA;


# filter out players which played less minutes
CREATE VIEW sorted_8 as 
SELECT * FROM
(
SELECT *, Rank()over (Partition by Season,TEAM ORDER BY Min_Times_Per DESC) as Rank 
FROM add_MTP
) rs
where Rank <=8

# get the log((team_PER)^2)
create view get_relationship as 
select season,team,pct as win_ratio, log(sum(min_times_per)*sum(min_times_per)) as log_of_sum_min_times_per_square
from sorted_8
group by season,team,win_ratio
order by season,team




