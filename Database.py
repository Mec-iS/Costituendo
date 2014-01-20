from django.db import models

# !!! DEFAULT IS NULL=FALSE !!! 
class Law(models.Model):
    class Meta:
        verbose_name = 'Codice'
        verbose_name_plural = 'Codici'
        
    name                 = models.CharField(max_length=50)
    became               = models.DateField()
    
    def __unicode__(self):
        return self.name

class Section(models.Model):
    class Meta:
        verbose_name = 'Sezione'
        verbose_name_plural = 'Sezioni'
    
    id                   = models.AutoField(primary_key=True)
    law                  = models.ForeignKey(Law)
    parent               = models.ForeignKey('self', default=None, null=True, blank=True)
    name                 = models.CharField(max_length=140)
    description          = models.CharField(max_length=140, blank=True, default='')
    order                = models.IntegerField()
    added                = models.DateField(auto_now_add=True)
    modified             = models.DateField(auto_now=True)
    who                  = models.CharField(max_length=100, editable=False)
    
    def __unicode__(self):
        return self.name
    
class Article(models.Model):
    class Meta:
        ordering = ['number']
        verbose_name = 'Articolo'
        verbose_name_plural = 'Articoli'
        unique_together = ('number', 'law')

    id                   = models.AutoField(primary_key=True)
    number               = models.IntegerField()
    text                 = models.TextField()
    law                  = models.ForeignKey(Law)
    section              = models.ForeignKey(Section)
    added                = models.DateField(auto_now_add=True)
    modified             = models.DateField(auto_now=True)
    who                  = models.CharField(max_length=100, editable=False)
    
    def __unicode__(self):
        number = str(self.number)
        law = self.law.name
        return law+' n.'+number

class Source(models.Model):
    class Meta:
        verbose_name = 'Fonte'
        verbose_name_plural = 'Fonti'

    TYPES = (
        (u'legge',       u'Legge dello Stato'),
        (u'opinione',    u'Opinione'),
        (u'ufficiale',   u'Dichiarazione'),
        (u'sentenza',    u'Sentenza'),
        (u'regolamento', u'Regolamento'),
        (u'libro',       u'Pubblicazione giuridica'),
        (u'stampa',      u'Stampa/Blog'),
        (u'redazione',      u'Redazione OpenIUS'),
    )
    id                   = models.AutoField(primary_key=True)
    type                 = models.CharField(max_length=50, choices=TYPES)
    editor               = models.CharField(max_length=140)
    name                 = models.CharField(max_length=140)
    details              = models.TextField(blank=True, default='')
    added                = models.DateField(auto_now_add=True)
    modified             = models.DateField(auto_now=True)
    who                  = models.CharField(max_length=100, editable=False)
    
    def __unicode__(self):
        return self.name

class Author(models.Model):
    class Meta:
        verbose_name = 'Autore'
        verbose_name_plural = 'Autori'

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
    id                   = models.AutoField(primary_key=True)
    title                = models.CharField(max_length=50, choices=TITLES)
    name                 = models.CharField(max_length=140)
    surname              = models.CharField(max_length=140)
    function             = models.CharField(max_length=140, choices=FUNCTIONS)
    details              = models.TextField(blank=True, default='')
    added                = models.DateField(auto_now_add=True)
    modified             = models.DateField(auto_now=True)
    who                  = models.CharField(max_length=100, editable=False)
    source               = models.ForeignKey(Source)
    
    def __unicode__(self):
        return self.name+'_'+self.surname+'@'+self.source.editor

class Topic(models.Model):
    class Meta:
        verbose_name = 'Argomento'
        verbose_name_plural = 'Argomenti'

    id                   = models.AutoField(primary_key=True)
    key                  = models.CharField(max_length=50, unique=True)
    text                 = models.TextField(blank=True, default='')
    added                = models.DateField(auto_now_add=True)
    modified             = models.DateField(auto_now=True)
    who                  = models.CharField(max_length=100, editable=False)
    
    def __unicode__(self):
        return self.key
        
class Resource(models.Model):
    class Meta:
        verbose_name = 'Risorsa'
        verbose_name_plural = 'Risorse'

    id                   = models.AutoField(primary_key=True)
    article              = models.ForeignKey(Article)
    added                = models.DateField(auto_now_add=True)
    modified             = models.DateField(auto_now=True)
    who                  = models.CharField(max_length=100, editable=False)
    source               = models.OneToOneField(Source)
    author               = models.ManyToManyField(Author)
    topics               = models.ManyToManyField(Topic, default=None, null=True, blank=True)
    

class TextResource(Resource):
    class Meta:
        verbose_name = 'Risorsa: testo'
        verbose_name_plural = 'Risorsa: testo'
        
    CATEGORY = (
        (u'esegesi',        u'Esegesi'),
        (u'storia',         u'Storia'),
        (u'dottrina',       u'Dottrina'),
        (u'giurisprudenza', u'Giurisprudenza'),
        (u'normativa',      u'Normativa'),
        (u'attualita',      u"Attualita'"),
        (u'citazione',      u'Citazione'),
    )
    text                 = models.TextField()
    category             = models.CharField(max_length=50, choices=CATEGORY)
    
    def __unicode__(self):
        returning = self.text[0:35]+'...'+'/'+self.category
        return returning
    
    def __str__(self):
        returning = self.text[0:35]+'...'+'/'+self.category
        return returning

class UrlResource(Resource):
    class Meta:
        verbose_name = 'Risorsa: link'
        verbose_name_plural = 'Risorsa: link'
    CATEGORY = (
       (u'link', u'articolo'),
       (u'video', u'video'),
       (u'audio', u'audio'),
    )
    description          = models.CharField(max_length=255)
    url                  = models.CharField(max_length=255)
    category             = models.CharField(max_length=80, choices=CATEGORY)
        
    def __unicode__(self):
        description = self.description
        description = description.split()
        returning = '-'.join(description[0:5])
        returning = returning+'...'+'@'+self.url[0:20]+'...'
        return returning
    
    def __str__(self):
        description = self.description
        description = description.split()
        returning = '-'.join(description[0:5])
        returning = returning+'...'+'@'+self.url[0:20]+'...'
        return returning

class Page(models.Model):
    id                   = models.AutoField(primary_key=True)
    slug                 = models.SlugField(unique=True)
    title                = models.CharField(max_length=140)
    version              = models.IntegerField(default=0)
    html                 = models.TextField()
    added                = models.DateField(auto_now_add=True)
    modified             = models.DateField(auto_now=True)
    
'''
class DataResource(Resource):
    CATEGORY = (
       (u'pdf', u'pdf'),
       (u'csv', u'csv'),
       (u'json', u'json'),
    )
    file                = models.FileField(upload_to('uploads'))
'''