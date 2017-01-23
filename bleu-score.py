import nltk

hypothesis = ['It', 'is', 'a', 'cat', 'at', 'room']
reference = ['It', 'is', 'a', 'cat', 'inside', 'the', 'room']
#there may be several references
BLEUscore = nltk.translate.bleu_score.sentence_bleu([reference], hypothesis)
#for sentances larger than n=4
print BLEUscore

h2 = ["open", "the", "file"]
r2 = ["open", "file"]
#the maximum is bigram, so assign the weight into 2 half.
smallBleuScore = nltk.translate.bleu_score.sentence_bleu([r2], h2, weights = (0.5, 0.5))
print smallBleuScore
