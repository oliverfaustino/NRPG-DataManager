select pp.id_pp, pp.nome 

from pp, invo 

where pp.id_pp = invo.id_pp_1 

and invo.id_invo = ?
