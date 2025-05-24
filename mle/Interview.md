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
2. framing the problem as ml task
3. data preparation
4. model development
5. evaluation
6. development and serving
7. monitoring and infra