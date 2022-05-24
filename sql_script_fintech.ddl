-- Gerado por Oracle SQL Developer Data Modeler 21.4.2.059.0838
--   em:        2022-05-22 22:17:41 BRT
--   site:      Oracle Database 11g
--   tipo:      Oracle Database 11g



-- predefined type, no DDL - MDSYS.SDO_GEOMETRY

-- predefined type, no DDL - XMLTYPE

CREATE TABLE t_banco (
    cd_banco NUMBER(3) NOT NULL,
    nr_banco NUMBER(7) NOT NULL,
    nm_banco VARCHAR2(25) NOT NULL
);

ALTER TABLE t_banco ADD CONSTRAINT t_banco_pk PRIMARY KEY ( cd_banco );

CREATE TABLE t_bandeira_cartao (
    cd_bandeira NUMBER(3) NOT NULL,
    ds_bandeira VARCHAR2(30 CHAR) NOT NULL
);

ALTER TABLE t_bandeira_cartao ADD CONSTRAINT t_bandeira_cartao_pk PRIMARY KEY ( cd_bandeira );

CREATE TABLE t_cartao (
    cd_cartao                     NUMBER(3) NOT NULL,
    t_usuario_cod_usuario         NUMBER(3) NOT NULL,
    t_bandeira_cartao_cd_bandeira NUMBER(3) NOT NULL,
    t_tipo_cartao_cd_tipo_cartao  NUMBER(3) NOT NULL
);

ALTER TABLE t_cartao ADD CONSTRAINT t_cartao_pk PRIMARY KEY ( cd_cartao );

CREATE TABLE t_categoria_investimento (
    cd_categoria_investimento NUMBER(5) NOT NULL,
    ds_categoria_investimento VARCHAR2(30 CHAR) NOT NULL
);

ALTER TABLE t_categoria_investimento ADD CONSTRAINT t_categoria_investimento_pk PRIMARY KEY ( cd_categoria_investimento );

CREATE TABLE t_categoria_item (
    cd_categoria_item NUMBER(5) NOT NULL,
    ds_categoria      VARCHAR2(30 CHAR) NOT NULL
);

ALTER TABLE t_categoria_item ADD CONSTRAINT t_categoria_item_pk PRIMARY KEY ( cd_categoria_item );

CREATE TABLE t_cidade (
    cd_cidade NUMBER(3) NOT NULL,
    nm_cidade VARCHAR2(100) NOT NULL
);

ALTER TABLE t_cidade ADD CONSTRAINT t_cidade_pk PRIMARY KEY ( cd_cidade );

CREATE TABLE t_conta_bancaria (
    cd_conta_bancaria          NUMBER(3) NOT NULL,
    nr_agencia                 NUMBER(5) NOT NULL,
    nr_conta_bancaria          NUMBER(10) NOT NULL,
    nr_digito_conta            NUMBER(2) NOT NULL,
    t_usuario_cod_usuario      NUMBER(3) NOT NULL,
    t_banco_cd_banco           NUMBER(3) NOT NULL,
    t_tipo_conta_cd_tipo_conta NUMBER(3) NOT NULL
);

ALTER TABLE t_conta_bancaria ADD CONSTRAINT t_conta_bancaria_pk PRIMARY KEY ( cd_conta_bancaria );

CREATE TABLE t_ddd (
    cd_ddd NUMBER(3) NOT NULL,
    nr_ddd NUMBER(3) NOT NULL
);

ALTER TABLE t_ddd ADD CONSTRAINT t_ddd_pk PRIMARY KEY ( cd_ddd );

CREATE TABLE t_ddi (
    cd_ddi NUMBER(3) NOT NULL,
    nr_ddi VARCHAR2(5) NOT NULL
);

ALTER TABLE t_ddi ADD CONSTRAINT t_ddi_pk PRIMARY KEY ( cd_ddi );

CREATE TABLE t_estado (
    cd_estado NUMBER(3) NOT NULL,
    nm_estado VARCHAR2(100 CHAR) NOT NULL
);

ALTER TABLE t_estado ADD CONSTRAINT t_estado_pk PRIMARY KEY ( cd_estado );

CREATE TABLE t_genero (
    cd_genero             NUMBER(2) NOT NULL,
    ds_genero             VARCHAR2(30 CHAR) NOT NULL,
    t_usuario_cod_usuario NUMBER(3) NOT NULL
);

CREATE UNIQUE INDEX t_genero__idx ON
    t_genero (
        t_usuario_cod_usuario
    ASC );

ALTER TABLE t_genero ADD CONSTRAINT t_genero_pk PRIMARY KEY ( cd_genero );

CREATE TABLE t_login (
    nr_cpf                NUMBER(11) NOT NULL,
    nr_senha              VARCHAR2(8 CHAR) NOT NULL,
    t_usuario_cod_usuario NUMBER(3) NOT NULL
);

CREATE UNIQUE INDEX t_login__idx ON
    t_login (
        t_usuario_cod_usuario
    ASC );

ALTER TABLE t_login ADD CONSTRAINT t_login_pk PRIMARY KEY ( nr_cpf );

CREATE TABLE t_movimentacao (
    cd_movimentacao                                    NUMBER(5) NOT NULL,
    dt_data                                            DATE NOT NULL,
    nr_valor                                           NUMBER(7, 2) NOT NULL,
    ds_item                                            VARCHAR2(25 CHAR) NOT NULL,
    t_usuario_cod_usuario                              NUMBER(3) NOT NULL, 
--  ERROR: Column name length exceeds maximum allowed length(30) 
    t_tipo_movimentacao_cd_tipo_movimentacao           NUMBER(3) NOT NULL,
    t_login_nr_cpf                                     NUMBER(11) NOT NULL, 
--  ERROR: Column name length exceeds maximum allowed length(30) 
    t_categoria_item_cd_categoria_item                 NUMBER(5) NOT NULL, 
--  ERROR: Column name length exceeds maximum allowed length(30) 
    t_categoria_investimento_cd_categoria_investimento NUMBER(5) NOT NULL, 
--  ERROR: Column name length exceeds maximum allowed length(30) 
    t_tipo_investimento_cd_investimento                NUMBER(5) NOT NULL
);

ALTER TABLE t_movimentacao ADD CONSTRAINT t_movimentacao_pk PRIMARY KEY ( cd_movimentacao,
                                                                          t_tipo_movimentacao_cd_tipo_movimentacao );

CREATE TABLE t_pais (
    cd_pais NUMBER(3) NOT NULL,
    nm_pais VARCHAR2(100 CHAR) NOT NULL
);

ALTER TABLE t_pais ADD CONSTRAINT t_pais_pk PRIMARY KEY ( cd_pais );

CREATE TABLE t_telefone (
    cd_telefone             NUMBER(3) NOT NULL,
    nr_telefone             NUMBER(9),
    t_usuario_cod_usuario   NUMBER(3) NOT NULL,
    t_ddi_cd_ddi            NUMBER(3) NOT NULL,
    t_ddd_cd_ddd            NUMBER(3) NOT NULL,
    t_tipo_telefone_cd_tipo NUMBER(3) NOT NULL
);

ALTER TABLE t_telefone ADD CONSTRAINT t_telefone_pk PRIMARY KEY ( cd_telefone );

CREATE TABLE t_tipo_cartao (
    cd_tipo_cartao NUMBER(3) NOT NULL,
    ds_tipo_cartao VARCHAR2(30) NOT NULL
);

ALTER TABLE t_tipo_cartao ADD CONSTRAINT t_tipo_cartao_pk PRIMARY KEY ( cd_tipo_cartao );

CREATE TABLE t_tipo_conta (
    cd_tipo_conta     NUMBER(3) NOT NULL,
    ds_conta_bancaria VARCHAR2(20) NOT NULL
);

ALTER TABLE t_tipo_conta ADD CONSTRAINT t_tipo_conta_pk PRIMARY KEY ( cd_tipo_conta );

CREATE TABLE t_tipo_investimento (
    cd_investimento      NUMBER(5) NOT NULL,
    ds_tipo_investimento VARCHAR2(35 CHAR) NOT NULL
);

ALTER TABLE t_tipo_investimento ADD CONSTRAINT t_tipo_investimento_pk PRIMARY KEY ( cd_investimento );

CREATE TABLE t_tipo_movimentacao (
    cd_tipo_movimentacao NUMBER(3) NOT NULL,
    ds_movimentacao      VARCHAR2(30) NOT NULL
);

ALTER TABLE t_tipo_movimentacao ADD CONSTRAINT t_tipo_movimentacao_pk PRIMARY KEY ( cd_tipo_movimentacao );

CREATE TABLE t_tipo_telefone (
    cd_tipo          NUMBER(3) NOT NULL,
    ds_tipo_telefone VARCHAR2(25) NOT NULL
);

ALTER TABLE t_tipo_telefone ADD CONSTRAINT t_tipo_telefone_pk PRIMARY KEY ( cd_tipo );

CREATE TABLE t_usuario (
    cod_usuario        NUMBER(3) NOT NULL,
    nm_nome_completo   VARCHAR2(150 CHAR) NOT NULL,
    dt_data_nascimento DATE NOT NULL,
    tx_email           VARCHAR2(100 CHAR),
    t_login_nr_cpf     NUMBER(11) NOT NULL,
    t_genero_cd_genero NUMBER(2) NOT NULL,
    t_cidade_cd_cidade NUMBER(3) NOT NULL,
    t_estado_cd_estado NUMBER(3) NOT NULL,
    t_pais_cd_pais     NUMBER(3) NOT NULL
);

CREATE UNIQUE INDEX t_usuario__idx ON
    t_usuario (
        t_login_nr_cpf
    ASC );

CREATE UNIQUE INDEX t_usuario__idxv1 ON
    t_usuario (
        t_genero_cd_genero
    ASC );

ALTER TABLE t_usuario ADD CONSTRAINT t_usuario_pk PRIMARY KEY ( cod_usuario );

ALTER TABLE t_cartao
    ADD CONSTRAINT t_cartao_t_bandeira_cartao_fk FOREIGN KEY ( t_bandeira_cartao_cd_bandeira )
        REFERENCES t_bandeira_cartao ( cd_bandeira );

ALTER TABLE t_cartao
    ADD CONSTRAINT t_cartao_t_tipo_cartao_fk FOREIGN KEY ( t_tipo_cartao_cd_tipo_cartao )
        REFERENCES t_tipo_cartao ( cd_tipo_cartao );

ALTER TABLE t_cartao
    ADD CONSTRAINT t_cartao_t_usuario_fk FOREIGN KEY ( t_usuario_cod_usuario )
        REFERENCES t_usuario ( cod_usuario );

ALTER TABLE t_conta_bancaria
    ADD CONSTRAINT t_conta_bancaria_t_banco_fk FOREIGN KEY ( t_banco_cd_banco )
        REFERENCES t_banco ( cd_banco );

--  ERROR: FK name length exceeds maximum allowed length(30) 
ALTER TABLE t_conta_bancaria
    ADD CONSTRAINT t_conta_bancaria_t_tipo_conta_fk FOREIGN KEY ( t_tipo_conta_cd_tipo_conta )
        REFERENCES t_tipo_conta ( cd_tipo_conta );

ALTER TABLE t_conta_bancaria
    ADD CONSTRAINT t_conta_bancaria_t_usuario_fk FOREIGN KEY ( t_usuario_cod_usuario )
        REFERENCES t_usuario ( cod_usuario );

ALTER TABLE t_genero
    ADD CONSTRAINT t_genero_t_usuario_fk FOREIGN KEY ( t_usuario_cod_usuario )
        REFERENCES t_usuario ( cod_usuario );

ALTER TABLE t_login
    ADD CONSTRAINT t_login_t_usuario_fk FOREIGN KEY ( t_usuario_cod_usuario )
        REFERENCES t_usuario ( cod_usuario );

--  ERROR: FK name length exceeds maximum allowed length(30) 
ALTER TABLE t_movimentacao
    ADD CONSTRAINT t_movimentacao_t_categoria_investimento_fk FOREIGN KEY ( t_categoria_investimento_cd_categoria_investimento )
        REFERENCES t_categoria_investimento ( cd_categoria_investimento );

--  ERROR: FK name length exceeds maximum allowed length(30) 
ALTER TABLE t_movimentacao
    ADD CONSTRAINT t_movimentacao_t_categoria_item_fk FOREIGN KEY ( t_categoria_item_cd_categoria_item )
        REFERENCES t_categoria_item ( cd_categoria_item );

ALTER TABLE t_movimentacao
    ADD CONSTRAINT t_movimentacao_t_login_fk FOREIGN KEY ( t_login_nr_cpf )
        REFERENCES t_login ( nr_cpf );

--  ERROR: FK name length exceeds maximum allowed length(30) 
ALTER TABLE t_movimentacao
    ADD CONSTRAINT t_movimentacao_t_tipo_investimento_fk FOREIGN KEY ( t_tipo_investimento_cd_investimento )
        REFERENCES t_tipo_investimento ( cd_investimento );

--  ERROR: FK name length exceeds maximum allowed length(30) 
ALTER TABLE t_movimentacao
    ADD CONSTRAINT t_movimentacao_t_tipo_movimentacao_fk FOREIGN KEY ( t_tipo_movimentacao_cd_tipo_movimentacao )
        REFERENCES t_tipo_movimentacao ( cd_tipo_movimentacao );

ALTER TABLE t_movimentacao
    ADD CONSTRAINT t_movimentacao_t_usuario_fk FOREIGN KEY ( t_usuario_cod_usuario )
        REFERENCES t_usuario ( cod_usuario );

ALTER TABLE t_telefone
    ADD CONSTRAINT t_telefone_t_ddd_fk FOREIGN KEY ( t_ddd_cd_ddd )
        REFERENCES t_ddd ( cd_ddd );

ALTER TABLE t_telefone
    ADD CONSTRAINT t_telefone_t_ddi_fk FOREIGN KEY ( t_ddi_cd_ddi )
        REFERENCES t_ddi ( cd_ddi );

ALTER TABLE t_telefone
    ADD CONSTRAINT t_telefone_t_tipo_telefone_fk FOREIGN KEY ( t_tipo_telefone_cd_tipo )
        REFERENCES t_tipo_telefone ( cd_tipo );

ALTER TABLE t_telefone
    ADD CONSTRAINT t_telefone_t_usuario_fk FOREIGN KEY ( t_usuario_cod_usuario )
        REFERENCES t_usuario ( cod_usuario );

ALTER TABLE t_usuario
    ADD CONSTRAINT t_usuario_t_cidade_fk FOREIGN KEY ( t_cidade_cd_cidade )
        REFERENCES t_cidade ( cd_cidade );

ALTER TABLE t_usuario
    ADD CONSTRAINT t_usuario_t_estado_fk FOREIGN KEY ( t_estado_cd_estado )
        REFERENCES t_estado ( cd_estado );

ALTER TABLE t_usuario
    ADD CONSTRAINT t_usuario_t_genero_fk FOREIGN KEY ( t_genero_cd_genero )
        REFERENCES t_genero ( cd_genero );

ALTER TABLE t_usuario
    ADD CONSTRAINT t_usuario_t_login_fk FOREIGN KEY ( t_login_nr_cpf )
        REFERENCES t_login ( nr_cpf );

ALTER TABLE t_usuario
    ADD CONSTRAINT t_usuario_t_pais_fk FOREIGN KEY ( t_pais_cd_pais )
        REFERENCES t_pais ( cd_pais );



-- Relatório do Resumo do Oracle SQL Developer Data Modeler: 
-- 
-- CREATE TABLE                            21
-- CREATE INDEX                             4
-- ALTER TABLE                             44
-- CREATE VIEW                              0
-- ALTER VIEW                               0
-- CREATE PACKAGE                           0
-- CREATE PACKAGE BODY                      0
-- CREATE PROCEDURE                         0
-- CREATE FUNCTION                          0
-- CREATE TRIGGER                           0
-- ALTER TRIGGER                            0
-- CREATE COLLECTION TYPE                   0
-- CREATE STRUCTURED TYPE                   0
-- CREATE STRUCTURED TYPE BODY              0
-- CREATE CLUSTER                           0
-- CREATE CONTEXT                           0
-- CREATE DATABASE                          0
-- CREATE DIMENSION                         0
-- CREATE DIRECTORY                         0
-- CREATE DISK GROUP                        0
-- CREATE ROLE                              0
-- CREATE ROLLBACK SEGMENT                  0
-- CREATE SEQUENCE                          0
-- CREATE MATERIALIZED VIEW                 0
-- CREATE MATERIALIZED VIEW LOG             0
-- CREATE SYNONYM                           0
-- CREATE TABLESPACE                        0
-- CREATE USER                              0
-- 
-- DROP TABLESPACE                          0
-- DROP DATABASE                            0
-- 
-- REDACTION POLICY                         0
-- 
-- ORDS DROP SCHEMA                         0
-- ORDS ENABLE SCHEMA                       0
-- ORDS ENABLE OBJECT                       0
-- 
-- ERRORS                                   9
-- WARNINGS                                 0
