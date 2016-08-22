#!/usr/bin/python

"""
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess

def svc(cvalue):
    ### features_train and features_test are the features for the training
    ### and testing datasets, respectively
    ### labels_train and labels_test are the corresponding item labels
    features_train, features_test, labels_train, labels_test = preprocess()

    #########################################################
    ### your code goes here ###

    #########################################################

    ########################## SVM #################################
    ### we handle the import statement and SVC creation for you here

    from sklearn.svm import SVC
    ##clf = SVC(kernel="linear")
    clf = SVC(kernel="rbf", C=cvalue)

    #### now your job is to fit the classifier
    #### using the training features/labels, and to
    #### make a set of predictions on the test data

    #features_train = features_train[:len(features_train)/100]
    #labels_train = labels_train[:len(labels_train)/100]

    t0 = time()
    print "Start training:", round(t0, 3), "s"
    clf.fit(features_train, labels_train)
    print "training time;", round(time()-t0,3), "s"

    #### store your predictions in a list named pred
    pred = clf.predict(features_test)


    from sklearn.metrics import accuracy_score
    acc = accuracy_score(pred, labels_test)
    print acc

    return pred.tolist()

def submitAccuracy():
    return acc


#svc(1)
#svc(100)
#svc(1000)
result = svc(10000)
#svc(100000)
print result.count(1)
