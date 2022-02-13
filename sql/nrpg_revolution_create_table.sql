CREATE TABLE traco_unico (
                id_traco_unico INTEGER NOT NULL,
                nome VARCHAR(50) NOT NULL,
                classificacao VARCHAR(50),
                CONSTRAINT id_traco_unico PRIMARY KEY (id_traco_unico)
);


CREATE TABLE elemento (
                id_elemento INTEGER NOT NULL,
                nome VARCHAR(10) NOT NULL,
                CONSTRAINT id_elemento PRIMARY KEY (id_elemento)
);


CREATE TABLE kkg (
                id_kkg INTEGER NOT NULL,
                nome VARCHAR(30) NOT NULL,
                classificacao VARCHAR(30) NOT NULL,
                CONSTRAINT id_kkg PRIMARY KEY (id_kkg)
);


CREATE TABLE juinjutsu (
                id_juinjutsu INTEGER NOT NULL,
                nome VARCHAR(30) NOT NULL,
                CONSTRAINT id_juinjutsu PRIMARY KEY (id_juinjutsu)
);


CREATE TABLE kinjutsu (
                id_kinjutsu INTEGER NOT NULL,
                nome VARCHAR(30) NOT NULL,
                CONSTRAINT id_kinjutsu PRIMARY KEY (id_kinjutsu)
);


CREATE TABLE senjutsu (
                id_senjutsu INTEGER NOT NULL,
                nome VARCHAR(30) NOT NULL,
                CONSTRAINT id_senjutsu PRIMARY KEY (id_senjutsu)
);


CREATE TABLE yugojutsu (
                id_yugojutsu INTEGER NOT NULL,
                nome VARCHAR(30) NOT NULL,
                CONSTRAINT id_yugojutsu PRIMARY KEY (id_yugojutsu)
);


CREATE TABLE hiden (
                id_hiden INTEGER NOT NULL,
                nome VARCHAR(30) NOT NULL,
                classificacao VARCHAR(30) NOT NULL,
                CONSTRAINT id_hiden PRIMARY KEY (id_hiden)
);


CREATE TABLE premio (
                id_premio INTEGER NOT NULL,
                nome VARCHAR(10) NOT NULL,
                CONSTRAINT id_premio PRIMARY KEY (id_premio)
);


CREATE TABLE cargo (
                id_cargo INTEGER NOT NULL,
                nome VARCHAR(30) NOT NULL,
                CONSTRAINT id_cargo PRIMARY KEY (id_cargo)
);


CREATE TABLE patente (
                id_patente INTEGER NOT NULL,
                nome VARCHAR(6) NOT NULL,
                CONSTRAINT id_patente PRIMARY KEY (id_patente)
);


CREATE TABLE afiliacao (
                id_afiliacao INTEGER NOT NULL,
                nome VARCHAR(30) NOT NULL,
                CONSTRAINT id_afiliacao PRIMARY KEY (id_afiliacao)
);


CREATE TABLE player (
                id_player INTEGER NOT NULL,
                nome VARCHAR(30) NOT NULL,
                numero BIGINT NOT NULL,
                recrutador INTEGER DEFAULT 0,
                CONSTRAINT id_player PRIMARY KEY (id_player)
);


CREATE TABLE pp (
                id_pp INTEGER NOT NULL,
                id_player INTEGER NOT NULL,
                nome VARCHAR(30) NOT NULL,
                aparencia VARCHAR(30) NOT NULL,
                sangue INTEGER NOT NULL,
                base VARCHAR(30) NOT NULL,
                cla_1 VARCHAR(30) NOT NULL,
                cla_2 VARCHAR(30),
                id_afiliacao INTEGER NOT NULL,
                id_patente INTEGER NOT NULL,
                id_cargo INTEGER,
                id_elemento_1 INTEGER NOT NULL,
                id_elemento_2 INTEGER,
                id_elemento_3 INTEGER,
                id_elemento_4 INTEGER,
                id_elemento_5 INTEGER,
                registro_ninja NUMERIC(6) NOT NULL,
                data_criacao DATE NOT NULL,
                ponto INTEGER,
                id_premio_1 INTEGER,
                id_premio_2 INTEGER,
                id_premio_3 INTEGER,
                id_premio_4 INTEGER,
                id_hiden INTEGER,
                id_juinjutsu INTEGER NOT NULL,
                id_kinjutsu INTEGER,
                id_kkg INTEGER,
                modificacao_corporal VARCHAR(50),
                id_senjutsu INTEGER,
                id_traco_unico INTEGER,
                id_yugojutsu INTEGER,
                CONSTRAINT id_pp PRIMARY KEY (id_pp)
);


CREATE TABLE arma (
                id_arma INTEGER NOT NULL,
                nome VARCHAR(50) NOT NULL,
                id_pp_1 INTEGER,
                id_pp_2 INTEGER,
                id_pp_3 INTEGER,
                id_pp_4 INTEGER,
                id_pp_5 INTEGER,
                id_pp_6 INTEGER,
                CONSTRAINT id_arma PRIMARY KEY (id_arma)
);


CREATE TABLE reen (
                id_reen INTEGER NOT NULL,
                nome VARCHAR(30) NOT NULL,
                id_pp INTEGER,
                CONSTRAINT id_reen PRIMARY KEY (id_reen)
);


CREATE TABLE bijuu (
                id_bijuu INTEGER NOT NULL,
                nome VARCHAR(30) NOT NULL,
                id_pp_jinchuuriki INTEGER,
                CONSTRAINT id_bijuu PRIMARY KEY (id_bijuu)
);


CREATE TABLE pseudo_jinchuuriki (
                id_pseudo_jinchuuriki INTEGER NOT NULL,
                id_bijuu INTEGER NOT NULL,
                id_pp_1 INTEGER,
                id_pp_2 INTEGER,
                id_pp_3 INTEGER,
                CONSTRAINT id_pseudo_jinchuuriki PRIMARY KEY (id_pseudo_jinchuuriki)
);


CREATE TABLE invo (
                id_invo INTEGER NOT NULL,
                nome VARCHAR(30) NOT NULL,
                id_pp_1 INTEGER,
                id_pp_2 INTEGER,
                CONSTRAINT id_invo PRIMARY KEY (id_invo)
);


ALTER TABLE pp ADD CONSTRAINT traco_unico_pp_fk
FOREIGN KEY (id_traco_unico)
REFERENCES traco_unico (id_traco_unico)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE pp ADD CONSTRAINT elemento_pp_fk
FOREIGN KEY (id_elemento_5)
REFERENCES elemento (id_elemento)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE pp ADD CONSTRAINT elemento_pp_fk1
FOREIGN KEY (id_elemento_1)
REFERENCES elemento (id_elemento)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE pp ADD CONSTRAINT elemento_pp_fk2
FOREIGN KEY (id_elemento_2)
REFERENCES elemento (id_elemento)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE pp ADD CONSTRAINT elemento_pp_fk3
FOREIGN KEY (id_elemento_3)
REFERENCES elemento (id_elemento)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE pp ADD CONSTRAINT elemento_pp_fk4
FOREIGN KEY (id_elemento_4)
REFERENCES elemento (id_elemento)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE pp ADD CONSTRAINT kkg_pp_fk
FOREIGN KEY (id_kkg)
REFERENCES kkg (id_kkg)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE pp ADD CONSTRAINT juinjutsu_pp_fk
FOREIGN KEY (id_juinjutsu)
REFERENCES juinjutsu (id_juinjutsu)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE pp ADD CONSTRAINT kinjutsu_pp_fk
FOREIGN KEY (id_kinjutsu)
REFERENCES kinjutsu (id_kinjutsu)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE pp ADD CONSTRAINT senjutsu_pp_fk
FOREIGN KEY (id_senjutsu)
REFERENCES senjutsu (id_senjutsu)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE pp ADD CONSTRAINT yugojutsu_pp_fk
FOREIGN KEY (id_yugojutsu)
REFERENCES yugojutsu (id_yugojutsu)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE pp ADD CONSTRAINT hiden_pp_fk
FOREIGN KEY (id_hiden)
REFERENCES hiden (id_hiden)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE pp ADD CONSTRAINT premio_pp_fk
FOREIGN KEY (id_premio_1)
REFERENCES premio (id_premio)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE pp ADD CONSTRAINT premio_pp_fk1
FOREIGN KEY (id_premio_2)
REFERENCES premio (id_premio)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE pp ADD CONSTRAINT premio_pp_fk2
FOREIGN KEY (id_premio_3)
REFERENCES premio (id_premio)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE pp ADD CONSTRAINT premio_pp_fk3
FOREIGN KEY (id_premio_4)
REFERENCES premio (id_premio)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE pp ADD CONSTRAINT cargo_pp_fk
FOREIGN KEY (id_cargo)
REFERENCES cargo (id_cargo)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE pp ADD CONSTRAINT patente_pp_fk
FOREIGN KEY (id_patente)
REFERENCES patente (id_patente)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE pp ADD CONSTRAINT afiliacao_pp_fk
FOREIGN KEY (id_afiliacao)
REFERENCES afiliacao (id_afiliacao)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE pp ADD CONSTRAINT player_pp_fk
FOREIGN KEY (id_player)
REFERENCES player (id_player)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE player ADD CONSTRAINT player_player_fk
FOREIGN KEY (recrutador)
REFERENCES player (id_player)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE invo ADD CONSTRAINT pp_invo_fk
FOREIGN KEY (id_pp_1)
REFERENCES pp (id_pp)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE invo ADD CONSTRAINT pp_invo_fk1
FOREIGN KEY (id_pp_2)
REFERENCES pp (id_pp)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE bijuu ADD CONSTRAINT pp_bijuu_fk
FOREIGN KEY (id_pp_jinchuuriki)
REFERENCES pp (id_pp)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE pseudo_jinchuuriki ADD CONSTRAINT pp_pseudo_jinchuuriki_fk
FOREIGN KEY (id_pp_1)
REFERENCES pp (id_pp)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE pseudo_jinchuuriki ADD CONSTRAINT pp_pseudo_jinchuuriki_fk1
FOREIGN KEY (id_pp_2)
REFERENCES pp (id_pp)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE pseudo_jinchuuriki ADD CONSTRAINT pp_pseudo_jinchuuriki_fk2
FOREIGN KEY (id_pp_3)
REFERENCES pp (id_pp)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE reen ADD CONSTRAINT pp_reen_fk
FOREIGN KEY (id_pp)
REFERENCES pp (id_pp)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE arma ADD CONSTRAINT pp_arma_fk
FOREIGN KEY (id_pp_1)
REFERENCES pp (id_pp)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE arma ADD CONSTRAINT pp_arma_fk1
FOREIGN KEY (id_pp_2)
REFERENCES pp (id_pp)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE arma ADD CONSTRAINT pp_arma_fk2
FOREIGN KEY (id_pp_3)
REFERENCES pp (id_pp)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE arma ADD CONSTRAINT pp_arma_fk3
FOREIGN KEY (id_pp_4)
REFERENCES pp (id_pp)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE arma ADD CONSTRAINT pp_arma_fk4
FOREIGN KEY (id_pp_5)
REFERENCES pp (id_pp)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE arma ADD CONSTRAINT pp_arma_fk5
FOREIGN KEY (id_pp_6)
REFERENCES pp (id_pp)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE pseudo_jinchuuriki ADD CONSTRAINT bijuu_pseudo_jinchuuriki_fk
FOREIGN KEY (id_bijuu)
REFERENCES bijuu (id_bijuu)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;