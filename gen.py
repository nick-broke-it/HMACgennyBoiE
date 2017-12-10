import random

print "HMAC GEN CREATED BY @NICKSKICKS3"
print "github.com/yeezymane"

macBoiInput = raw_input("Number of Cookies to Generate: ")

try:
    macBOIE = int(macBoiInput)
except:
    print "Put in a fucking number moron"

for i in range(macBOIE):
    thatshit = ["-"]
    for i in range(random.randint(34,42)):
        newNumb = random.randint(0,9)
        thatshit.append(str(newNumb))

    for i in range(random.randint(35,53)):
        alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        boie = random.randint(1,25)

        odds = random.randint(1,6)
        if odds==1:
            newLetter = alphabet[boie].upper()
        else:
            newLetter = alphabet[boie]

        thatshit.append(newLetter)

    cookie = "".join(thatshit)
    print "HMAC COOKIE = {}".format(cookie)
