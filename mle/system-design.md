All points listed are just examples


Interview
1. write a ml algorithm from scratch
   1. write k means clustering or k nearest neighbors
   2. write linear or logistic regression
   3. use numpy, pandas, sci kit learn
2. provide end-to-end solution given some data
   1. transform data
   2. choose models and metrics
      1. precision, recall, F1 for classification models
   3. show hyperparameter tuning
   4. explain how to search the hyperparameter space
      1. random search, quick search, grid search, etc
3. perform a common ML operation
   1. 2d convolution
   2. self attention
   3. batch normalization
4. coding example:
   1. one
      1. input: table of data with features like user time on app, number of interactions
      2. task: create a ml solution
      3. output: predict the likelihood of app deletion
   2. two:
      1. input: labels on whether content is harmful
      2. output: predict if a new content is harmful
5. interview core:
   1. understand the given problem
   2. understand the chosen ml framework
   3. implement organized and accurate code
   4. communicate your logic
6. judgement
   1. understanding ml fundamentals
   2. working with relevant datasets
   3. communication


Questions
1. data handling: turn raw data into valuable signals
   1. what are common transformations for categorical data
   2. we have 10,000 features, how to reduce input 
2. model selection and optimization: also include loss functions, hyperparameters, optimizers
   1. describe how splits in a decision tree occur
   2. how to construct a loss function if our priority is to reduce complexity of the model
3. evaluation methods and metrics: how to interpret and calculate
   1. pros and cons to use accuracy when measuring model performance
   2. what metrics to use to know recommendation system performance
4. development and deployment: 
   1. deploying:
      1. when to refresh or replace a model in production
      2. A/B testing, canary testing, feature flags, shadow deployment
   2. serving
      1. on device vs cloud
      2. modern model compression, knowledge distillation
   3. optimize and compile
      1. compilers for common ml frameworks and hardware combinations
      2. vectorization of iterative calculations, batching operations
   4. monitoring
      1. telemetry, health, performance
      2. user traffic handling: batch vs real time 
      3. benchmark with ground truth data
   

ML coding:
1. implement attention mechanism
2. implement convolutional filter
3. implement k means clustering
4. identity common ancestors in a tree


ML concept:
1. bias-variance trade off
2. training data vs testing data
3. stochastic gradient descent, mini-batch, gradient descent
4. feature scaling and normalization


