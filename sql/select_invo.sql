select pp.nome from pp, invo 

	where invo.nome = ?

	pp.id_pp = invo.id_pp_1 

	or 

	pp.id_pp = invo.id_pp_2