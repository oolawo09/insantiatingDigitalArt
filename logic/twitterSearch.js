//includes 

var util = require('util'), 
  twitter = require('twitter'), 
  sentimentAnalysis = require('./sentimentAnalysis'), 
  db = require('diskdb');

db = db.connect('db', ['sentiments']);  

//config
var config = {
  consumer_key: 'NwSVrchUoSuilT6HSKgrEHJKE', 
  consume_secret: 'ZSQdOnVDjj8Up63qQQmLPlqtfcHzhDVAcnQQd5LxkEr0lcizJp', 
  access_token_key: '453809533-2oX8EOHRkPQ9no6ZR5pSIzTNt3usF9zkmjbKbx3m', 
  access_token_secret: 'egG0evEUXEAZdLK5tcMQeSFQNCCE48npCOtkrLq8fRBOF'
}; 

module.exports = function(text, callback) {
 var twitterClient = new twitter(config); 
 var response = [], dbData = []; // to store tweets and sentiment

 twitterClient.search(text, function(data) {
   for(var i=0; i<data.statuses.length; i++){
     var resp = {}; 
     resp.tweet = data.statuses[i]; 
     resp.sentiment = sentimentAnalysis(data.statuses[i].next);
     dbData.push({
       tweet: resp.tweet.text, 
       score: resp.sentiment.score
    }); 
    response.push(resp); 
  };
  db.sentiments.save(dbData);
  callback(response); 
 });
}

