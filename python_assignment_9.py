sentence = input("bir cümle giriniz. ")
def function(sentence):
    return dict((i,sentence.count(i)) for i in sentence)
print(function(sentence))