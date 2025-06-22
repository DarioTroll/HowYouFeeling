drop database health;
create database health;
use health;

CREATE TABLE Dolore (
    codice INT AUTO_INCREMENT PRIMARY KEY,
    data DATE NOT NULL,
    ora TIME NOT NULL,

    -- TESTA
    viso INT,
    testa_fronte INT,
    testa_tempie_dx INT,
    testa_tempie_sx INT,
    testa_sommità INT,
    testa_occipite INT,
    nuca INT,

    -- MASCELLA E DENTI
    mascella_dx INT,
    mascella_sx INT,
    denti INT,

    -- COLLO E SPALLE
    collo INT,
    spalla_dx INT,
    spalla_sx INT,

    -- BRACCIA E MANI
    braccio_superiore_dx INT,
    braccio_superiore_sx INT,
    braccio_inferiore_dx INT,
    braccio_inferiore_sx INT,
    gomito_dx INT,
    gomito_sx INT,
    polso_dx INT,
    polso_sx INT,
    mano_dx INT,
    mano_sx INT,
    dito_dx INT,
    dito_sx INT,

    -- TORACE E ADDOME
    petto_superiore_dx INT,
    petto_superiore_sx INT,
    petto_centrale INT,
    pancia INT,
    addome_superiore INT,
    addome_inferiore INT,

    -- SCHIENA
    schiena_superiore_dx INT,
    schiena_superiore_sx INT,
    schiena_inferiore_dx INT,
    schiena_inferiore_sx INT,
    sedere_dx INT,
    sedere_sx INT,

    -- GAMBE
    gamba_superiore_dx INT,
    gamba_superiore_sx INT,
    ginocchio_dx INT,
    ginocchio_sx INT,
    polpaccio_dx INT,
    polpaccio_sx INT,
    caviglia_dx INT,
    caviglia_sx INT,
    piede_dx INT,
    piede_sx INT
);

CREATE TABLE Umore (
    codice INT AUTO_INCREMENT PRIMARY KEY,
    data DATE NOT NULL,
    ora TIME NOT NULL,
    ansia INT,
    energia INT,
    soddisfazione INT,
    felicita INT,
    stress INT 
);

CREATE TABLE Sonno (
    codice INT AUTO_INCREMENT PRIMARY KEY,
    data DATE NOT NULL,
    ora TIME NOT NULL,
    ora_inizio TIME NOT NULL,
    ora_fine TIME NOT NULL,
    qualita INT
);
