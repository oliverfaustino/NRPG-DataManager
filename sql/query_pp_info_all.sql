select pp.id_personagem, pp.personagem, pp.cla_1, pp.cla_2, pp.base, pp.sangue, pp.aparencia, pp.patente, p.patente as rank_da_patente, 
pp.afiliacao, a.afiliacao as nome_da_afilicação, pp.poderes_cla_1, pp.poderes_cla_2, pp.kkg, pp.hiden, pp.traco_unico, pp.yugojutsu, 
pp.modificacao_corporal, pp.data_criacao 
from pp_info pp, patente_info p, afiliacao_info a
where pp.patente = p.id_patente and pp.afiliacao = a.id_afiliacao
order by id_personagem asc