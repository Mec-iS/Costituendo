TABLE Articolo:
    '''
       Tabella che definisce un qualunque Articolo di un qualunque Codice
    '''
    id                   > INT(12)
    numero               > INT(10) required=True
    testo                > TEXT required=True
    Codice               > VARCHAR(25) required = True choices?=['Costituzione', 'CodiceCivile']
    Parte                > VARCHAR(10) choices?=['PrincipiFondamentali', 'Prima', 'Seconda','Terza', 'Quarta', 'Quinta']
    Titolo               > VARCHAR(10) choices?=['I', 'II','III', 'IV', 'V', 'VI', 'VII']
    Libro                > VARCHAR(10) choices?=['I', 'II','III', 'IV', 'V', 'VI', 'VII']
    Sezione              > VARCHAR(10) choices?=['I', 'II','III', 'IV', 'V', 'VI', 'VII']
    Capo                 > VARCHAR(10) choices?=['I', 'II','III', 'IV', 'V', 'VI', 'VII']


TABLE Dettaglio:
    '''
       Tabella che descrive i dettagli che possono accompagnare un Autore, una Fonte, una Risorsa
    '''
    id                   > INT(12)
    riferito_a           > FK #(Fonte o  Autore o Argomento)
    testo                > TEXT required=True
    
TABLE Risorsa:
    '''
       Tabella che descrive una risorsa
    '''
    id                   > INT(12)
    categoria            > VARCHAR(50) required=True choices?=['esegesi', 'Storia', 'link', 'dottrina', 'giurisprudenza', 'normativa', 'attualita', 'dati']
    contenuto            > TEXT required=True # testo commento o spiegazione risorsa/link
    url                  > VARCHAR(80)
    autore               > db.ListProperty(db.Key) # una risorsa = + Autori possibili
    fonte                > db.ListProperty(db.Key) # una risorsa = + Fonti possibili
    dettaglio            > FK #Dettaglio
    
TABLE Pagina:
    '''
       Tabella che descrive il contenuto di una pagina riferita ad un articolo
    '''
    id                   > INT(12)
    titolo               > VARCHAR(80) required=True
    html                 > TEXT # HTML string
    
TABLE Fonte:
    '''
       Tabella che descrive una fonte
    '''
    id                   > INT(12)
    tipo                 > VARCHAR(50) required=True choices?=['Legge', 'Accademico', 'Commentatore', 'Costituizionalista', 'Giornalista',
                                                         'Organo Giurisdizionale', 'TAR', 'Corte Costituzionale', 'Presidente della Repubblica']
    dettaglio            > FK #Dettaglio
  
  
TABLE Autore:
    '''
       Tabella che descrive un autore
    '''
    id                   > INT(12)
    titolo               > VARCHAR(25) required=True choices?=['Governo', 'Parlamento', 'Prof.', 'Dott.', 'Avv.', 'Sig.', 'Sig.ra']
    nome                 > VARCHAR(50)
    cognome              > VARCHAR(50)
    dettagli             > FK #Dettaglio
    
TABLE Argomento:
    id                   > INT(12)
    tag                  > VARCHAR(25)
    dettaglio            > FK #Dettaglio

TABLE Openius:
    '''
       Tabella delle relazioni che vanno ad ordinare i dati presenti in Openius
    '''
    id_articolo          > 
    ids_risorsa          >
    ids_autore           >
    ids__fonte           >
    ids_argomento        >
    id_pagina_corrente   >
    


'''
TABLE Dati:
  #Possibile implementazione futura
    id                   > INT(12)
    formato              > VARCHAR(20) choices?=['pdf', 'json', 'csv', 'xcl']
    contenuto            >
'''

