import datetime
import pandas as pd
import random
import numpy as np

class Forum_Page:

    def __init__(self, name):
        self.__name = name
        self.__board = pd.DataFrame(columns = ['Title','Date', 'Author', 'Post', 'Votes'])
        self.__board.set_index('Title', inplace = True)
        self.__board['Votes'] = self.__board['Votes'].astype('int')
        self.__anon_words = self.__process('words.txt')
        
    
    def __process(self, filename):
        with open(filename,'r', encoding = 'UTF8') as file:
           result = [line.rstrip() for line in file]
        return result
        
    def __exists(self, title):
        return title in self.__board.index
        

    def checker(self):
        return self.__board.copy()
        #public method, returns copy of dataframe, for debugging purposes, should not be called in any submitted files

    def get_name(self):
        return self.__name        
    
    def __generate_anon(self, maxlength = 15, min_num = 1, max_num = 3):
        userStr = ''
        if maxlength < (10 + min_num) or min_num > maxlength or min_num < 0 or max_num < 0 or maxlength < 0:
            print('Invalid specifications')
            return None
        else:
            while userStr == '' or len(userStr) > maxlength or userStr in self.__board['Author'].values:
                word1 = random.choice(self.__anon_words)
                word2 = random.choice(self.__anon_words)
                numList = random.sample(range(0,10), random.choice(range(min_num,max_num+1)))
                numStr = (''.join(str(f) for f in numList))
                userStr = word1 + '_' + word2 + '_' + numStr
        return userStr
        
        
        
        
        pass
        #private (2 leading underscores), select 2 words from word list, select digit, digit must be unique, returns username string or None

    def add_post(self, title, post, author = None, date = None, maxlength = 15, min_num = 1, max_num = 3):
        if author == None:
            author = self.__generate_anon(maxlength, min_num, max_num)
        if date == None:
            date = str(datetime.date.today())
        if self.__exists(title) == False:
            self.__board.loc[title] = [date, author, post, '0']
        return self.__board
        
        pass
        #uses def__exists method to see if title exists
        #1st case: if title exists, return None (should not return None with a line of code)
        #2nd case: 

    def delete_post(self, title):
        if self.__exists(title) == True:
            self.__board.loc[title,'Author'] = np.NaN
            self.__board.loc[title,'Post'] = np.NaN
        pass
        #calls exists method
        #result of delete method: set author and post to be missing
        #change nothing else
    
    def vote_post(self, title, up = True):
        if self.__exists(title) == True and self.__board.loc[title, 'Post'] != np.NaN and self.__board.loc[title, 'Author'] != np.NaN:
            if up == True:
                voteInt = int(self.__board.loc[title, 'Votes'])+1
                self.__board.loc[title, 'Votes'] = str(voteInt)
            elif up ==  False:
                voteInt = int(self.__board.loc[title, 'Votes'])-1
                self.__board.loc[title, 'Votes'] = str(voteInt)
        pass   
        #check that post exists in dataframe, use exists method to avoid errors
        #Make sure post is not deleted; make sure post and author are not missing
        
    def find_author_by_keyword(self, keyword):
        authordf = self.__board.loc[self.__board['Post'].str.contains(keyword, case=False)]
        authorlist = authordf['Author'].values.tolist()
        return authorlist
        pass
        #Use posts column of dataframe
        #returns list of authors
        #should not modify internal dataframe
    
    def get_post_date_info(self, title):
        weekday_convert = {2:'Monday', 3:'Tuesday', 4:'Wednesday', 5:'Thursday', 6:'Friday', 0:'Saturday', 1:'Sunday'} #do not change or delete
        days_in_month = {'01':31, '02':28 , '03':31 , '04':30, '05':31, '06':30, '07':31, '08':31, '09':30, '10':31, '11':30, '12':31} #do not change or delete
        month_number = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'] #do not change or delete
        month_name = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 
                           'September', 'October', 'November', 'December'] #do not change or delete
    
        if self.__exists(title) == True:
            year  = self.__board.loc[title, 'Date'][0:4]
            month = self.__board.loc[title, 'Date'][5:7]
            day = self.__board.loc[title, 'Date'][-2:]
            monthdict = {month_number[i]: month_name[i] for i in range(len(month_number))}
            convert = lambda x : monthdict[x]
            daycount = days_in_month[month] + int(day)
            x='1'
            if month == '01':
                daycount -= 31
                while '0' + x != month:
                    num = days_in_month['0' + x]
                    daycount += num
                    intx = int(x)
                    intx += 1
                    x= str(intx)
            elif int(year)%4 == 0 and int(year)%100 != 0:
                leapYear = {'02': 29}
                days_in_month.update(leapYear)
                while '0' + x != month:
                    num = days_in_month['0' + x]
                    daycount += num
                    intx = int(x)
                    intx += 1
                    x= str(intx)
            else:
                 while '0' + x != month:
                    num = days_in_month['0' + x]
                    daycount += num
                    intx = int(x)
                    intx += 1
                    x= str(intx)

            if month == '02' or month == '01':
                intMonth = int(month) + 12
                K = (int(year)-1)%100
                J = (int(year)-1)//100
                h = (int(day) + (13 * (intMonth + 1))//5 + K + (K//4) + (J//4) - (2 * J)) % 7
            else:
                intMonth = int(month)
                K = (int(year))%100
                J = (int(year))//100
                h = (int(day) + (13 * (intMonth + 1))//5 + K + (K//4) + (J//4) - (2 * J)) % 7
            weekday = weekday_convert[h]
            monthName = convert(month)
            intday = int(day)
            
            if daycount%10 == 1:
                return title + ' posted on ' + weekday + ', ' + monthName + ' ' + str(intday) + ', ' + 'the ' + str(daycount) + 'st day of ' + year
            elif daycount%10 == 2:
                return title + ' posted on ' + weekday + ', ' + monthName + ' ' + str(intday) + ', ' + 'the ' + str(daycount) + 'nd day of ' + year
            elif daycount%10 == 3:
                return title + ' posted on ' + weekday + ', ' + monthName + ' ' + str(intday) + ', ' + 'the ' + str(daycount) + 'nd day of ' + year
            else:
                return title + ' posted on ' + weekday + ', ' + monthName + ' ' + str(intday) + ', ' + 'the ' + str(daycount) + 'th day of ' + year
        


            


        pass
        #Make sure title exists in df (exists method)
        #If title does not exist, returns None
        #If leap year, update dictionary, february days:29
    
    def __str__(self):
        activePosts = self.__board.copy()
        activePosts.dropna(axis = 0, inplace=True)
        postList = list(activePosts.index.values)
        postTitles = '\n'.join(postList)
        print ('Titles for ' + self.__name + ': ' + '\n' + postTitles)


        pass
        #returns string
        #active post means no missing data
        #new dataframe that contains only active posts
        #should not change original dataframe