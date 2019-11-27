# Exam Information

  * The exam will be **bring-your-own-device** and **without safe exam browser**.
  * Date: **04/12**

## Resources

You can use:
  * Calculator
  * All written (printed) and electronic material, including programs on your device
    - This includes, among others, spreadsheet programs and Python as well. Note that no external tools are necessarily; all exercises can be solved with a calculator.
    * The lecture slides are made available in PDF format for download [here](slides/)
  * **No online resources!**

### Grading

  * The exam contains N multiple choice questions, where there is -1 point for wrong answer (no answer is 0 points). These are explicitly indicated.
  * Total points: 100 + N
  * Grading
    - 0-39	F
    - 40-49	E
    - 50-59	D
    - 60-79	C
    - 80-89	B
    - 90+	A

## Topics

Motto: "everything from the lectures and practicums"
(except topics that are crossed out in the list below)

  * Text representation and preprocessing
    - Tokenization, stopword removal, stemming
    * Term vectors, TFIDF term weighting
    - Cosine similarity
  * Text classification
    - Model development and training strategies
    - Naive Bayes classifier
    - Multiclass classification
        * One-against-rest and one-against-one approaches
    - Evaluation
        * Confusion matrix
        * Type I and II Errors
        * Evaluation measures for binary evaluation (accuracy, precision, recall, F1, true/false positive/negative rate)
        * Evaluation Measures for multiclass evaluation (micro- and macro-averaging)
  * ~~Text clustering~~
  * Information retrieval
    - Search engine architecture
    - Indexing
        * Inverted index with term frequency or with position information
    - Query processing (term-at-a-time vs. document-at-a-time)
    - Retrieval models
        * Vector space model
        * BM25
        * Language models and different smoothing methods (Jelinek-Mercer, Dirichlet)
        * Sequential Dependence Model
    - Fielded retrieval models (BM25F, MLM, PRMS, FSDM)
    - Feedback
        * Rocchio feedback
        * Relevance models
    - Web search
        * Anchor text
        * PageRank
        * SEO
    - Learning-to-rank
        * Difference between pointwise, pairwise, listwise methods
        * Types of features (query, document, query-document)
    - Neural IR
        * Word embeddings, Word2Vec (CBOW, Skip-gram)
        * Neural IR models (DSSM, Duet, NRM-F)
    - Evaluation
        * Techniques for collecting relevance assessments (crowdsourcing, pooling)
        * Precision, recall, (mean) average precision, (mean) reciprocal rank, NDCG
        * Offline vs. online evaluation
  * Semantic search
    - Knowledge bases, RDF, DBpedia
    - Entity retrieval
        * Representing properties of entities
        * Ranking term-based entity representations
        * Entity linking incorporated retrieval (ELR) model
    - Entity linking
        * Mention detection (and sources of surface forms)
        * Candidate selection (commonness)
        * Disambiguation (features, individual vs. collective approaches, TAGME, AIDA)
        * Evaluation
    - ~~Table search, generation, and completion~~
