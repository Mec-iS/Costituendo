from django.db import models

# !!! DEFAULT IS NULL=FALSE !!! 
class Law(models.Model):
    id                   = models.AutoField(primary_key=True)
    name                 = models.CharField(max_length=50)
    became               = models.DateField()
    
    def __unicode__(self):
        return self.name

class Section(models.Model):
    id                   = models.AutoField(primary_key=True)
    law_id               = models.ForeignKey(Law)
    parent_id            = models.ForeignKey('self', null=True, blank=True, default=None)
    name                 = models.CharField(max_length=140)
    description          = models.CharField(max_length=140, blank=True, default='')
    order                = models.IntegerField()
    
    def __unicode__(self):
        return self.name
    
class Article(models.Model):
    id                   = models.AutoField(primary_key=True)
    number               = models.IntegerField()
    text                 = models.TextField()
    law_id               = models.ForeignKey(Law)
    section_id           = models.ForeignKey(Section)
    
    def __unicode__(self):
        return self.number
    
class Resource(models.Model):
    id                   = models.AutoField(primary_key=True)
    article              = models.ForeignKey(Article)

class TextResource(Resource):
    CATEGORY = (
        (u'esegesi',        u'Esegesi'),
        (u'storia',         u'Storia'),
        (u'dottrina',       u'Dottrina'),
        (u'giurisprudenza', u'Giurisprudenza'),
        (u'normativa',      u'Normativa'),
        (u'attualita',      u'Attualita'),
        (u'citazione',      u'Citazione'),
    )
    text                 = models.TextField()
    category             = models.CharField(max_length=50, choices=CATEGORY)

class UrlResource(Resource):
    CATEGORY = (
       (u'link', u'link'),
       (u'video', u'video'),
       (u'audio', u'audio'),
    )
    description          = models.CharField(max_length=255)
    url                  = models.CharField(max_length=255)

class Source(models.Model):
    TYPES = (
        (u'legge',       u'Legge dello Stato'),
        (u'opinione',    u'Opinione'),
        (u'ufficiale',   u'Dichiarazione'),
        (u'sentenza',    u'Sentenza'),
        (u'regolamento', u'Regolamento'),
        (u'libro',       u'Pubblicazione giuridica'),
    )
    referred_to          = models.ForeignKey(Resource)
    id                   = models.AutoField(primary_key=True)
    type                 = models.CharField(max_length=50, choices=TYPES)
    name                 = models.CharField(max_length=140, choices=TYPES)
    details              = models.TextField(blank=True, default='')

class Author(models.Model):
    TITLES = (
        (u'prof',   u'Prof.'),
        (u'dott',   u'Dott.'),
        (u'avv',    u'Avv.'),
        (u'sig',    u'Sig.'),
        (u'sig_ra', u'Sig.ra'),
        (u'pres',   u'Presidente'),
        (u'ministro',   u'Ministro'),
    )
    FUNCTIONS = (
        (u'governo',     u'Membro del Governo'),
        (u'giudice',     u'Parte del Collegio giudicante'),
        (u'funzionario', u'Funzionario'),
        (u'profess',     u'Professionista'),
        (u'cittadino',   u'Cittadino'),
        
    )
    referred_to          = models.ForeignKey(Source)
    id                   = models.AutoField(primary_key=True)
    title                = models.CharField(max_length=50, choices=TITLES)
    name                 = models.CharField(max_length=140)
    surname              = models.CharField(max_length=140)
    function             = models.CharField(max_length=140, choices=FUNCTIONS)
    details              = models.TextField(blank=True, default='')
    
class Topic(models.Model):
    referred_to         = models.ForeignKey(Resource)
    key                 = models.CharField(max_length=50, unique=True)
    text                = models.TextField(blank=True, default='')

class Page(models.Model):
    id                  = models.AutoField(primary_key=True)
    slug                = models.SlugField(unique=True)
    title               = models.CharField(max_length=140)
    version             = models.IntegerField(default=0)
    html                = models.TextField()
    
'''
class DataResource(Resource):
    CATEGORY = (
       (u'pdf', u'pdf'),
       (u'csv', u'csv'),
       (u'json', u'json'),
    )
    file                = models.FileField(upload_to('uploads'))
'''
