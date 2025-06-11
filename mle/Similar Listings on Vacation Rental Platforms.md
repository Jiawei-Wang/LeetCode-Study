1. ml object and input/output:
   a listing the user is viewing -> similar listing system -> ranked list of similar listings
2. ml category
   session-based recommendation system: two listings co-occur in user's browsing history will have embeddings mapped to close embedding space
3. data and feature engineering: user, listing, user-listing interaction
4. model: NN
5. training: sliding window with negative sampling
6. improvement: add central listing + booked listing pair as positive
7. loss function: dot product between two embeddings -> sigmoid -> cross-entropy against ground truth
8. evaluation
   offline: average rank of the booked listing
   online: CTR, session book rate
9. serving
   1. training pipeline: new listings -> model fine-tuning
   2. indexing pipeline: listings -> embeddings -> index table
   3. prediction pipeline: currently-viewed listing -> embedding -> nearest neighbor -> list of candidates -> re-ranking service 