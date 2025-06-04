1. define ml objective
   retrieve images that are visually similar to input image 
2. choose ml category
   search system is a ranking problem
   representation learning: input -> model -> embeddings (vectors)
3. data
   images, users, user-image interactions
   preprocessing of images
4. model
   what model: NN
   training: contrastive training (input image + 1 similar + n different + label)
   dataset: human label / user interactions / self-supervision (data augmentation)
   loss function: computer similarity -> softmax -> cross-entropy
5. evaluation
   offline: MRR, Recall@k, Precision@k, mAP, nDCG
   online: click-through rate, average engagement time
6. serving
   1. prediction pipeline: 
      1. embedding generation service: input -> embedding
         1. preprocessor: raw data -> input
         2. trained ml model
      2. nearest neighbor service: embedding -> similar images
      3. re-ranking service
   2. indexing pipeline: stream of new images -> storage -> indexing service -> index table
   