import pandas as pd
import numpy as np

#You cannot change the names of the functions, the variables, or the default arguments

def make_subset(df, region = None, vaccine = None, year = None, additive = True):
    if additive==False:
        newdf = df[df['Region'].isin(region) | df['Vaccine'].isin(vaccine) | df['Year'].isin(year) ]
    
    elif additive==True and (region != None and vaccine != None and year != None):
        newdf = df[df['Region'].isin(region) & df['Vaccine'].isin(vaccine) & df['Year'].isin(year) ]
    elif additive==True and (region == None  and vaccine != None and year != None):
        newdf = df[df['Year'].isin(year) & df['Vaccine'].isin(vaccine)]
    elif additive==True and (vaccine == None and region != None and year != None):
        newdf = df[df['Region'].isin(region) & df['Year'].isin(year)]
    elif additive==True and (year == None and vaccine != None and region != None):
        newdf = df[df['Region'].isin(region) & df['Vaccine'].isin(vaccine)]
    elif additive==True and (region != None and vaccine == None and year == None):
        newdf = df[df['Region'].isin(region)]
    elif additive == True and (vaccine != None and year == None and region == None):
        newdf = df[df['Vaccine'].isin(vaccine)]
    elif additive == True and (year != None and vaccine == None and region == None):
        newdf = df[df['Year'].isin(year)]
    else:
        newdf = df.copy()
    return newdf
    
        
    
    pass


#if additive == True and (region == None and vaccine == None and year == None):
        #vaccinecopy = df.copy()
        #return vaccinecopy
    #elif additive == True:
        
        #df.loc[(df['Region'] == region) & (df['Vaccine'] == vaccine) & (df['Year'] == year)]

        #newdf = df.loc((df['Region']==(i for i in region)) | (df['Year']==(i for i in year)) | (df['Vaccine']==(i for i in vaccine)))
        #return newdf

        #for i in region:
            #for j in vaccine:
                #for k in year:
                    #newdf = df.loc((df['Region']== i) | (df['Vaccine']==j))