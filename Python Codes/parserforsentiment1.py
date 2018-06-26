import csv
from nltk.corpus import stopwords
import re
import string

stop = stopwords.words('english')

inter1 = []
posts_clean = []
posts = []
posts_found_with_brand = []
limited_post = []
limited_post2 = []

with open('USAvsROTW.csv') as f:
    rows = csv.reader(f, delimiter = ',')
    for row in rows:
        inter1.append(row[2])
        #print row[2]
        #print "--------------------"

for row in inter1:
    #print "Entering inter1"
    sentences_all = []
    sentences = re.split(r' *[\.\?!][\'"\)\]]* *', row)
    for s in sentences:
        #print "Entering 1st secnday loop"
        in1 = ''.join(s)
        out = re.sub('[%s]' % re.escape(string.punctuation), '', in1.lower())
        sentences_all.append(out)
    posts.append(sentences_all)

for post in posts:
    #print "Entering 2nd main"
    sentences_clean = []
    for sentence in post:
        #print "Enter 2nd secondary"
        s = []
        for i in sentence.split():
            if i not in stop:
                s.append(i)
        sentences_clean.append(s)
    posts_clean.append(sentences_clean)

nb = raw_input('bitcoin')
nb2 = raw_input('usa001')
nb3 = raw_input('20')

for post in posts_clean:
    #print "Entering posts_clean"
    for sentence in post:
        #print "Entering sentences in posts "
        x = 0
        for i in sentence:
            #print "Entering sentences in sentences "
            if(i == nb):
                x = 1
                posts_found_with_brand.append(post)
                break

        if(x == 1):
            #print "Break coz x = 1 "
            break


limit = int(nb3) + 1

for post in posts_found_with_brand:
    print "Enter posts_found_with_brand"
    sentence_with_attribute = []
    position_in_sentences = []
    for sentence in post:
        print "Sentence in post"
        position  = 0
        for i in sentence:
            print "i in Sentence"
            if(i == nb2):
                position_in_sentences.append(position)
                sentence_with_attribute.append(sentence)
            position = position + 1

    j = 0
    for sentence in sentence_with_attribute:
        print "sentence_with_attribute"
        limited_sentence = []
        for i in range(len(sentence)):
            print "Length sentence"
            if(abs(i - position_in_sentences[j]) < limit):
                limited_sentence.append(sentence[i])
        j = j + 1
        limited_post.append(limited_sentence)


# print limited_post

for sent in limited_post:
    limited_post2.append(' '.join(sent))

# for sent in limited_post2:
#   print sent

writer = csv.writer(open('bitcoin_usa.csv', 'wb'))
for sent in limited_post2:
    writer.writerow([sent])


print "written limit_post.csv"

