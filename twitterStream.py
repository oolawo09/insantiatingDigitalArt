import twitter

ckey = 'NwSVrchUoSuilT6HSKgrEHJKE'
csecret = 'ZSQdOnVDjj8Up63qQQmLPlqtfcHzhDVAcnQQd5LxkEr0lcizJp'
atoken = '453809533-2oX8EOHRkPQ9no6ZR5pSIzTNt3usF9zkmjbKbx3m' 
asecret = 'egG0evEUXEAZdLK5tcMQeSFQNCCE48npCOtkrLq8fRBOF' 

auth = twitter.oauth.OAuth(atoken, asecret, ckey, csecret)

twitter_api = twitter.Twitter(auth = auth)

world_woe_id = 1
kenya_woe_id = 1528488
usa_woe_id = 23424977

world_trends = twitter_api.trends.place(_id=world_woe_id)
kenya_trends = twitter_api.trends.place(_id=kenya_woe_id)
usa_trends = twitter_api.trends.place(_id=usa_woe_id)

print world_trends
print 
print kenya_trends 
print 
print usa_trends



