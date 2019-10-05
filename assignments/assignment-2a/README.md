# Assignment 2A

The task is to implement document retrieval methods and evaluate them using a standard test collection.

The assignment consists of three main parts.

For each part a skeleton of the code are provided as Jupyter notebooks in your team's own repository.

For this assignment, the only acceptable solutions are modifications of these notebooks. Only edit the designated parts of the skeleton code provided. The submissions that will be graded are those that are pushed to the individual team's repository at the deadline.

The notebooks also contain designated markdown cells where you should write your mini-report for each part. There is no separate report file to submit for this assignment.

Do your best to follow the schedule as indicated by week number, since the assignment consists of several parts that each require time and effort, and also depend on your solutions to previous parts. However, only the final submission will be graded, so there is some flexibility. Take advantage of this to efficiently solve each part and then go back to iterate on each part, rather than getting stuck in the early stages.

*This assignment description will be updated over the course of the coming weeks. Make sure to always look at the most recent version of the respective parts.*

## Part 1 (weeks 38-39)

  - Download the document collection and index it by completing the missing parts of the provided code skeleton.
    * Use two fields, title and content.
    * See [below](#document-collection) for details about the document collection.
    * The `1_Indexer.ipynb` notebook contains the code skeleton that you need to complete.
  - Complete the `1_Evaluation.ipynb` notebook, which should be able to take a ranking file and ground truth file as input and output.
      - A sample ranking file and ground truth file with dummy data is made available for testing purposes.
      - The evaluation capability will be used to evaluate rankings produced by the retrieval models that you implement in Parts 2 and 3.

## Part 2 (weeks 39-40)

  - Implement two (single-field) retrieval models (LM and BM25) and evaluate them using your evaluation solution from Part 1.
    * Search only in the `content` field.
    * Return the top 100 documents for each query in `data/queries.txt` and write the results to a `data/baseline.txt` file (see [below](#output-file-format) for the output file format).
    * The `2_Retrieval.ipynb` notebook contains the code skeleton that you need to complete.

## Part 3 (weeks 40-41)

  - Implement multi-field versions of BM25 and LM retrieval models, i.e., BM25F and MLM.
  - Tune the parameters
    * For BM25F, tune the field weights, k1, and b parameters.
    * For MLM, tune the field weights, smoothing method, and smoothing parameter.
    * The `3_Multifield_retrieval.ipynb` notebook contains the code skeleton that you need to complete.
  - You may compete with a single ranking against other teams.
    * The competition is hosted on [Kaggle](https://www.kaggle.com/t/4dd79e8ac78c4dc3bac2c5525e08f2d3).
    * The competition uses graded relevance judgments and NDCG@100 as the evaluation metric. (Documents with the highest relevance level have been shared with you in `data/qrels2.csv`; the rest of the data is withheld.)
    * You may submit a 2 entries to Kaggle per day (starting on 02/10).
    * Your performance will be based on the last submission to the Kaggle competition.


## Deliverable

  - The code solutions must be submitted as edits in the Jupyter notebooks provided with skeleton code.
  - The mini-report sections must be filled out in the notebooks. No separate report needs to be submitted.
  - You must submit your best ranking file to the Kaggle competition, and your grade will take your performance results into account.

### Assignment scoring

The specific criteria for scoring the assignment is as follows:

* Indexer (5 points)
* Evaluation (2 points)
* Retrieval (6 points)
* Multifield retrieval (7 points)

### Submission deadline

The deadline for submitting your code on GitHub as well as your final ranking on Kaggle is 09/10 17:00.


## Data

### Document collection

The AQUAINT document collection consists of newswire text data in English, drawn from three sources: the Xinhua News Service (`xie`), the New York Times News Service (`nyt`), and the Associated Press Worldstream News Service (`apw`). It has been used in official benchmark evaluations conducted by National Institute of Standards and Technology (NIST).

The text data are separated into directories by source (`apw`, `nyt`, `xie`); within each source, data files are subdivided by year, and within each year, there is one file per date of collection. Each file contains a stream of SGML-tagged text, i.e., blocks of text bounded by `<DOC>` and `</DOC>` tags.  Create an index with *title* (inside `<HEADING>`) and *content* fields (inside `<TEXT>`) and use `<DOCNO>` as the document identifier (docID).

The collection is 1.1GB compressed and can be dowloaded from the URL provided on [Canvas](https://stavanger.instructure.com/courses/4586/discussion_topics/44794).

Upon successful indexing, the index should contain 1,033,461 documents.

You are requested to delete the collection after this assignment.


### Queries

The [queries.txt](data/queries.txt) file contains 50 queries in total.  Each line starts with a 3-digit queryID, followed by the query string.  E.g.,

```
336 Black Bear Attacks
341 Airport Security
...
```


### Relevance judgments

The [qrels2.csv](data/qrels2.csv) file contains the relevance judgments for all queries. Each line contains a queryID and the set of docIDs. The queryID and docIDs are separated by a comma, the docIDs are separated by spaces. (Note that relevance is binary, so the order in which these documents are listed does not matter.)

The qrels file (qrels2.csv) contains only 45 queries, i.e., for 5 queries there are no relevance assessments. Just ignore those queries that are not in qrels2.csv when computing the MAP scores.

```
queryID,docIDs
303,APW19980610.1778 APW19990525.0223 APW19990602.0039  ...
307,APW19980602.0026 APW19980603.0021 APW19980810.1038 ...
...
```


### Output file format

The output file should contain two columns: QueryId and DocumentId. For each query in `queries.txt`, up to 100 documents may be returned, in decreasing order of relevance (i.e., more relevant first).

The file should contain a header and have the following format:

```
QueryId,DocumentId
303,APW19980715.1061
303,APW19990108.0103
303,APW19990108.0283
303,XIE19970211.0115
303,XIE19980610.0069
303,XIE19991228.0201
...
307,APW19980915.0811
307,XIE19990501.0067
307,XIE19970120.0005
307,XIE19961203.0196
307,XIE19981121.0137
...
```
