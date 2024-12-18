-- Création par Dowson et Wiktor

CREATE TABLE alerte (
  PRIMARY KEY (alerte_id),
  alerte_id     INT NOT NULL AUTO_INCREMENT,
  alerte_type   ENUM('lit', 'equipement'),
  alerte_description   VARCHAR(255),
  resolu        BOOLEAN,
  date_creation DATE DEFAULT NOW()
);

CREATE TABLE departement (
  PRIMARY KEY (departement_id),
  departement_id  INT NOT NULL AUTO_INCREMENT,
  departement_nom VARCHAR(255),
  departement_description     VARCHAR(255)
);

CREATE TABLE alerte_departement (
    PRIMARY KEY (alerte_departement_id),
    alerte_departement_id INT NOT NULL AUTO_INCREMENT,
    alerte_id INT NOT NULL,
    FOREIGN KEY(alerte_id) REFERENCES alerte(alerte_id),
    departement_id INT NOT NULL,
    FOREIGN KEY(departement_id) REFERENCES departement(departement_id)
);


CREATE TABLE equipement (
  PRIMARY KEY (equipement_id),
  equipement_id     INT NOT NULL AUTO_INCREMENT,
  type_equipement              VARCHAR(255),
  disponible           BOOLEAN DEFAULT 1,
  date_modification DATE DEFAULT NOW(),
  departement_id    INT NOT NULL,
   FOREIGN KEY(departement_id) REFERENCES departement(departement_id)
);

CREATE TABLE lit (
  PRIMARY KEY (lit_id),
  lit_id            INT NOT NULL AUTO_INCREMENT,
  disponible        BOOLEAN DEFAULT 1,
  type_lit          ENUM('Standard', 'Pédiatrique', 'Intensif'),
  date_creation     DATE DEFAULT NOW(),
  date_modification DATE DEFAULT NOW(),
  chambre        INT
);

CREATE TABLE patient (
  PRIMARY KEY (patient_id),
  patient_id        INT NOT NULL AUTO_INCREMENT,
  nom               VARCHAR(255),
  prenom            VARCHAR(255),
  date_naissance    DATE,
  contact           VARCHAR(255),
  adresse           VARCHAR(255),
  actif             BOOLEAN,
  date_creation     DATE DEFAULT NOW(),
  date_modification DATE DEFAULT NOW(),
  lit_id            INT,
  FOREIGN KEY(lit_id) REFERENCES lit(lit_id),
  departement_id INT,
  FOREIGN KEY(departement_id) REFERENCES departement(departement_id)
);

CREATE TABLE personnel_medical (
  PRIMARY KEY (personned_medical_id),
  personned_medical_id int NOT NULL,
  nom                  VARCHAR(255),
  prenom               VARCHAR(255),
  date_naissance       DATE,
  contact              VARCHAR(255),
  adresse              VARCHAR(255),
  specialite           VARCHAR(255),
  date_creation        DATE DEFAULT NOW(),
  date_modification    DATE DEFAULT NOW(),
  departement_id       INT,
  FOREIGN KEY(departement_id) REFERENCES departement(departement_id)
);

CREATE TABLE transfert_medical (
  PRIMARY KEY (tranfert_id),
  tranfert_id             INT NOT NULL AUTO_INCREMENT,
  raison                  VARCHAR(255),
  date_creation           DATE DEFAULT NOW(),
  transfert_status        BOOLEAN,              
  departement_source      INT NOT NULL,
   FOREIGN KEY(departement_source) REFERENCES departement(departement_id),
  patient_id              INT NOT NULL,
   FOREIGN KEY(patient_id) REFERENCES patient(patient_id),
  departement_destination INT NOT NULL,
   FOREIGN KEY(departement_destination) REFERENCES departement(departement_id)
);

INSERT INTO departement (departement_id, departement_nom, departement_description) VALUES (1, "Général", ""), (2, "Pédiatrie", ""), (3, "Soins Intensif", ""), (4, "Réhabilitation", "");



DELIMITER $$

CREATE PROCEDURE InsertEquipementIntensif()
BEGIN
    DECLARE i INT DEFAULT 1;
    DECLARE dep INT DEFAULT 0;

-- Global --------------------------------------------------------



-- Departement 1(Général) -------------------------------------------------

    SET dep = 1;


-- Departement 3 (Soins Intensifs) --------------------------------------------------

    SET dep = 3;



    -- Equipement -----------------------------
    WHILE i <= 43 DO
        INSERT INTO equipement (type_equipement, departement_id)
        VALUES ('Moniteur de fréquence cardiaque', dep);
        SET i = i + 1;
    END WHILE;

    SET i = 1; 

    WHILE i <= 60 DO
        INSERT INTO equipement (type_equipement, departement_id)
        VALUES ('Moniteur de respiration', dep);
        SET i = i + 1;
    END WHILE;

    SET i = 1;

    WHILE i <= 75 DO
        INSERT INTO equipement (type_equipement, departement_id)
        VALUES ('Moniteur de température', dep);
        SET i = i + 1;
    END WHILE;

    SET i = 1;

    WHILE i <= 102 DO
        INSERT INTO equipement (type_equipement, departement_id)
        VALUES ('Appareil de surveillance de la saturation en oxygène', dep);
        SET i = i + 1;
    END WHILE;

    SET i = 1;

    WHILE i <= 15 DO
        INSERT INTO equipement (type_equipement, departement_id)
        VALUES ('Moniteur multiparamétrique', dep);
        SET i = i + 1;
    END WHILE;

    SET i = 1;

    WHILE i <= 32 DO
        INSERT INTO equipement (type_equipement, departement_id)
        VALUES ('Ventilateur mécanique', dep);
        SET i = i + 1;
    END WHILE;

    SET i = 1;

    WHILE i <= 106 DO
        INSERT INTO equipement (type_equipement, departement_id)
        VALUES ('Appareil de perfusion intraveineuse', dep);
        SET i = i + 1;
    END WHILE;



-- Departement 2 (Pédiatrie) ------------------------------------------------------

    SET i = 1;
    SET dep = 2;

    -- Chambres ------------------------------------------------
  

    -- Equipement ----------------------------------------------
    WHILE i <= 50 DO
        INSERT INTO equipement (type_equipement, departement_id)
        VALUES ('Stéthoscope Pédiatrique', dep);
        SET i = i + 1;
    END WHILE;

    SET i = 1;

    WHILE i <= 150 DO
        INSERT INTO equipement (type_equipement, departement_id)
        VALUES ('Thérmomètre médical', dep);
        SET i = i + 1;
    END WHILE;

    SET i = 1;

    WHILE i <= 175 DO
        INSERT INTO equipement (type_equipement, departement_id)
        VALUES ('Oxymètre de pouls', dep);
        SET i = i + 1;
    END WHILE;

    SET i = 1;

    WHILE i <= 25 DO
        INSERT INTO equipement (type_equipement, departement_id)
        VALUES ("Appareils d'échographie pédiatrique", dep);
        SET i = i + 1;
    END WHILE;

    SET i = 1;

    WHILE i <= 200 DO
        INSERT INTO equipement (type_equipement, departement_id)
        VALUES ('Tensiomètre pédiatrique', dep);
        SET i = i + 1;
    END WHILE;

    SET i = 1;

    WHILE i <= 110 DO
        INSERT INTO equipement (type_equipement, departement_id)
        VALUES ('Inhalateur et nébuliseur', dep);
        SET i = i + 1;
    END WHILE;

    SET i = 1;

    WHILE i <= 60 DO
        INSERT INTO equipement (type_equipement, departement_id)
        VALUES ('Moniteur cardiaque', dep);
        SET i = i + 1;
    END WHILE;

-- Département 4 (Réhabilitation) ------------------------------------------------

    SET i = 1;
    SET dep = 4;

    

    -- Equipement --------------------------
    WHILE i <= 15 DO
        INSERT INTO equipement (type_equipement, departement_id)
        VALUES ("Exosquelette pédiatrique", dep);
        SET i = i + 1;
    END WHILE;

    SET i = 1;

    WHILE i <= 62 DO
        INSERT INTO equipement (type_equipement, departement_id)
        VALUES ('Tapis roulant et appareils de marche pour enfant', dep);
        SET i = i + 1;
    END WHILE;

    SET i = 1;

    WHILE i <= 94 DO
        INSERT INTO equipement (type_equipement, departement_id)
        VALUES ('Valos stationnaire pédiatrique', dep);
        SET i = i + 1;
    END WHILE;

    SET i = 1;

    WHILE i <= 26 DO
        INSERT INTO equipement (type_equipement, departement_id)
        VALUES ('Appareils de mobilisation passive continue', dep);
        SET i = i + 1;
    END WHILE;

    SET i = 1;

    WHILE i <= 46 DO
        INSERT INTO equipement (type_equipement, departement_id)
        VALUES ('Appareils de stimulation nerveuse électrique transcutanée', dep);
        SET i = i + 1;
    END WHILE;

    -- global --

    SET i = 0;

    WHILE i <= 300 DO 
        INSERT INTO lit(type_lit) 
        VALUES ('Standard') ;
        SET i = i + 1 ;
    END WHILE;

    SET i = 0;

    WHILE i <= 120 DO 
        INSERT INTO lit(type_lit) 
        VALUES ('Pédiatrique') ;
        SET i = i + 1 ;
    END WHILE;

    SET i = 0;

    WHILE i <= 100 DO 
        INSERT INTO lit(type_lit) 
        VALUES ('Intensif') ;
        SET i = i + 1 ;
    END WHILE;





END$$

DELIMITER ;

CALL InsertEquipementIntensif();
DROP PROCEDURE InsertEquipementIntensif;