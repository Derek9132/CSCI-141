from Project_3 import *

list1 = tweets_from_file('SEATTLE_POST.txt')
newdict = top_entries(list1, hashes=True)
#print(newdict)

list2 = tweets_from_file('RICHMONDVOICE.txt')
newdict2 = top_entries(list2, hashes=True)
#print(newdict2)

list3 = tweets_from_file('SEATTLE_POST.txt')
newdict3 = {}
tweetlist1 = []
for tweet in list3:
    tweetlist1.extend(distill_tweet(tweet, punct='.:;$'))
for word in tweetlist1:
    if tweetlist1.count(word) >= 20 and '#' not in word and '@' not in word:
        newdict3[word] = tweetlist1.count(word)
#print(newdict3)

list4 = tweets_from_file('RICHMONDVOICE.txt')
newdict4 = {}
tweetlist2 = []
for tweet in list4:
    tweetlist2.extend(distill_tweet(tweet, punct='.:;$'))
for word in tweetlist2:
    if tweetlist2.count(word) >= 20 and '#' not in word and '@' not in word:
        newdict4[word] = tweetlist2.count(word)
#print(newdict4)

set1 = set(list(newdict.keys()))
set2 = set(list(newdict2.keys()))
#print(set1.difference(set2))

set3 = set(list(newdict3.keys()))
set4 = set(list(newdict4.keys()))
#print(set3.intersection(set4))

print(distill_tweet('hhhttptcocom'))
