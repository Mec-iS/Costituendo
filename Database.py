### Laws, sections and articles

TABLE laws:
    id                  > INT
    name                > TEXT required=True

TABLE sections:
    id                  > INT
    law_id              > FK(laws)
    parent_id           > FK(sections) default=0
    name                > TEXT required=True

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
