select pp.nome as nome_do_pp, player.numero as número_do_player, player.nome as dono_do_personagem, a.nome as afiliação
from pp, afiliacao a, player
where pp.id_afiliacao = a.id_afiliacao
and pp.id_afiliacao = 3
and pp.id_player = player.id_player
and pp.id_patente <> 1