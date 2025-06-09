1. ml objective
   maximize number of event registrations
2. input and output
   input: user
   output: events ranked by relevance
3. ml category
   Learning to Rank: pointwise, pairwise, listwise
4. data source: user, event, user friendship, user event interaction
5. feature engineering: 
   difficulty: cold start problem
   location related features + time related features + social related features + event related features
6. model: binary classification  
   Neural Net
   others:
   1. Logistic Regression
   2. Decision Tree
      1. bagging: random forest
      2. boosting
   3. Gradient Boosted Decision Tree
7. construct dataset: user feature + event feature + label
   imbalance issue: focal loss / class-balanced loss / undersample majority class
8. loss function: binary cross-entropy
9. evaluation:
   offline: Recall@k, Precision@k, MRR, nDCG, mAP
   online: CTR, conversion rate, revenue
10. serving
    1. online learning pipeline: data source -> dataset -> training -> model repo -> evaluation -> deployment
    2. prediction pipeline: user -> (combine with event db) -> rule based event filter -> candidate events -> (combine with batch + streaming feature store) -> re-ranking NN -> top k events