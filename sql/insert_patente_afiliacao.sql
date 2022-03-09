SELECT p.nome as dono_do_pp, p.numero, pp.nome as nome_do_pp, a.nome as afiliação_do_pp,pa.nome as patente_do_pp
	FROM player p, pp, patente pa, afiliacao a
	where pp.id_player = p.id_player 
	and pp.id_patente = pa.id_patente
	and pp.id_afiliacao = a.id_afiliacao
	and pp.id_afiliacao = 1
	and pp.id_patente = 3;
