1. ml objective: maximize both explicit and implicit reactions
2. input and output: user -> ranked list of unseen posts sorted by engagement score
3. ml category: Learning to Rank
   user + post -> different classifier for each reaction type -> prediction on each reaction type -> combine with weights -> final engagement score
4. data: user, post, user-post interaction, friendship, etc
5. feature engineering: user features, post features, user-author affinities, etc
6. model
   multi-task DNN: input features -> shared layers -> each classification head -> each probability output
7. training dataset: user features + post features + affinity features + label
8. loss function
   binary cross-entropy for binary classification
   regression loss for regression task
9. evaluation
   offline: ROC and ROC-AUC
   online: CTR, reaction rate, time spent, user feedback
10. serving
    1. data preparation pipeline: stream of new data and interactions -> data store -> batch + online feature computation -> feature store
    2. prediction pipeline: user -> retrieval service (for new posts) -> ranking service -> re-ranking service