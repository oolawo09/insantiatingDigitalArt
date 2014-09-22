#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import jinja2
import webapp2
import twitter 
import json
import os
import urllib


ckey = 'NwSVrchUoSuilT6HSKgrEHJKE'
csecret = 'ZSQdOnVDjj8Up63qQQmLPlqtfcHzhDVAcnQQd5LxkEr0lcizJp'
atoken = '453809533-2oX8EOHRkPQ9no6ZR5pSIzTNt3usF9zkmjbKbx3m'
asecret = 'egG0evEUXEAZdLK5tcMQeSFQNCCE48npCOtkrLq8fRBOF'

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class MainHandler(webapp2.RequestHandler):
    
    def get(self):
        self.getData()
    
    def getData(self):
        #authentication 
        kenya_woe_id = 1528488
        auth = twitter.oauth.OAuth(atoken, asecret, ckey, csecret)
        twitter_api = twitter.Twitter(auth = auth)
        #pulling data
        kenya_trends = twitter_api.trends.place(_id=kenya_woe_id)
        # self.response.write(json.dumps(kenya_trends, indent=1))
        trends = kenya_trends[0]['trends'];
        self.response.write('Trending in Nairobi today: </br>')
        #creating template_values
        template_values = {}
        for trend in trends: 
            self.response.write(trend['name'] + '</br>')
            self.response.write(' ')

            
    

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
