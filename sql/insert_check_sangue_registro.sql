select pp.nome as nome_do_personagem, player.nome as nome_do_player from pp, player
where pp.id_player = player.id_player
order by pp.nome asc