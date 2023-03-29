import datetime
import pandas as pd
import random
import numpy as np
from Forum_Page import *

#Do not change the lists below 
title_list = ['A Post', 'Final_Project', 'Potato_Recipe', 'Pandas', 'Override']
post_text_list = ['This post is about nothing', 'You are working on the CSCI 141 Final Project', 'There \
are lots of ways to make potatoes', 'Pandas is used to analyze data', 'For students who need overrides \
to enroll in CSCI classes, the Computer Science Department will be releasing a centralized \
override system to handle all requests.']
#Write your main program code here
CSCI_141 = Forum_Page('CSCI_141')
CSCI_141.add_post(title='A Post', post='This post is about nothing', maxlength=15, min_num=2, max_num=5)
CSCI_141.add_post(title='Final_Project', post='You are working on the CSCI 141 Final Project', maxlength=15, min_num=2, max_num=5)
CSCI_141.add_post(title='Potato_Recipe', post='There are lots of ways to make potatoes', maxlength=15, min_num=2, max_num=5)
CSCI_141.add_post(title='Pandas', post='Pandas is used to analyze data', maxlength=15, min_num=2, max_num=5)
CSCI_141.add_post(title='Override', post='For students who need overrides to enroll in CSCI classes, the Computer Science Department will be releasing a centralized \
override system to handle all requests.', maxlength=15, min_num=2, max_num=5)
CSCI_141.vote_post('Final Project', up=True)
CSCI_141.vote_post('Final Project', up=True)
CSCI_141.vote_post('Final Project', up=True)
CSCI_141.vote_post('Final Project', up=True)
CSCI_141.vote_post('Final Project', up=True)
print(CSCI_141.find_author_by_keyword('CSCI'))
CSCI_141.delete_post('Potato_Recipe')
CSCI_141.get_post_date_info('Pandas')
CSCI_141.__str__()

