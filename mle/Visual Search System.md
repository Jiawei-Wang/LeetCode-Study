1. clarifying requirements
   1. what is business objective
   2. features the system needs to support
   3. all data related questions
   4. constraints of the system
   5. scale of the system
   6. performance
2. framing the problem as ml task
   1. define ml objective
   2. specify system input and out
   3. choose ml category
3. data preparation
   1. data engineering
      1. data source
      2. data type
         1. structured: numerical, categorical
         2. unstructured: audio, video, image, text
      3. ETL
      4. data storage
   2. feature engineering
      1. feature selection/extraction: select and extract predictive features from raw data
      2. handling all kinds of data issues
      3. feature transformation: transform predictive features into model usable format
         1. feature scaling
         2. discretization
         3. encode categorical features
            1. one hot
            2. embedding learning: word2vec
4. model development
   1. model selection
      1. pick simple ones first
      2. switch to more complex models
   2. model training
      1. construct dataset
         1. collect raw data
         2. identify features and labels
         3. select sampling strategy
         4. split data
         5. address class imbalance
      2. choose loss function
      3. train from scratch or fine-tune
         1. distributed training
5. evaluation
   1. offline evaluation
   2. online evaluation
6. development and serving
   1. cloud vs on-device
   2. model compression
      1. knowledge distillation
      2. pruning
      3. quantization
   3. testing in production
      1. shadow deployment
      2. a/b testing
   4. prediction pipeline
      1. batch prediction
      2. online prediction
7. monitoring and infra