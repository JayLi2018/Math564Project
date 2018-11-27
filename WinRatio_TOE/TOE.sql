# create view to get all the stats we need to calculate TOE -- team offensive efficiency
create view TOE_STATS AS 
select season,team, win_ratio, three_pm, (fgm-three_pm) as two_pm, fga, oreb, tov, (second_points/2)/oreb as ORBS, (oppo_pts_off_to/2)/tov as op_pots, pace from team_stats

# get the TOE
select season, team, win_ratio, (two_pm + 1.5*three_pm)/(fga - oreb*orbs + tov*op_pots)as toe,pace
from toe_stats

# create view to get all stats we need to calculate OPTOE --opponent team offensive efficiency

CREATE VIEW OP_TOE_STATS AS 
SELECT T.Season,T.TEAM, (OP.OPP_FGM-OP.OPP_3PM) AS OPP_2PM, OP.OPP_3PM, OP.OPP_FGA,OP.OPP_OREB,(T.oppo_second_points/2)/OP.OPP_OREB as opp_orbs,op.opp_tov,(t.pts_off_to/2)/(op.opp_tov) as TEAM_POTS
from Team_STATS t ,team_opp_stats op
where t.season = op.season and t.team = op.team

# get the OPTOE

SELECT season, team, (oppo_2pm + 1.5*oppo_3pm)/(OPP_FGA-opp_orb*opp_orbs + oppo_tov*TEAM_POTS) as OPTOE
from OP_TOE_STATS

# view 
create view toe_optoe as
with toe as
(
select season, team, win_ratio, (two_pm + 1.5*three_pm)/(fga - oreb*orbs + tov*op_pots)as toe,pace
from toe_stats
),
optoe as
(
SELECT season, team, (opp_2pm + 1.5*opp_3pm)/(OPP_FGA-opp_oreb*opp_orbs + opp_tov*TEAM_POTS) as OPTOE
from OP_TOE_STATS
)
select t.*,o.optoe
from toe t, optoe o
where t.season = o.season and t.team = o.team

# calculate net rating

with avg_pace as
(
select season,  avg(pace) as lg_pace 
from toe_optoe
group by season
)
select t.*, a.lg_pace,10*(t.toe-t.optoe)*pace/lg_pace as net_rating 
from avg_pace a, toe_optoe t
where t.season = a.season
order by season,win_ratio desc

# old net rating

select t.season,t.team, ((t.two_fgm+t.three_pm)/(t.fga-t.oreb+t.tov)) - ((o.opp_2pm+o.opp_3pm)/(o.OPP_FGA-o.OPP_OREB+opp_tov)) as old_net_rating
from toe_stats t ,OP_TOE_STATS t
where t.season = o.season and t.team = o.team

