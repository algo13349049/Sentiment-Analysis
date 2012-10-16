#! /usr/bin/env python

from conceptnet.models import *
import nltk
from collections import Counter

en = Language.get('en')


f = open('X.emotions','w')

X = []

raw = []

basic_emotions = ['happy','sad','anger','fear','disgust','surprise']


for i in basic_emotions:
	assertions = Assertion.objects.filter(concept2__text= i , language=en)

	for a in assertions:
		raw.extend(a.rawassertion_set.all())
	for r in raw:
		X.append( str(r.surface1) )


count = Counter(X)

X_tuple = []

for i in count:
	t = (i, count[i])
	X_tuple.append(t)


sorted_by_second = sorted( X_tuple, key = lambda tup:-tup[1])

print sorted_by_second


for i in sorted_by_second:
	if( len(nltk.word_tokenize(i[0])) == 1 ):
		print >>f , i[0], "\t", i[1] 
		f.flush()	

f.close()

