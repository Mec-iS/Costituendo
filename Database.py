### Laws, sections and articles

TABLE laws:
    '''
        Table to host all laws of a specific country. In this table only the main data will appear
        
        1, 'Costituzione', 1948, 0
        2, 'Codice Civile', 19??, 0
        3, 'Codice Penale', 19??, 0
    '''
    id                  > INT # Autoincremental ID of the law
    name                > TEXT required=True # Name of the law
    creation            > DATE #Creation date
    repealed            > BOOL # Is the law still valid or has been repealed?
    repeal_date         > DATE # Date of repeal (if it has been repealed)

TABLE sections:
    '''
        Table to host all laws sections.

        1, 1, 0, 'Principi fondamentali'
        2, 1, 0, 'Parte prima'
        3, 1, 2, 'Titolo I'
        4, 1, 2, 'Titolo II'
    '''
    id                  > INT # Autoincremental ID of the section
    law_id              > FK(laws) # Foreign Key pointing to the law which the section is part of
    parent_id           > FK(sections) default=0 # Section that contain this section (if none, 0 will appear)
    name                > TEXT required=True # Name of the section

TABLE articles:
    id                  > INT
    number              > INT required=True
    text                > TEXT required=True
    law_id              > FK(laws)
    section_id          > FK(sections)

### Resources

TABLE resources:
    id                  > INT
    category_id         > FK(resource_categories)
    text                > TEXT required=True
    url                 > VARCHAR(255)
    author              > FK(authors)
    source              > FK(sources)
    
TABLE resource_categories:
    id                  > INT
    name                > VARCHAR(100) required=True    

TABLE resource_fields:
    id                  > INT
    resource_id         > FK(resources)
    key                 > VARCHAR(50)
    value               > TEXT

### Sources

TABLE sources:
    id                  > INT
    type_id             > FK(source_types)
    name                > VARCHAR(50)

TABLE source_type:
    id                  > INT
    name                > VARCHAR(50)
    
TABLE source_fields:
    id                  > INT
    source_id           > FK(sources)
    key                 > VARCHAR(50)
    value               > TEXT

### Authors

TABLE authors:
    id                  > INT
    title_id            > FK(titles)
    name                > VARCHAR(50)
    surname             > VARCHAR(50)
    
TABLE author_titles:
    id                  > INT
    name                > VARCHAR(50)

TABLE author_fields:
    id                  > INT
    author_id           > FK(authors)
    key                 > VARCHAR(50)
    value               > TEXT

### Topics

TABLE topics:
    id                   > INT
    name                 > VARCHAR(50)

TABLE topic_fields:
    id                  > INT
    topic_id            > FK(topics)
    key                 > VARCHAR(50)
    value               > TEXT

TABLE author_topic:
    author_id           > FK(authors)
    topic_id            > FK(topics)

TABLE resource_topic:
    resource_id         > FK(resources)
    topic_id            > FK(topics)

TABLE article_topic:
    article_id          > FK(articles)
    topic_id            > FK(topics)

TABLE law_topic:
    law_id              > FK(laws)
    topic_id            > FK(topics)
