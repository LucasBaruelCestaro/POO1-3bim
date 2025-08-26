CREATE DATABASE univap;
USE univap;

CREATE TABLE disciplinas (
  codigodisc int NOT NULL,
  nomedisc varchar(50) DEFAULT NULL,
  PRIMARY KEY (codigodisc)
);


CREATE TABLE professores (
  registro int NOT NULL,
  nomeprof varchar(50) DEFAULT NULL,
  telefoneprof varchar(50) DEFAULT NULL,
  idadeprof int DEFAULT NULL,
  salarioprof float DEFAULT NULL,
  PRIMARY KEY (registro)
);


CREATE TABLE disciplinasxprofessores (
  codigodisciplinanocurso int NOT NULL,
  coddisciplina int DEFAULT NULL,
  codprofessor int DEFAULT NULL,
  curso int DEFAULT NULL,
  cargahoraria int DEFAULT NULL,
  anoletivo int DEFAULT NULL,
  PRIMARY KEY (codigodisciplinanocurso),
  FOREIGN KEY (coddisciplina) REFERENCES disciplinas (codigodisc),
  FOREIGN KEY (codprofessor) REFERENCES professores (registro)
);

insert into professores(registro, nomeprof, telefoneprof, idadeprof, salarioprof) values (1, "Lucas", "12996531108", 16, 3400.00);
select * from professores;