ML system:
1. Data Prep
   1. Data Collection
      1. Raw data ingestion from logs, sensors, APIs, databases, etc.
   2. Data Verification
      1. Validate quality, completeness, consistency; catch anomalies early.
   3. Data Privacy & Security
      1. Ensure compliance (e.g., masking PII, consent management).
   4. Metadata Management
      1. Track datasets, versions, lineage for reproducibility.
2. Feature & Modeling Pipeline
   1. Feature Extraction / Feature Engineering
      1. Build, transform, and store features (offline/online parity).
   2. ML Algorithm
      1. Select model type, train, evaluate, tune.
   3. Configuration
      1. Track experiment settings: hyperparameters, model configs, data versions.
   4. Model Registry
      1. Save trained models with metadata, metrics, versions.
3. Evaluation
   1. Evaluation Pipeline
      1. Test performance offline; prepare for online validation.
   2. Analysis Tools
      1. Analyze metrics, compare experiments, debug behavior.
   3. Explainability & Fairness
      1. Audit for bias, generate model insights (SHAP, LIME).
4. Orchestration & Automation
   1. Process Management
      1. Use workflow engines (Airflow, Dagster) to manage data → model pipelines.
   2. CI/CD for ML (MLOps)
      1. Automate training, testing, and deployment steps via pipelines.
5. Deployment & Serving
   1. Service Infrastructure
      1. Host the model via API or batch, with scaling and monitoring.
   2. Machine Resource Management
      1. Allocate GPUs, autoscale, manage inference latency.
   3. Monitoring
      1. Track data drift, model degradation, infrastructure health.
6. Post-Deployment Loop
   1. Feedback Loop
      1. Capture predictions, user interactions, and re-label for future training.
   2. Disaster Recovery / Backup
      1. Ensure you can recover from failures or bad deployments.


ML interview:
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
         1. feature scaling: 
            1. normalization
            2. standardization
            3. log scaling
         2. discretization
         3. encode categorical features
            1. integer encoding
            2. one hot
            3. embedding learning: word2vec
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
   1. data distribution shift