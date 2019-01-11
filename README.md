# Gait-Recognition
It is the project of gait recognition
Human recognition methods , such as fingerprints,face,or iris biometric
modalities,generally reguire a cooperative subject, views from certain aspects,and physical contact or close proximity
These methods cannot rliably recognize noncooperating individuals at a distance in real world under changing environmental
conditions.Gait,which concerns recognizing individuals by the way they walk.
>>Gait Energy Image (GEI), to characterize human walking properties for individual recognition by gait.  Real templates are computed from training silhouette sequences, while  generate the synthetic templates from training sequences by simulating silhouette distortion.
>>following link give proper description
 1-https://ieeexplore.ieee.org/document/1561189/
 2-https://www.sciencedirect.com/science/article/pii/S0165168410000411
 3-https://www.sciencedirect.com/science/article/pii/S0167865509000920

# Data Preprocessing
We work on the normal images of person silhouettes .From the data, we extract
normal images of corresponding sets of images and make Gait Energy Image (GEI),
to characterize human walking properties for individual recognition by gait. Real
templates are computed from training silhouette sequences, while generate the
synthetic templates from training sequences by simulating silhouette distortion
We Prepare GEI by summation of all the images of corresponding normal image and
divided by the number of images containing by that particular normal image.Now we
have GEI images .Flip the images left right so all are in same orientation.Store the GEI
images in a new folder from where we extract .

# Calculating Accuracy
We split the data into train and test in 3:1 ratio.And then shuffle the train and test test
set, before training the data to get parameters.Dimension reduction PCA is applied to
reduce the dimension and getting more accuracy
Different Classifier are used to get the better accuracy with tuning the parameters ,
Decision Tree classifier,Linear SVC ,Logistic Regression and few more..And finally we
got 95% test accuracy and 100% train accuracy in Logistic at C=0.01 with lbfgs solver
and max_iter=250.

