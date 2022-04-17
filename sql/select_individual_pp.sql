SELECT pp.id_pp, pp.id_player, pp.nome, pp.aparencia, pp.sangue, pp.base, pp.cla_1, pp.cla_2, 
       A.nome as afiliação, PA.nome as patente, CA.nome as cargo, E1.nome as elemento_1, 
       E2.nome as e_2, E3.nome as e_3, E4.nome ase_4, E5.nome as e_5, pp.data_criacao, PR1.nome as prêmio_guardado_1, 
       PR2.nome as prêmio_2, PR3.nome as prêmio_3, PR4.nome as prêmio_4, dinheiro, H1.nome as hiden_1, 
       H2.nome as hiden_2, H3.nome as hiden_3, J.nome as juinjutsu, K1.nome as Kinjutsu_1, K2.nome as kinjutsu_2, 
       K3.nome as kinjutsu_3, K4.nome as kinjutsu_4, K5.nome as kinjutsu_5, KKG1.nome as kkg_1, KKG2.nome as kkg_2, 
       KKG3.nome as kkg_3, KKG4.nome as kkg_4, KKG5.nome as kkg_5, pp.modificacao_corporal, S1.nome as senjutsu_1, 
       S2.nome as senjutsu_2, S3.nome as senjutsu_3, TU1.nome as traço_único_1, TU2.nome as traço_único_2, 
        TU3.nome as traço_único_3, Y1.nome as yugojutsu_1, Y2.nome as yugojutsu_2, Y3.nome as yugojutsu_3
  FROM pp

inner join afiliacao A on pp.id_afiliacao = A.id_afiliacao
inner join patente PA on pp.id_patente = PA.id_patente
inner join cargo CA on pp.id_cargo = CA.id_cargo

inner join elemento E1 on pp.id_elemento_1 = E1.id_elemento 
inner join elemento E2 on pp.id_elemento_2 = E2.id_elemento 
inner join elemento E3 on pp.id_elemento_3 = E3.id_elemento 
inner join elemento E4 on pp.id_elemento_4 = E4.id_elemento 
inner join elemento E5 on pp.id_elemento_5 = E5.id_elemento

inner join premio PR1 on pp.id_premio_1 = PR1.id_premio
inner join premio PR2 on pp.id_premio_2 = PR2.id_premio
inner join premio PR3 on pp.id_premio_3 = PR3.id_premio
inner join premio PR4 on pp.id_premio_4 = PR4.id_premio

inner join hiden H1 on pp.id_hiden_1 = H1.id_hiden
inner join hiden H2 on pp.id_hiden_2 = H2.id_hiden
inner join hiden H3 on pp.id_hiden_3 = H3.id_hiden

inner join juinjutsu J on pp.id_juinjutsu = J.id_juinjutsu

inner join kinjutsu K1 on pp.id_kinjutsu_1 = K1.id_kinjutsu
inner join kinjutsu K2 on pp.id_kinjutsu_2 = K2.id_kinjutsu
inner join kinjutsu K3 on pp.id_kinjutsu_3 = K3.id_kinjutsu
inner join kinjutsu K4 on pp.id_kinjutsu_4 = K4.id_kinjutsu
inner join kinjutsu K5 on pp.id_kinjutsu_5 = K5.id_kinjutsu

inner join kkg KKG1 on pp.id_kkg_1 = KKG1.id_kkg
inner join kkg KKG2 on pp.id_kkg_2 = KKG2.id_kkg
inner join kkg KKG3 on pp.id_kkg_3 = KKG3.id_kkg
inner join kkg KKG4 on pp.id_kkg_4 = KKG4.id_kkg
inner join kkg KKG5 on pp.id_kkg_5 = KKG5.id_kkg

inner join senjutsu S1 on pp.id_senjutsu_1 = S1.id_senjutsu
inner join senjutsu S2 on pp.id_senjutsu_2 = S2.id_senjutsu
inner join senjutsu S3 on pp.id_senjutsu_3 = S3.id_senjutsu

inner join traco_unico TU1 on pp.id_traco_unico_1 = TU1.id_traco_unico
inner join traco_unico TU2 on pp.id_traco_unico_2 = TU2.id_traco_unico
inner join traco_unico TU3 on pp.id_traco_unico_3 = TU3.id_traco_unico

inner join yugojutsu Y1 on pp.id_yugojutsu_1 = Y1.id_yugojutsu
inner join yugojutsu Y2 on pp.id_yugojutsu_2 = Y2.id_yugojutsu
inner join yugojutsu Y3 on pp.id_yugojutsu_3 = Y3.id_yugojutsu 

WHERE id_pp = 1.1