__author__ = 'fengchaoyi'
#utf

# people, money both array
def calculator(people, money):
    average = sum(money)/len(money)
    recorder = {}
    for i in range(len(people)):
        p = people[i]
        recorder[p]=average-money[i]
    return recorder

# calculate who give how much money to whom
def givemoney(recorder):
    giver = []
    receiver = []
    paystack = []
    for (k,v) in recorder.items():
        if v<0:
            receiver.append(k)
        else:
            giver.append(k)
    i=0
    j = 0
    while (i<len(receiver) and j < len(giver)):
        r = receiver[i]
        g = giver[j]
        if recorder[g]>-(recorder[r]):
            str = g + " give " + `(-(recorder[r]))` + " to " + r
            paystack.append(str)
            recorder[g] += recorder[r]
            recorder[r] = 0
            i+=1
        elif recorder[g]<-(recorder[r]):
            str = g + " give "+ `(recorder[g])`+ " to " + r
            paystack.append(str)
            recorder[r] += recorder[g]
            recorder[g] = 0
            j+=1
        else:
            str = g + " give "+`(recorder[g])` + " to " + r
            paystack.append(str)
            recorder[g] = 0
            recorder[r] = 0
            j+=1
            i+=1
    print 'after givemoney(): '
    print recorder
    return paystack

people = ['a','b','c','d','e','f','g','h','i']
money = [100, 136, 150, 150, 40, 0, 0, 0, 0]
print "money that everyone payed:"
print dict(zip(people, money))
recorder =  calculator(people, money)
print 'before givemoney(): '
print recorder
paystack = givemoney(recorder)
print "so the AAcalculater result is: "
print paystack
