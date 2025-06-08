1. ml objective
   detect harmful posts
2. input and output
   post -> probability of it being harmful
3. feature fusion
   1. why: input is multi-modality (image, text, author, etc)
   2. strategies
      1. early fusion (input level): raw data -> separate encoding streams -> all extracted features -> fusion layer -> single, high-dimensional feature vector -> ml model
      2. late fusion (output level): raw data -> separate encoding streams -> each extracted feature -> each ml model per feature -> all predictions -> fusion -> combined prediction
      3. intermediate fusion: raw data -> separate encoding streams -> each extracted feature -> processed separately by initial layers of NN -> output being fused by Cross-Modal Attention Layer -> joint processed by subsequent layers of NN -> final prediction
4. ml category: multi-task learning (multi-task classifier) with early fusion
   post -> image + text + metadata -> fused features -> shared backbone layers -> transformed features -> task-specific layers (classification heads) -> prediction on each harmful class -> combined output
   Other considerations:
   1. single binary classifier: can't determine which class of harm
   2. one binary classifier per harmful class: expensive
   3. multi-label classifier: needs extra feature engineering
5. data source: users, posts, user-post interactions
6. model hyperparameter tuning: grid search, random search
7. training
   construct training dataset: batch offline -> feature input and label output
   loss function: standard binary classification loss like cross-entropy for each task 
   overfitting: gradient blending and focal loss
8. evaluation
   offline: PR-curve, ROC curve
   online: Prevalence, impressions, appeals, user reports, proactive rate
9. serving
   detection service: post -> feature preparation -> trained ml model -> output
   enforcement service
   
   