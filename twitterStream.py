import twitter
import json 

ckey = 'NwSVrchUoSuilT6HSKgrEHJKE'
csecret = 'ZSQdOnVDjj8Up63qQQmLPlqtfcHzhDVAcnQQd5LxkEr0lcizJp'
atoken = '453809533-2oX8EOHRkPQ9no6ZR5pSIzTNt3usF9zkmjbKbx3m' 
asecret = 'egG0evEUXEAZdLK5tcMQeSFQNCCE48npCOtkrLq8fRBOF' 

auth = twitter.oauth.OAuth(atoken, asecret, ckey, csecret)

twitter_api = twitter.Twitter(auth = auth)

kenya_woe_id = 1528488

kenya_trends = twitter_api.trends.place(_id=kenya_woe_id)

print json.dumps(kenya_trends, indent=1)
 



