# Report on Assignment 2B

**Team ID:** *add*

**Student Name(s):** *add*


## Feature development (max. 500 words, excluding table and list)

  * Briefly list *all* the features implemented in your code, one feature per bullet point. If the implementation of a feature was not trivial, briefly (max. 50 words per item) describe the implementation. Use short, distinctive, and informative names for the additional features, e.g., not FeatureX but rather PageRank.
  * We distinguish between 3 feature groups:
      - [QD] Query-document features
      - [Q] Query features
      - [D] Document features
  
  * Features
      * Query-document features
	      * *TODO Add each of the 6 document-query features specified in Part 1 of the assignment that was also implemented in your code.*
	      * *For example:* BM25 on 'title' field
          * *TODO Add each additional feature implemented*: *TODO implementation details*
	  * Query features
	      * *TODO Add each additional feature implemented*: *TODO implementation details*
	  * Document features
	      * *TODO Add each additional feature implemented*: *TODO implementation details*

  * Describe your rationale behind your choice of additional features. Why would you expect these do be helpful in identifying the most relevant documents to a query?

### Learning algorithm
* Choose one learning-to-rank algorithm for the entire assignment, explain why this one was chosen, and state how the hyperparameters were set. 

### Results

* Complete the table below with learning-to-rank results on `data/queries.txt`.
  - These numbers should be obtained using 5-fold cross-validation on the provided queries and relevance judgments.
  - Report on four combinations of feature groups: QD, QD+Q, QD+D, QD+Q+D
  - Use the same training/test folds to make sure the numbers are comparable!

| **Features** | **Output file** | **NDCG@10** | **NDCG@20** |
| -- | -- | -- | -- |
| Only QD features | *TODO* | *TODO* | *TODO* |
| QD + Q features | *TODO* | *TODO* | *TODO* |
| QD + D features | *TODO* | *TODO* | *TODO* |
| ALL features (QD + Q + D) | *TODO* | *TODO* | *TODO* |


## Feature selection experiments (max. 400 words, excluding table)

* In part 3 of the assignment you have searched for and determined the 5 best for learning-to-rank. 
* List the five best features.
* Describe the process of finding the best performing subset of five features out of all the features you developed. Include your reasoning behind each of the different subsets tried.
* If you needed to update the hyperparameters during these steps, describe the changes and your reasoning behind each update.

### Results

* Complete the table below with learning-to-rank results on `data/queries2.txt`, filling in just the two rows: 
    * the full feature set and 
	* the selected feature set of the five best features.

| **Features** | **Output file** | **NDCG@10** | **NDCG@20** |
| -- | -- | -- | -- |
| ALL features (QD + Q + D) | *TODO* | *TODO* | *TODO* |
| Selected five best features | *TODO* | *TODO* | *TODO* |


## Kaggle submission (max. 300 words)

* Having made some submissions to Kaggle, list the feature set you used to get the best performance. 
* Describe the process of arriving at this feature set. 
* Include your reasoning behind each of the different steps or stages described. 
* If you needed to update the hyperparameters during these steps, describe the changes and your reasoning behind each update.


## References

  * If you used external resources (websites, books, articles, etc.) make sure you acknowledge them here.
