select nome as player,check_in as pontos_de_check_in from player
where check_in <> 0 
order by check_in desc