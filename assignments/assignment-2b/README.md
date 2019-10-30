# Assignment 2B

**IMPORTANT** *This assignment description will be updated over the course of the coming days. Make sure to always look at the most recent version of the respective parts.*

**UPDATES (30/10 12:00)**
  *  The first-pass ranking data files (`data/ranking_bm25.csv` and `data/ranking2_bm25.csv`) have been pushed out to the private repositories. These are the documents you need to re-rank for each query set.
  * The Kaggle competition has been set up ([here](https://www.kaggle.com/c/uis-dat6402019-2b)). You're allowed 3 submissions per day until the deadline.
  * The API is currently unavailable (due to an ongoing index update).
  * The deadline has been extended by 48 hours to **06/11 17:00**.
  * The pre-precomputed statistics (discussed on Monday) are being computed and will be made available soon.

----

The task is to implement a learning-to-rank approach for web search and evaluate it using a standard test collection.

You are provided with a set of queries and with an initial ranking of top-100 results for each query (based on BM25). Your task is to re-rank these documents using a learning-to-rank approach. Specifically, you need to use a pointwise learning-to-rank approach, i.e., any standard regression algorithm that is available in scikit-learn.

An Elasticsearch index is already created (that is, we already indexed the document collection for you) and can be accessed via an API; see [below](#search-api).

The following Jupyter notebooks are provided for your convenience. You don't need to use these, you can follow any structure you like as long as your solution is submitted as Jupyter notebooks.
  * *1_Feature_computation*
  * *2_Ranking*
  * *3_Evaluation*


## Part 1 (week 42)

  * Implement a learning-to-rank method with the following minimum requirements:
    - Consider document-query matching in minimum 3 fields (title, content and anchors) and at least two different retrieval models (e.g., BM25 and LM). That is, 6 document-query features minimum.
    - Note that the anchor text index covers the entire ClueWeb collection, not just the Category B subset. I.e., you need to ignore documents that are not present in the regular index.
  * Select one learning-to-rank algorithm to use throughout the assignment.
  * Test your model using 5-fold cross-validation on the given training data (queries and relevance judgments, i.e., `data/queries.txt` and `data/qrels.csv`).

## Part 2 (week 43)

  * Design and implement additional features to maximize retrieval performance.
    - Add minimum 2 query features and minimum 2 document features.
    - PageRank scores for the ClueWeb collection are [available here](http://www.lemurproject.org/clueweb12/PageRank.php). Specifically, since you are working with the "Category B" subset, the files under the "ClueWeb12-B13 PageRank" heading are to be used.
    - Note: you *don't have to* use PageRank as a feature. If you want, you can take PageRank scores from one of these files (and you need to figure out the file format yourself; but really, it is not that complicated).
  * For inspiration on additional features, you can check the lecture slides or these papers:
    - [LETOR: Learning to Rank for Information Retrieval](https://www.microsoft.com/en-us/research/project/letor-learning-rank-information-retrieval/). Specifically, check the feature list [in this paper](https://arxiv.org/ftp/arxiv/papers/1306/1306.2597.pdf)
    - [Macdonald et al. 2012. On the Usefulness of Query Features for Learning to Rank](https://pdfs.semanticscholar.org/dbb5/a414a1168fe2142d9bea2ed561a4a43610bf.pdf)
  * Generate rankings for the "unseen" test queries (`data/queries2.txt`) and submit them on Kaggle: [link](https://www.kaggle.com/c/uis-dat6402019-2b).
    - Mind that you can use the entire training set for learning the model when generating rankings for the test queries.


## Part 3 (week 44)

  * Select a subset consisting of the five features, from the complete feature set, that give you the best overall performance.
    - You will need to describe in your report how you decided on these particular features.
  * If you think you found a better subset of features than you tried before, you may make a new Kaggle submission.
  * You may do this repeatedly as part of your search for the best five features.


## Deliverable

  - You need to complete the [REPORT.md](REPORT.md) file in your private repository.
  - All code files that were used to produce the report must be included in the GitHub repository. Do not store large data files on GitHub!


### Assignment scoring

The specific criteria for scoring the assignment is as follows:

  *  *To be added*


### Submission deadline

The deadline for submitting the report and code on GitHub is **06/11 17:00**.


## Data

### Document collection

The document collection is the [ClueWeb12](http://lemurproject.org/clueweb12/) dataset, specifically the "Category B" subset of it.  It consists of around 50 million pages.  

  * An Elasticsearch index of the documents (web pages) `clueweb12b` is provided with `title`, `url`, and `content` fields.  Content comprises only the visible text from the HTML source.
  * The anchor texts are stored in a separate index called `clueweb12b_anchors`.  Mind that this index contains the anchor texts for all ClueWeb documents, not only documents from the Category B subset. It means that documents that are present in this index, but not in the `clueweb12b` index, should be ignored.


### Queries

The [queries.txt](data/queries.txt) file contains 50 queries in total.  Each line starts with a 3-digit queryID, followed by the query string.  E.g.,

```
151 403b
152 angular cheilitis
...
```

You are provided with the relevance judgments for these queries (see below).

The [queries2.txt](data/queries2.txt) file contains additional 50 queries. These are "unseen" queries, for which you'll have to generate document rankings, but you don't get to see the corresponding relevance judgments.


### Relevance judgments

The [qrels.csv](data/qrels.csv) file contains the relevance judgments for the queries in `data/queries.txt`. Each line contains the relevance label for a query-document pair.  Relevance ranges from -2 to 4, where -2 is used for junk/spam pages and 0..4 is used to indicate the degree of relevance from non-relevant to highly relevant.

Note that this file may contain document IDs that are not present in the index. Just ignore those.

```
QueryId,DocumentId,Relevance
201,clueweb12-0000tw-05-12114,1
201,clueweb12-0000wb-30-01951,0
201,clueweb12-0000wb-60-01497,1
...
```


### Output file format

The output file should contain two columns: QueryId and DocumentId. For each query, up to 100 documents may be returned, in decreasing order of relevance (i.e., more relevant first).

The file should contain a header and have the following format:

```
QueryId,DocumentId
201,clueweb12-0108wb-86-18203
201,clueweb12-0209wb-62-29857
201,clueweb12-0300tw-49-08295
...
202,clueweb12-0001wb-80-19541
202,clueweb12-0001wb-85-15380
202,clueweb12-0001wb-99-29092
...
```


## Search API

A distributed index of the ClueWeb12B collection is built using Elasticsearch and is hosted on the cloud (specifically, the Amazon Elasticsearch Service, using Elasticsearch version 7.1).

There is a simple Search API that is made for requesting data from this index (this is essentially to make the index *read-only*, preventing anyone to accidentally make any unwanted modifications).

![Search API](search_api.png)

The API is available at `http://gustav1.ux.uis.no:5002`. Note that it is only available within UiS premises.

  * The main index is called `clueweb12b`, with fields `url`, `title`, and `content`.
  * *The anchors index is currently being built.*

The API source code is [available here](api.py). Note that you don't need to run it, this is only provided for transparency (so that you can see what exactly is happening in there).

See the [API usage](API_usage.ipynb) notebook for example usage.

Currently, the following functionality is supported.

  * **Search**: `/<indexname>/_search`
    - Execute a search query using [es.search()](https://elasticsearch-py.readthedocs.io/en/master/api.html#elasticsearch.Elasticsearch.search) and returns the search hits
    - Parameters:
        - `q` (mandatory): query
        - `df` (mandatory): field to search in
        - `size` (optional): number of hits to return (default: 10)
    - Examples:
        - searching in the title field of the document index `http://gustav1.ux.uis.no:5002/clueweb12b/_search?q=united+states&df=title&size=20`
        - searching in the anchor text index: `http://gustav1.ux.uis.no:5002/clueweb12b_anchors/_search?q=united+states&df=anchors&size=20`
  * **Termvectors**: `/<indexname>/<docid>/_termvectors`
    - Returns information and statistics on terms in the fields of a particular document using [es.termvectors()](https://elasticsearch-py.readthedocs.io/en/master/api.html#elasticsearch.Elasticsearch.termvectors)
    - Parameters:
        - `term_statistics` (optional): set true to return term statistics (default is false)
    - E.g. `http://gustav1.ux.uis.no:5002/clueweb12b/clueweb12-0209wb-65-17913/_termvectors?term_statistics=true`
    - NOTE: do not use the termvectors request to check if a document exists in the index. Use the exists endpoint instead (see next).
  * **Exists**: `/<indexname>/<docid>/_exists`
    - Returns whether the given document ID exists in that index using [es.exists()](https://elasticsearch-py.readthedocs.io/en/master/api.html#elasticsearch.Elasticsearch.exists)
    - E.g. `http://gustav1.ux.uis.no:5002/clueweb12b/clueweb12-1700tw-22-12689/_exists`
  * **Analyze**: `/<indexname>/_analyze`
    - Returns the analyzed version of the input text using [es.indices.analyze()](https://elasticsearch-py.readthedocs.io/en/master/api.html#elasticsearch.client.IndicesClient.analyze)
    - This endpoint is needed when using another retrieval method for scoring the query (e.g., LM). Instead of just splitting on spaces, use this request for tokenizing the query text.
    - Parameters:
        - `text` (mandatory): text to be analyzed
    - E.g. `http://gustav1.ux.uis.no:5002/clueweb12b/_analyze?text=World%27s+biggest+dog`

The API may be extended over time with additional functionality, should the need arise.  If you have specific requests, do let us know.

## FAQ

  * **How to deal with junk documents with relevance=-2?** When computing NDCG, use gain 0 for those results.  On the other hand, when training the model, use -2 as the target value (so that your model can learn to rank those results real low).
  * **Should we use binary target labels (i.e., target=1 if rel>0 and target=0 if rel<=0)?** No. Use the relevance labels directly as target values. We are treating it as a regression problem, not as a binary classification task.
  * **Do we need to use the PageRank scores from that link?** No. It's up to you. If you want, you can use them. What matters is that you implement at least 2 document features.
  * **How to check if a given document that we retrieve from the anchors text index exists in ClueWeb Category B?** A separate `exists` request has been introduced for that. Do not use `termvectors`, as that is too slow. Only use `termvectors` when computing the retrieval scores for a given document.
  * **Running the experiments takes a lot of time.** If you request all the data from the API each time you make a change or try to add a new feature, then yes, it'll take a very long time. You should compute individual features only once and store these somewhere (e.g., text or json files).
  * **Few document IDs retrieved from the API match those in the `qrels.txt` and/or `pagerank.docNameOrder.bz2`. Is this an error?** Yes, it’s an (indexing) error. It’s being fixed right now.
  * **The API is unavailable/not responding.** We’ll try to make sure it’s available. Mail to dat640help@gmail.com if it’s unavailable and we’ll try to bring it back ASAP.
  * **How should we calculate the BM25 scores?** If you want to use it as a feature, then calculate it yourself. Note that the BM25 first-pass ranking is given (without scores), and it’s not required to report on BM25.
