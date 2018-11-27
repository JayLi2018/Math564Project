# create view to get all the stats we need to calculate TOE
create view TOE_STATS AS 
select season,team, win_ratio, three_pm, (fgm-three_pm) as two_pm, fga, oreb, tov, (second_points/2)/oreb as ORBS, (oppo_pts_off_to/2)/tov as op_pots from team_stats

# get the TOE
create view toe_results as 
select season, team, win_ratio, (three_pm+two_pm)/(fga - oreb + tov) as toe, (two_pm + 1.5*three_pm)/(fga - oreb*orbs + tov*op_pots) as new_toe
from toe_stats

\copy (select * from toe_results) to 'toe_results.csv' DELIMITER ',' CSV HEADER;