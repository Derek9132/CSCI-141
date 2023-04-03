ENG_WORDS = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", 
             "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 
             'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 
             'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 
             'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 
             'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 
             'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 
             'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 
             'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 
             'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 
             'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 
             'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 
             'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', 
             "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', 
             "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', 
             "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"] 

def distill_tweet(str_tweet, punct = '.,;!?":/'):
    words = str_tweet.lower().translate(str_tweet.maketrans("'",' ', punct)).translate(str_tweet.maketrans("-",' ')).translate(str_tweet.maketrans("’",' ')).split()
    result = []
    for word in words:
        if word not in ENG_WORDS and word[0:4] != 'http' and not word.isnumeric():
            result += [word]
    return result

def top_entries(tweets, min_count = 1, hashes = False, mentions = False, punct = '.,;!?":/'):
    hashdict = {}
    mentiondict = {}
    worddict = {}
    tweetlist = []
    for t in tweets:
      tweetlist.extend(distill_tweet(t, punct))
    for word in tweetlist:
      if word[0:1] == '#' and tweetlist.count(word) >= min_count:
        hashdict[word] = tweetlist.count(word)
      if word[0:1] == '@'and tweetlist.count(word) >= min_count:
        mentiondict[word] = tweetlist.count(word)
      if word[0:1] != '#' and word[0:1] != '@' and tweetlist.count(word) >= min_count:
        worddict[word] = tweetlist.count(word)
    if hashes == True:
      return hashdict
    elif hashes == False and mentions == True:
      return mentiondict
    elif hashes == False and mentions == False:
      return worddict
      

def tweets_from_file(filename): 
  tweetlist = []
  with open(filename, 'r', encoding = 'UTF-8') as tweets:
    for line in tweets:
      tweetlist.append(line.rstrip())
  return tweetlist
    
  
        


#Do not put your main program or any other lines of code here
