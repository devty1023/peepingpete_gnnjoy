#-*- coding: utf-8 -*-
# coding=utf-8
import tweepy
from app_config import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET


class TpTwt:
    def __init__(self):
        self.consumer_key = CONSUMER_KEY
        self.consumer_secret = CONSUMER_SECRET
        self.access_token = ACCESS_TOKEN
        self.access_token_secret = ACCESS_TOKEN_SECRET

    '''
    updateTwt(self, userInfo)
    userInfo contains:
        userInfo['twtid']
        userInfo['username']
        userInfo['course']
        userInfo['seat']
    '''
    def updateTwt(self, userInfo):
        # generate custom message
        msg = '@' + userInfo['twtid'] + ' 용채형! ' + str(userInfo['course']) + '에 자리 ' + str(userInfo['seat']) + '개 나왔어요!'

        # post to twitter
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)
        api = tweepy.API(auth)

        try:
            api.update_status(msg)
        except tweepy.TweepError as e:
            print e
            print 'status update failed'
            return False

        return True

    def sendDM(self, twtid, message):
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)
        api = tweepy.API(auth)

        try:
            api.send_direct_message(text=message, user=twtid)
        except tweepy.TweepError as e:
            print e[0][0]['code']
            return e[0][0]['code']

        return 0


if __name__ == '__main__':
    tptwt = TpTwt()
    user = { 'twtid': 'ltae9110', 'course': 'test', 'seat': 0 }
    #bstwt.updateTwt(user)
    tptwt.updateTwt(user)
