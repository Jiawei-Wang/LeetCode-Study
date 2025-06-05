1. ml objective
   rank videos based on relevance to text query
2. input and output
   text query -> ranked list of videos 
3. ml category: representation learning
      text encoder: text -> text embedding
      video encoder: video -> video embedding
4. data: already annotated dataset (video + content text)
5. feature engineering
      text data: normalization -> tokenization -> token to id
      video data: decode frames, resizing, scaling, color correcting, etc
6. model
      text encoder: input text -> vector (word2vec or transformer)
      video encoder: input video -> vector (convolution or transformer)
7. training: contrastive
   loss calculation: compute similarities -> softmax -> cross-entropy with ground truth
8. evaluation
   offline: Precision@k, Recall@k, Mean Reciprocal Rank
   online: CTR, video completion rate, watch time
9. system
   1.  video indexing pipeline: new video -> storage -> preprocess + encoding + indexing -> embedding index table
   2.  text indexing pipeline: new video -> title and content text -> encoding + indexing -> embedding index table
   3.  prediction pipeline:
      1. input text query goes into visual search and text search (inverted index + Elasticsearch, not ml)
      2. visual search: input text -> embedding -> Nearest Neighbor on embedding index table
   4. search result: combine two search results together -> re-rank, filter, etc
   
