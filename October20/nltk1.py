import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords

EXAMPLE_TEXT = "Hello Mr. Smith, how are you doing today? the weather is great and " \
                "Python is awesome. The sky is pinkish-blue. You shouldn't eat carboard! " \
                "I am so blue I'm greener than purple. I stepped on a Corn Flake, now I'm " \
                "a Cereal Killer. Everyday a grape licks a friendly cow. Look, a distraction! " \
                "If your canoe is stuck in a tree with the headlights on, how many pancakes " \
                "does it take to get to the moon?"

w = "It is important to by very pythonly while you are pythoning with python. All pythoners have pythoned poorly at least once."

print(set(stopwords.words('english')))

print(EXAMPLE_TEXT)
print()

ps = PorterStemmer()

for word in word_tokenize(w):
    print(ps.stem(word))


#Tokenizes sentences from paragraph
print(sent_tokenize(EXAMPLE_TEXT))
print()
#Tokenizes words from paragraph
print(word_tokenize(EXAMPLE_TEXT))
