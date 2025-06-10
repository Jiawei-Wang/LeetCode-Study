1. ml objective: predict if an ad will be clicked
2. input: user
   output: ranked list of ads based on click probabilities
3. ml category: Learning to Rank
4. data and feature: ads, users, user-ad interactions
5. model
   1. Logistic Regression: can't deal with non-linear data, can't capture feature interactions
   2. LR + feature crossing: need domain knowledge, can be sparse
   3. GBDT: can't train on new data, can't take advantage of embeddings
   4. NN: sparsity means difficult training, can't capture all pairwise feature interactions (simply too many)
   5. Deep & Cross Network
   6. Factorization Machines
6. dataset: user features + ad features + interaction features + label
7. loss function: cross entropy
8. evaluation
   offline: cross entropy and normalized cross entropy
   online: CTR, conversion rate, revenue, user feedback
9. serving
   1. data preparation pipeline: new data + existing data source -> preprocessing -> batch feature processing (for static features) + online feature processing (for dynamic features) -> feature store -> training dataset 
   2. continual learning pipeline: training dataset -> model training -> validation -> deployment -> model registry
   3. prediction pipeline: user -> candidate generation service (rule based) -> a small group of ads -> fetch ads features from feature store -> ranking model -> re-ranking service (rule based) -> ranked ads