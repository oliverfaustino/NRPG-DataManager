select pp.nome from pp, invo 

	where invo.id_invo = ?

	pp.id_pp = invo.id_pp_1 

	or 

	pp.id_pp = invo.id_pp_2