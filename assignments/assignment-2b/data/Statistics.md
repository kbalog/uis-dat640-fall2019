# Pre-computed statistics

Statistics are available for all queries (in `queries.txt` and `queries.txt`) and all documents for the respective queries in the first_pass rankings for both query sets (`ranking_bm25.csv` and `ranking2_bm25.csv`) as well as in the qrels for the training query set (`qrels.csv`).

Note: there may be documents in `qrels.csv` which are not present in the index (and thus no statistics are available for them). You can safely ignore those.

## Available

  * Collection statistics (`stats_coll.tsv`)
    - `Field`: Name of the field
    - `Field_length`: The total term count in a given field
    - `Num_docs`: The number of documents where that field is not empty
  * Term statistics (`stats_terms.tsv`)
    - `Term`: Index term
    - `Field`: Name of the field
    - `SumTermFreq`: The total frequency of `Term` in `Field`
  * Document statistics (`stats_docs.tsv.zip`)
    - `DocumentId`: Document ID
    - `Field`: Name of the fields
    -	`Field_length`: The length of that field in the given document


## Coming soon

  * Document-term statistics
    - TF in each field
    - IDF in each field
