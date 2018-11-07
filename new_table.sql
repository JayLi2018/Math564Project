# create table
CREATE TABLE NBA
(
 Season INT,
 Player varchar(50),
 position varchar(20),
 age INT,
 Team varchar(20),
 gp INT,
 gs INT,
 mpg FLOAT,
 FG FLOAT,
 FGa FLOAT,
 FGp FLOAT,
 Three_PPG FLOAT,
 Three_PA FLOAT,
 Three_PP FLOAT,
 Two_PPG FLOAT,
 Two_PA FLOAT,
 Two_PP FLOAT,
 FT FLOAT,
 FTa FLOAT,
 FTp FLOAT,
 orb FLOAT,
 drb FLOAT,
 trb FLOAT,
 ast FLOAT,
 stl FLOAT,
 blk FLOAT,
 tov FLOAT,
 PF FLOAT,
 ppg FLOAT,
 win INT,
 loss INT,
 pct FLOAT,
 home varchar(20),
 away varchar(20),
 div varchar(20),
 conf varchar(20),
 team_ppg FLOAT,
 opp_ppg FLOAT,
 diff FLOAT,
 RK INT,
 TS FLOAT,
 AST_Ratio FLOAT,
 Turnover_Ratio FLOAT,
 Usage_Rate FLOAT,
 ORR FLOAT,
 DRR FLOAT,
 REBR FLOAT,
 PER FLOAT,
 VA FLOAT,
 EWA FLOAT
);

\copy NBA(Season,Player,position,age,Team,gp,gs,mpg,FG,FGa,FGp,Three_PPG,Three_PA,Three_PP,Two_PPG,Two_PA,Two_PP,FT,FTa,FTp,orb,drb,trb,ast,stl,blk,tov,PF,ppg,win,loss,pct,home,away,div,conf,team_ppg,opp_ppg,diff,RK,TS,AST_Ratio,Turnover_Ratio,Usage_Rate,ORR,DRR,REBR,PER,VA,EWA) from '/home/chenjie/Desktop/Math564Project/merge_espn_BRef.csv' DELIMITER ',' CSV HEADER



# input data
\copy NBA(Season,TEAM,win,loss,pct,home,away,div,conf,ppg,opp_ppg,diff,RK,PLAYER,GP,MPG,TS,AST,Tur_Ratio,USG,ORR,DRR,REBR,PER,VA,EWA) FROM '/home/chenjie/Desktop/Math564Project/all_merged_table.csv' DELIMITER ',' CSV HEADER

# calculate the product of minutes played(mpg*gp)
create view add_MTP as 
SELECT *, GP*MPG*PER AS Min_Times_Per
FROM NBA;


# filter out players which played less minutes
CREATE VIEW sorted_12 as 
SELECT * FROM
(
SELECT *, MPG*GP as sorting_standard,Rank()over (Partition by Season,TEAM ORDER BY MPG*GP DESC) as Rank 
FROM add_MTP
) rs
where Rank <=12

# get the log((team_PER)^2)
create view get_relationship_12 as 
select season,team,pct as win_ratio, log(sum(mpg*per)+sum(mpg*per)) as log_sum
from sorted_12
group by season,team,win_ratio


\copy (select * from get_relationship_12) to '/home/chenjie/Desktop/Math564Project/12_players.csv' DELIMITER ',' CSV HEADER;


sSELECT * FROM
(
SELECT *, MPG*GP as sorting_standard,Rank()over (Partition by Season,TEAM ORDER BY MPG*GP DESC) as Rank 
FROM add_MTP
) rs
where Rank <=10



select season, player, position, age, team, pct, (fg + ast)/(fga-orb + ast +tov) as Offensive_Efficiency
from NBA 
where (fga-orb + ast +tov) !=0
order by season,player, team

select season,team,pct as win_ratio, log(sum(gp*mpg*per)*sum(gp*mpg *per)) as log_sum 
from sorted_12 
group by season,team,win_ratio
