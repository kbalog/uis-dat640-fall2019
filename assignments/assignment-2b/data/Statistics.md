# Pre-computed statistics

Statistics are available for all queries (in `queries.txt` and `queries.txt`) and all documents for the respective queries in the first_pass rankings for both query sets (`ranking_bm25.csv` and `ranking2_bm25.csv`) as well as in the qrels for the training query set (`qrels.csv`).

  * Collection statistics (`stat_coll.tsv`)
    - `Field`: Name of the field
    - `Field_length`: The total term count in a given field
    - `Num_docs`: The number of documents where that field is not empty
  * Document statistics ()
    - `field_length`: The sum of all term frequencies in a field in a document.
    - Note: Some doc_ids don't have some fields.
  * Calculating term statistics
    - `sum_tf`: For each term in the set of query terms, for each field, for every document with that field, add up the frequency of that term.
    - `document_freqs[term][field]`: Count of documents with term in the given field.
  * Calculating document-term statistics
    - `tf`:
    - `idf`: Size of collection plus one, divided by the frequency of the term in all documents with the given field.
