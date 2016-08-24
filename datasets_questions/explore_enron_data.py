#!/usr/bin/python

"""
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000

"""

import pickle
import numpy as np

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))


#print len(enron_data)

#poi = {k: v for k, v in enron_data.iteritems() if v['poi'] == 1 }
#print len(poi)

##for key, value in enron_data.iteritems():#
##    print key


## Query the Dataset 1
#print enron_data['PRENTICE JAMES']['total_stock_value']


##How many email messages do we have from Wesley Colwell to persons of interest?
#print enron_data['COLWELL WESLEY']

## Value of stock option exercised by Jeff Skilling
#print enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]

#print enron_data["SKILLING JEFFREY K"]["total_payments"]
#print enron_data["LAY KENNETH L"]["total_payments"]
#print enron_data["FASTOW ANDREW S"]["total_payments"]

#print enron_data["SKILLING JEFFREY K"]

# for key, value in enron_data.iteritems():
#     if value['salary'] != 'NaN':
#         print value['salary']


#d = {k: v for k, v in enron_data.items() if v['salary'] != 'NaN'}
#print len(d)

#filtered_dict = {k:v for k,v in enron_data.iteritems() if v['email_address'] != 'NaN'}
#print len(filtered_dict)


#total_payments = {k:v for k,v in enron_data.iteritems() if v['total_payments'] == 'NaN'}
#print len(enron_data)
#print len(total_payments)



poi = {k:v for k,v in enron_data.iteritems() if v['poi'] == True }
poi_total_payments = {k:v for k,v in poi.iteritems() if v['total_payments'] == 'NaN'}
print len(poi)
print len(poi_total_payments)
