SELECT pp.id_pp, pp.id_player, pp.nome, pp.aparencia, pp.sangue, pp.base, pp.cla_1, pp.cla_2, 

       a.id_afiliacao,

       pa.id_patente,

       c.id_cargo,

       e.nome,

       pp.registro_ninja, pp.data_criacao, 

       pr.nome,

       pp.dinheiro,

       h.nome,

       j.id_juinjutsu,

       k.nome,

       kkg.nome,

       pp.modificacao_corporal, 

       s.nome,

       t.nome, 

       y.nome
       
  FROM pp, afiliacao a, patente pa, cargo c, elemento e, premio pr, hiden h, juinjutsu j, kinjutsu k, kkg, senjutsu s, traco_unico t, yugojutsu y

  where 
a.id_afiliacao = pp.id_afiliacao
and
       pa.id_patente = pp. id_patente
and
       c.id_cargo = pp.id_cargo
and
       e.id_elemento = pp.id_elemento_1
and
       e.id_elemento = pp.id_elemento_2
and
       e.id_elemento = pp.id_elemento_3
and
       e.id_elemento = pp.id_elemento_4 
and
       pr.id_premio = pp.id_premio_1
and
       pr.id_premio = pp.id_premio_2
and
       pr.id_premio = pp.id_premio_3
and
       pr.id_premio = pp.id_premio_4 
and
       h.id_hiden = pp.id_hiden_1
and
       h.id_hiden = pp.id_hiden_2 
and
       h.id_hiden = pp.id_hiden_3
and
       j.id_juinjutsu = pp.id_juinjutsu
and
       k.id_kinjutsu = pp.id_kinjutsu_1
and
       k.id_kinjutsu = pp.id_kinjutsu_2
and
       k.id_kinjutsu = pp.id_kinjutsu_3
and
       k.id_kinjutsu = pp.id_kinjutsu_4
and
       k.id_kinjutsu = pp.id_kinjutsu_5
and
       kkg.id_kkg = pp.id_kkg_1
and
       kkg.id_kkg = pp.id_kkg_2
and
       kkg.id_kkg = pp.id_kkg_3
and
       kkg.id_kkg = pp.id_kkg_4
and
       kkg.id_kkg = pp.id_kkg_5
and
       s.id_senjutsu = pp.id_senjutsu_1
and
       s.id_senjutsu = pp.id_senjutsu_2 
and
       s.id_senjutsu = pp.id_senjutsu_3
and
       t.id_traco_unico = pp.id_traco_unico_1
and
       t.id_traco_unico = pp.id_traco_unico_2
and
       t.id_traco_unico = pp.id_traco_unico_3 
and
       y.id_yugojutsu = pp.id_yugojutsu_1
and
       y.id_yugojutsu = pp.id_yugojutsu_2
and
       y.id_yugojutsu = pp.id_yugojutsu_3
and
	pp.id_pp = 1.1