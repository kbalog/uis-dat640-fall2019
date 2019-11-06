# Assignment 3

Your task is to implement three entity retrieval models on top of Elasticsearch and evaluate them on a standard test collection.

## Models

You need to implement three models and report evaluation results on those. All models should be implemented as a re-ranking mechanism over top-100 (first-pass) retrieval results that you obtain using the default retrieval model (BM25) in Elasticsearch.

  1. **MLM**: The mixture of language models approach with two fields, title and content, with weights 0.2 and 0.8, respectively. Content should be the "catch-all" field. Use Dirichlet smoothing with the smoothing parameter set to 2000.
  1. **SDM+ELR**: Sequential dependence model with the ELR extension.
      - This is a single-field variant of SDM, so you need to use the "catch-all" field for term-based scoring.
      - Use standard weights, that is, 0.8 for unigram matches, 0.05 for ordered bigram matches, 0.05 for unordered bigram matches, and 0.1 for entity matches.
      - Use Dirichlet smoothing with the smoothing parameter set to 2000.
      - Note: you'll need to build a positional index.
      - The entity annotations for queries are provided as part of the input.
  1. **Your model**: This may be any known extension/variant of existing models or your own invention. You may use any technique or combination of techniques introduced in the lectures, e.g., multiple fields, query expansion, word embeddings, etc. A standard option is FSDM+ELR, which should give you 10% relative improvement over SDM+ELR.

## Deliverable

  * The code solutions must be submitted as edits in the Jupyter notebooks provided:
    - *1_Indexing*: Code used for building the index.
    - *2_Ranking_Model_1*: Implementation of the MLM model.
    - *2_Ranking_Model_2*: Implementation of the SDM+ELR model.
    - *2_Ranking_Model_3*: Implementation of Your model.
    - *3_Evaluation*: Evaluation code is provided.
  * The ranking output files corresponding to the three models.
  * You need to complete the [REPORT.md](REPORT.md) file in your private repository.
  * You must submit your best ranking file to the Kaggle competition, and your grade will take your performance results into account.

### Assignment scoring

The specific criteria for scoring the assignment is as follows:

  * Indexing (*TBD* points)
  * Implementation of MLM (*TBD* points)
  * Implementation of SDM+ELR (*TBD* points)
  * Implementation of Your model (*TBD* points)
  * Performance of Your model (5 points)
    - Points are based on the relative improvement made in percentage points (using rules of rounding) compared to the SDM+ELR model in terms of NDCG@10 score:

    | Improvement | Points |
    | -- | -- |
    | <2% | 0 |
    | >=2 and <4% | 1 |
    | >=4 and <6% | 2 |
    | >=6 and <8% | 3 |
    | >=8 and <10% | 4 |
    | >=10% | 5 |

  * Report (*TBD* points)
  * Code readability and hygiene (*TBD* points)


### Submission deadline

The **deadline** for submitting your code on GitHub as well as your final ranking on Kaggle is **27/11 17:00**.


## Data

### Knowledge base

The knowledge base we use as our dataset is DBpedia, specifically [version 2015-10](http://wiki.dbpedia.org/Downloads2015-10). You need to download and index this collection using Elasticsearch on your local machine.  Keep only entities that have both title and abstract (i.e., `rdfs:label` and `rdfs:comment` predicates).

DBpedia is distributed as a set of sub-collections. The following sub-collections are to be used:

| File name | Predicates | Reverse* |
| -- | -- | -- |
| core-i18n/en/article_categories_en.ttl.bz2 | `<dcterms:subject>` | |
| core-i18n/en/category_labels_en.ttl.bz2 | `<rdfs:label>` | |
| core-i18n/en/disambiguations_en.ttl.bz2 | `<dbo:wikiPageDisambiguates>` | Yes |
| core-i18n/en/infobox_properties_en.ttl.bz2 | Too many to list here | |
| *Table is to be populated* |||

  * "Reverse" means that in the subject-predicate-object triple the entity stands as object. Thus, it's the subject component of the triple that needs to be indexed (i.e., "reverse" the direction of the triple).


### Fields

The choice of fields and preprocessing applied is up to you. In previous work, the following fields have been used successfully:
  * Names (canonical name(s) of the entity)
  * Aliases (name variants)
  * Categories
  * Attributes
  * Related entity names


A couple of things to keep in mind:

  * You'll need a "catch-all" field.
  * For subject-predicate-object (SPO) triples where the object is an entity, you want to make it searchable both as text (by performing URI resolution, i.e., replacing the URI with the canonical name of the entity) and as an entity. That is, you'll need to have two different types of fields, text and entity, and SPO triples with entity objects contribute to both types of fields.
  * For the SDM+ELR model, you'll need a "catch-all entities" field as well.
  * Remember that indexing may take some time, so make sure you leave enough time for it.
  * Use a single shard to make sure you're getting the right term statistics.


### Queries

The [queries.txt](data/queries.txt) file contains 234 queries in total.  Each line starts with a queryID, followed by the query string (separated by a tab).  E.g.,

```
INEX_LD-2009022	Szechwan dish food cuisine
INEX_LD-2009053	finland car industry manufacturer saab sisu
INEX_LD-2009062	social network group selection
...
```

You are provided with the relevance judgments for these queries (see below).

The [queries2.txt](data/queries2.txt) file contains additional 233 queries. These are "unseen" queries, for which you'll have to generate entity rankings, but you don't get to see the corresponding relevance judgments.


### Query entity annotations

Entity annotations for the queries are provided in the *TO BE ADDED* file.


### Relevance judgments

The [qrels.csv](data/qrels.csv) file contains the relevance judgments for the queries in `data/queries.txt`. Each line contains the relevance label for a query-entity pair.  Relevance ranges from 0 to 2, where 0 is non-relevant, 1 is somewhat relevant, and 2 is highly relevant.

```
QueryId,EntityId,Relevance
INEX_LD-2009022,<dbpedia:Afghan_cuisine>,0
INEX_LD-2009022,<dbpedia:Akan_cuisine>,0
INEX_LD-2009022,<dbpedia:Ambuyat>,0
INEX_LD-2009022,<dbpedia:American_Chinese_cuisine>,1
...
```


### Output file format

The output file should contain two columns: QueryId and EntityId. For each query, up to 100 entities may be returned, in decreasing order of relevance (i.e., more relevant first).

The file should contain a header and have the following format:

```
QueryId,EntityId
INEX_LD-2009022,<dbpedia:American_Chinese_cuisine>
INEX_LD-2009022,<dbpedia:Chinese_cuisine>
INEX_LD-2009022,<dbpedia:Hot_and_sour_soup>
...
INEX_LD-2009053,<dbpedia:Sisu_A-45>
INEX_LD-2009053,<dbpedia:Sisu_A2045>
INEX_LD-2009053,<dbpedia:Sisu_Auto>
...
```
