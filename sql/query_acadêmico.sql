select p.id_player, p.player, p.personagem_1, pp.patente from player_info p, pp_info pp
where personagem = personagem_1 
and patente = 1 
order by personagem_1;