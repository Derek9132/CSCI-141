#Do not change any of the import lines
import pandas as pd
import numpy as np
from Project_4 import *


#Part 1: Data QC
#Do not change the order of lines
#Maintain the original structures (if there is a lambda, use a lambda etc)

#Read in the data
vaccineData = pd.read_csv('vaccine_data.csv')
#Assign column names
vaccineData.columns=['Region','Vaccine','Year','Percentage']
#Update region names to replace & with and and remove spaces
vaccineData['Region']=vaccineData['Region'].str.replace('&','and').str.replace(' ','_')
#Change type of Year column to a string
vaccineData['Year'] = vaccineData['Year'].astype('str')
#Create description column
#The dictionary line is correct, you must use the dictionary
mappings = {'BCG':'tuberculosis', 'DTP1':'diphteria_pertussis_tetanus','DTP3': 'diptheria_pertussis_tetanus',\
'MCV1':'meningococcal_disease','MCV2':'meningococcal_disease','HEPBB':'hepatitis B', 'HEPB3':'hepatitis B',\
'HIB1':'Haeomphilus influenza', 'HIB3':'Haemophilus influenza','IPV1': 'polio','IPV3': 'polio', 'POL3': 'polio','PCV3':'pneumococcal disease', 'RCV1':'rubella',\
'ROTAC':'rotavirus','YFV':'Yellow Fever Virus'}
vaccineData['Description'] = vaccineData['Vaccine'].apply(lambda x: mappings[x])
#Drop any rows with missing data (ANY missing data)
vaccineData.dropna(axis=0,inplace=True)
#Check the data frame before continuing
print(vaccineData)


#Part 3: Putting it all together
BCG_2019 = make_subset(vaccineData, vaccine = ['BCG'], year = ['2019'])
DTP1_Years = make_subset(vaccineData, region=['East_Asia_and_Pacific'], vaccine=['DTP1'], year=['1980'], additive=False)
BCG2019_Series = pd.Series(data = BCG_2019['Percentage'].values, index = BCG_2019['Region'])
DTP1_Series = pd.Series(data = DTP1_Years['Percentage'].values, index = DTP1_Years['Year'])
#print(BCG2019_Series)
#print(DTP1_Years)
#print(DTP1_Series)
#print(BCG_2019)
#print(make_subset(vaccineData, region=['Eastern_and_Southern_Africa'], vaccine=['ABC1', 'ABC2'], additive=True))









