from google.appengine.ext import db
from google.appengine.ext.db import polymodel
import json
from google.appengine.api import memcache


# GOOGLE DATASTORE MODELS

class Articolo(db.Model):
    '''
       Classe che definisce un qualunque Articolo di un qualunque Codice
    '''
    numero               = db.StringProperty(required = True)
    testo                = db.StringProperty(required = True)
    argomenti            = db.StringListProperty(default=[])
    Codice               = db.StringProperty(required = True, choices=['Costituzione', 'CodiceCivile'])
    Parte                = db.StringProperty(default='None', choices=['PrincipiFondamentali', 'Prima', 'Seconda','Terza', 'Quarta', 'Quinta'])
    Titolo               = db.StringProperty(default='None', choices=['I', 'II','III', 'IV', 'V', 'VI', 'VII'])
    Libro                = db.StringProperty(default='None', choices=['I', 'II','III', 'IV', 'V', 'VI', 'VII'])
    Sezione              = db.StringProperty(default='None', choices=['I', 'II','III', 'IV', 'V', 'VI', 'VII'])
    Capo                 = db.StringProperty(default='None', choices=['I', 'II','III', 'IV', 'V', 'VI', 'VII'])
    risorse              = db.ListProperty(db.Key) # un articolo = + Risorse possibili

class Dettaglio(db.Expando):
    '''
       Classe che descrive i dettagli che possono accompagnare un Autore, una Fonte, una Risorsa
    '''
    riferito_a          = db.ReferenceProperty()
    testo               = db.StringProperty(required = True)
    
class Risorsa(db.Model):
    '''
       Classe che descrive una risorsa
    '''
    tipo                 = db.StringProperty(default='None', choices=['commento', 'Storia', 'multimedia', 'link', 'legge dello Stato'])
    testo                = db.StringProperty(default='None') # testo commento o spiegazione risorsa/link
    url                  = db.StringProperty(default='None')
    autore               = db.ListProperty(db.Key) # una risorsa = + Autori possibili
    fonte                = db.ListProperty(db.Key) # una risorsa = + Fonti possibili
    dettagli             = db.ReferenceProperty(Dettaglio, collection_name='resource_details')
    
class Pagina(db.Model):
    '''
       Classe che descrive il contenuto di una pagina riferita ad un articolo
    '''
    articolo             = db.ReferenceProperty(Articolo, collection_name='wiki_article')
    title                = db.StringProperty(default='None')
    
class Fonte(db.Expando):
    '''
       Classe che descrive una fonte
    '''
    tipoFonte           = db.StringProperty(required = True, choices=['Governo', 'Parlamento', 'Accademico', 'Commentatore', 'Costituizionalista', 'Giornalista'])
    dettagli            = db.ReferenceProperty(Dettaglio)
  
  
class Autore(db.Expando):
    '''
       Classe che descrive un autore
    '''
    nome                = db.StringProperty()
    cognome             = db.StringProperty()
    dettagli            = db.ReferenceProperty(Dettaglio)
    
class Argomento(db.Expando):
    tag                 = db.StringProperty()
    dettagli             = db.ReferenceProperty(Dettaglio, collection_name='tag_details')
    
    
    
