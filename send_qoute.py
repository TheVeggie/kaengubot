from twython import Twython
import random

zitateDatei = open('zitateFile.txt')
personDatei = open('personen.txt')
zitate = zitateDatei.readlines()
person = personDatei.readlines()
zitateDatei.close()
personDatei.close()


apiKey = ''
apiSecret = ''
accessToken = ''
accessTokenSecret = ''

api = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)

zufallsZahl1 = random.randint(0, len(zitate)-1)
zufallsZahl2 = random.randint(0, len(person)-1)

tweet = zitate[zufallsZahl1] + person[zufallsZahl2]
print(tweet)

api.update_status(status=tweet)
