-- SOLO UNA BOZZA: DA AGGIUNGERE FOREIGN KEYS

/*
Table to host all LAWS (Codexes) of a specific country. In this table only the main data will appear
        
        1, 'Costituzione', 1948, 0
        2, 'Codice Civile', 19??, 0
        3, 'Codice Penale', 19??, 0
*/

CREATE TABLE laws(
    id                  SERIAL primary key, -- Autoincremental ID of the law 
    name                VARCHAR(20) NOT NULL, -- Name of the law 
    became              DATE NOT NULL        -- Date when became a law 
);

/*
Table to host all laws SECTIONS.

        1, 1, 0, 'Principi fondamentali', 1
        2, 1, 0, 'Parte prima', 1
        3, 1, 2, 'Titolo I', 1
        4, 1, 2, 'Titolo II', 2
*/

CREATE TABLE sections(
    id                  SERIAL primary key, -- Autoincremental ID of the section
    law_id              > FK(laws), -- Foreign Key pointing to the law which the section is part of
    parent_id           > FK(sections) default=0, -- Section that contain this section (if none, 0 will appear)
    name                VARCHAR(50) NOT NULL, -- Name of the section
    description         VARCHAR(50) NOT NULL, -- Formal description of the section
    order               INT -- Order to be able to sort in a selection
);

CREATE TABLE articles(
    id                  SERIAL primary key,
    number              INT NOT NULL,
    text                TEXT NOT NULL,
    law_id              > FK(laws),
    section_id          > FK(sections)
);

-- Resources: RESOURCES connected to some article

CREATE TABLE resources(
    id                  SERIAL primary key,
    category_id         > FK(resource_categories),
    text                TEXT NOT NULL,
    url                 VARCHAR(255),
    author              > FK(authors),
    source              > FK(sources)
);

/*  RESOURCES have RESOURCE_CATEGORIES 
    possible names = ['esegesi', 'Storia', 'link', 'dottrina', 
                     'giurisprudenza', 'normativa', 'attualita', 'dati'] 
*/

CREATE TABLE resource_categories(
    id                  SERIAL primary key,
    name                VARCHAR(100) NOT NULL
);

/*
    RESOURCES have RESOURCE_FIELDS for detailed informations about them 
*/    

CREATE TABLE resource_fields(
    id                  SERIAL primary key,
    resource_id         > FK(resources),
    key                 VARCHAR(50),
    value               TEXT
);

/*
    RESOURCES come from SOURCES
    possible name = ['Giudice', 'Avvocato', 'Accademico', 
                    'Organo Giurisdizionale', 'TAR', 'Corte Costituzionale', 'Presidente della Repubblica',
                    'Commentatore', 'Costituizionalista', 'Giornalista', 'Redattore OPEN-IUS', 'Utente']
*/

CREATE TABLE sources(   
    id                  SERIAL primary key,
    type_id             > FK(source_types),
    name                VARCHAR(50) NOT NULL
);
    
/*
    SOURCES have a SOURCE_TYPE
    possible name = ['Legge dello Stato', 'Opinione', 'Dichiarazione',
                    'Sentenza', 'Regolamento']
*/

CREATE TABLE source_type( 
    id                  SERIAL primary key,
    name                VARCHAR(50) NOT NULL
);

/*
    SOURCES have SOURCE_FIELDS for detailed informations about them 
*/

CREATE TABLE source_fields(
    id                  SERIAL primary key,
    source_id           > FK(sources),
    key                 VARCHAR(50),
    value               TEXT
);

/*
    RESOURCES have one or more AUTHORS:
    a person that expresses his/her own opinion 
    or that executes any public function 

*/

CREATE TABLE authors(
    id                  SERIAL primary key,
    title_id            > FK(titles),
    name                VARCHAR(50) NOT NULL, 
    surname             VARCHAR(50) NOT NULL
);

/*
    AUTHORS has TITLES:
    function = ['Membro del Governo', 'Parlamentare', 'Parte del Collegio giudicante', 'Funzionario',
                'Professisonista', 'Cittadino']
    name =  ['Prof.', 'Dott.', 'Avv.', 'Sig.', 'Sig.ra']
*/
CREATE TABLE author_titles(
    id                  SERIAL private key,
    name                VARCHAR(50),
    function            VARCHAR(50)
);

/*
    AUTHORS have AUTHOR_FIELDS for detailed informations about them 
*/

CREATE TABLE author_fields(
    id                  SERIAL primary key,
    author_id           > FK(authors),
    key                 VARCHAR(50),
    value               TEXT
);

/*
    RESOURCES have one or more TOPICS:
    job policy, welfare, education, etc.
*/

CREATE TABLE topics(
    id                   SERIAL private key,
    name                 VARCHAR(50) NOT NULL
);

/*
    TOPICS have TOPICS_FIELDS for detailed informations about them 
*/

CREATE TABLE topic_fields(
    id                  SERIAL private key,
    topic_id            > FK(topics)
    key                 VARCHAR(50),
    value               TEXT
);

/*
    REFERENCES TABLES
*/

CREATE TABLE author_topic( 
    author_id           > FK(authors)
    topic_id            > FK(topics)
);

CREATE TABLE resource_topic(
    resource_id         > FK(resources)
    topic_id            > FK(topics)
);

CREATE TABLE article_topic(
    article_id          > FK(articles)
    topic_id            > FK(topics)
);

CREATE TABLE law_topic(
    law_id              > FK(laws)
    topic_id            > FK(topics)
);
    
'''
TABLE Dati:
  #Possibile implementazione futura
    id                   > INT(12)
    formato              > VARCHAR(20) choices?=['pdf', 'json', 'csv', 'xcl'] 
    contenuto            > BLOB
'''
