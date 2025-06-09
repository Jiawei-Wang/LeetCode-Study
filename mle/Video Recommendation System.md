1. ml objective
   maximize the number of relevant videos
2. input and output
   input: user
   output: list of videos
3. ml category: sequential hybrid filtering (first collaborate filtering, then content based filtering)
   CBF: user watched video A -> video B is similar to A -> B is recommended to user (video features needed)
   CF: user B is similar to user A -> videos B watched are recommended to user A (purely using user profile)
4. data source and feature engineering: videos, users, user-video interactions
5. model
   1. Matrix factorization: fill out feedback matrix
      1. construct sparse feedback matrix (using explicit + implicit feedback)
      2. create user embedding matrix + video embedding matrix (initial values are random)
      3. training: dot product of embeddings -> compare to feedback matrix -> reduce error
      4. prediction: use model to fill out feedback matrix
   2. Two-tower NN: map users and videos into same embedding space
      1. construct dataset: user features + video features + label
      2. user features -> user encoder -> user embedding
         video features -> video encoder -> video embedding
      3. training: dot product of embeddings -> compare to label -> reduce error
      4. prediction: 
            all videos -> video encoder -> embeddings -> vector db
            new user -> user encoder -> embedding -> search for nearest neighbor
   compare:
      cost: matrix factorization is cheaper than two tower
      speed: matrix factorization is faster than two tower
      cold start: two tower is better than matrix factorization
      recommendation quality: two tower is better than matrix factorization
6. evaluation
   offline: Precision@k, mAP, diversity
   online: click-through rate, number of completed videos, watch time, user feedback
7. serving
   1. candidate generation: new user -> feature preprocess -> user encoder -> embedding -> two tower -> find candidate videos from pre-computed vector db
   2. scoring: candidate videos + user -> two tower -> rank videos based on video features -> smaller group of videos
   3. re-ranking: business related requirements
