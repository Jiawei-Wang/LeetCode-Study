1. ml objective
   detect objects in images
2. input and output
   image -> objects and their locations
3. ml category
   regression for location
   classification for object
   two-stage networks: R-CNN (RPN + classifier)
4. data: 
   street view images + annotated metadata dataset
   image preprocess -> data augmentation -> dataset
5. model
   input -> convolutional layer -> feature map -> RPN -> candidate regions -> classifier -> object
6. training: forward propagation + loss calculation + backward propagation
   regression loss: Mean Squared Error
   classification loss: cross-entropy
7. evaluation
   offline: Precision, Average Precision, Mean Average Precision
   online: user reports
8. additional algorithm:
   Non-maximum suppression to remove overlapping boxes
9. ml system:
   1.  batch prediction pipeline:
       1.  preprocessing: data source -> raw images -> data
       2.  object detector: R-CNN (CNN + RPN + classifier + Non-maximum suppression) for feature + region + classification
       3.  blurring service: blurred images -> db
   2.  data pipeline: user report -> hard negative mining -> new data point -> preprocess + augmentation -> new dataset -> model retraining
