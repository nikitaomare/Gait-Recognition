import os
import time

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import scale, StandardScaler
from sklearn.svm import LinearSVC

## data preprocessing
from matplotlib.pyplot import imshow
import numpy as np
import os
from skimage import io
import PIL
from PIL import Image,ImageOps
X = []
y = []

for sub_dir in os.listdir('Depth_Cropped'):
    label=int(sub_dir[1:])
    k=0
    for sub_dir2 in os.listdir(os.path.join('Depth_Cropped', sub_dir)):
        
        for i in (os.path.join('Depth_Cropped', sub_dir,sub_dir2)):
            if i=='n':
                    k=k+1
                    
                
                
                    image1=np.zeros((250,200))
                    j=0
                    for j,sub_dir3 in enumerate(os.listdir(os.path.join('Depth_Cropped',sub_dir,sub_dir2)),1):
                         if   sub_dir3.endswith('.png'):
                          
                             filename=(os.path.join('Depth_Cropped',sub_dir,sub_dir2,sub_dir3))
                             col=Image.open(filename)
                             if k%2==0:
                              
                              #col=Image.open(filename)
                                  col=ImageOps.mirror(col)
                             gray=col.convert('L')
                             bw=np.asarray(gray).copy()
                          
                             bw=gray.point(lambda x:0 if x<128 else 255)
                             image1=image1+bw
            
        
 

                    X.append(image1/j)
                    y.append(label)
        
X = np.array(X, dtype='float64')
y = np.array(y)

print("X.shape: {}, y.shape: {}".format(X.shape, y.shape))


##apply lg
X=X.reshape(X.shape[0],-1)
pca=PCA(.99)
X=pca.fit_transform(X)
print('X.shape:'+str(X.shape)+',y.shape:'+str(y.shape))
x_train,x_test,y_train,y_test=train_test_split(X,y,test_size=.2)
lg=LogisticRegression(multi_class='multinomial',solver='lbfgs')
lg=lg.fit(x_train,y_train)
y_pred=lg.predict(x_test)
acc=accuracy_score(y_test,y_pred)
print('accuracy:'+str(acc))
