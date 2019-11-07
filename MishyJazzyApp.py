__author__ = 'Mark Mon Monteros'

import ApiIntegration
import kivy, facebook, pyfacebook, flask, json, os, sys, requests

kivy.require('1.11.1')

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.behaviors.button import ButtonBehavior
from kivy.vector import Vector
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.actionbar import ActionBar, ActionItem
from kivymd.theming import ThemeManager
from authlib.client import OAuth2Session
import google.oauth2.credentials
import googleapiclient.discovery
# from oauth2client.client import OAuth2WebServerFlow
# import com.facebook.FacebookSdk;
# import com.facebook.appevents.AppEventsLogger;


class Root(FloatLayout):
    label_wid = ObjectProperty()
    #info = StringProperty()
    fb = StringProperty()
    gg = StringProperty()
    ig = StringProperty()

    def __init__(self, **kwargs):
        super(Root, self).__init__(**kwargs)

        self.label_wid.text = 'Mishy & Jazzy'
        self.fb = 'Facebook'
        self.gg = 'Google'
        self.ig = 'Instagram'
        self.id = ''
        self.name = ''
        self.fname = ''
        self.lname = ''
        self.email = ''
        self.bday = ''

    def login_fb(self):
        APP_DATA = ApiIntegration.Facebook().get_app()
        APP_ID = APP_DATA['id']
        APP_NAME = APP_DATA['name']
        APP_DOMAIN = APP_DATA['link']
        print('APP_ID: ' + str(APP_ID), '\nAPP_NAME: ' + str(APP_NAME), '\nAPP_DOMAIN: ' + str(APP_DOMAIN))
        APP_TOKEN = ApiIntegration.Facebook().get_appToken()['access_token']
        print('APP_TOKEN: ' + str(APP_TOKEN))
        USER_DATA = ApiIntegration.Facebook().authenticate()
        print(USER_DATA)
        userFields = ApiIntegration.Facebook().get_fields()
        print('\nuserFields: ', userFields)

        for i in userFields:
            try:
                print(USER_DATA[i])
                print('Found: ' + str(i)) # fields found
            except KeyError:
                print('Not Found: ' + str(i))  # fields not found -- need facebook permissions

        for i in USER_DATA:
            if i == 'id':
                self.id = str(USER_DATA[i])
            if i == 'name':
                self.name = str(USER_DATA[i])
            if i == 'first_name':
                self.fname = str(USER_DATA[i])
            if i == 'last_name':
                self.lname = str(USER_DATA[i])
            if i == 'email':
                self.email = str(USER_DATA[i])
            if i == 'birthday':
                self.bday = str(USER_DATA[i])

        self.fb = 'Logged in as ' + self.fname

'''
    def login_gg(self):
        app_id = '1194867230686918'
        access_token = 'EAAQZBubTWvsYBAAJklTeBZCZCHukrPt16XKjf1rXDL5tff343QfodA8xLdAnZCBZBbMRe6zVoN0l91xp8nvhuAci3L8sY7dsrZBZAVk1NSZCpDgg4P0j2G4wqQXm4RRXaJaRJsvdyxqCxxOnresJZAiIDdeO35X8nK90ZD'
        app_secret = '4faccbc8c6aae79e0aeb3d32b2c11d92'
        client_token = 'cfdd77be8de6ee97d19b37aee5c8d786'
        domain = 'https://mjposh.com'
        test_app_id = '405301966773403'
        test_app_secret = '4faccbc8c6aae79e0aeb3d32b2c11d92'
        test_user_id = '101587881177123'
        test_user_email = 'kram_xsrhhtf_soretnom@tfbnw.net'
        # https://www.facebook.com/v3.3/dialog/oauth?client_id=405301966773403&redirect_uri=https://broodtech.net
        # self.api = pyfacebook.Api(app_id=app_id, app_secret=app_secret, short_token=access_token)
        self.api = pyfacebook.Api(app_id=app_id, long_term_token=access_token)
        with open('fb.json', 'w', encoding='UTF-8') as f:
            f.write(str(self.api.get_token_info(return_json=True)))

        with open('fb.json', 'r', encoding='UTF-8') as f:
            df = f.read()
            with open('fb_edit.json', 'w', encoding='UTF-8') as edit:
                df2 = df.replace("':", '":')
                df2 = df2.replace("',", ',')
                df2 = df2.replace(",", '",')
                df2 = df2.replace(']"', "]")
                df2 = df2.replace(": '", ": ")
                df2 = df2.replace(": ", ': "')
                df2 = df2.replace('"[', "[")
                df2 = df2.replace('"{', '{')
                df2 = df2.replace("'", '"')
                edit.write(df2)

        with open('fb_edit.json', 'r', encoding='UTF-8') as f:
            json_data = f.read()

        output = json.loads(json_data)
        self.fullName = output['data']['application']
        os.remove('fb.json')
        os.rename('fb_edit.json', 'fb.json')
        self.fname = self.fullName.split(' ')[0]

        self.fb = 'Logged in as ' + self.fname

    def login_gg():
        client_id = '75853028934-f34sog8v1g9i0ckng9lmvukc5l2hm8on.apps.googleusercontent.com'
        client_secret = 'KmDqn7J4jwUEWGoSx85TsJHx'
        api_key = 'AIzaSyAyN1AU6r6yLB1gmrQebI5RlW71aVPHar0'
        end_point = 'https://accounts.google.com/o/oauth2/v2/auth'
        ACCESS_TOKEN_URI = 'https://www.googleapis.com/oauth2/v4/token'
        AUTHORIZATION_URL = 'https://accounts.google.com/o/oauth2/v2/auth?access_type=offline&prompt=consent'
        AUTH_TOKEN_KEY = 'auth_token'
        AUTH_STATE_KEY = 'auth_state'

        oauth2_tokens = flask.session[AUTH_TOKEN_KEY]
        credentials = google.oauth2.credentials.Credentials(
            oauth2_tokens['access_token'],
            refresh_token=oauth2_tokens['refresh_token'],
            client_id=client_id,
            client_secret=client_secret,
            token_uri=ACCESS_TOKEN_URI)

        oauth2_client = googleapiclient.discovery.build(
            'oauth2', 'v2',
            credentials=credentials)

        return oauth2_client.userinfo().get().execute()

        # print(credentials)

        self.gg = 'Logged in as ' + self.fname

    def login_ig(self):
        app_id = '1194867230686918'
        access_token = 'EAAQZBubTWvsYBAAJklTeBZCZCHukrPt16XKjf1rXDL5tff343QfodA8xLdAnZCBZBbMRe6zVoN0l91xp8nvhuAci3L8sY7dsrZBZAVk1NSZCpDgg4P0j2G4wqQXm4RRXaJaRJsvdyxqCxxOnresJZAiIDdeO35X8nK90ZD'
        client_id = '63dc705bb9ef4a8892b887392c8d47a7'
        self.api = pyfacebook.InstagramApi(app_id=app_id, long_term_token=access_token, instagram_business_id=client_id)
        with open('fb.json', 'w', encoding='UTF-8') as f:
            f.write(str(self.api.get_token_info(return_json=True)))

        with open('fb.json', 'r', encoding='UTF-8') as f:
            df = f.read()
            with open('fb_edit.json', 'w', encoding='UTF-8') as edit:
                df2 = df.replace("':", '":')
                df2 = df2.replace("',", ',')
                df2 = df2.replace(",", '",')
                df2 = df2.replace(']"', "]")
                df2 = df2.replace(": '", ": ")
                df2 = df2.replace(": ", ': "')
                df2 = df2.replace('"[', "[")
                df2 = df2.replace('"{', '{')
                df2 = df2.replace("'", '"')
                edit.write(df2)

        with open('fb_edit.json', 'r', encoding='UTF-8') as f:
            json_data = f.read()

        output = json.loads(json_data)
        self.fullName = output['data']['application']
        os.remove('fb.json')
        os.rename('fb_edit.json', 'fb.json')
        self.fname = self.fullName.split(' ')[0]

        self.ig = 'Logged in as ' + self.fname
'''

class MishyJazzyApp(App):
    def build(self):
        return Root()


if __name__ == '__main__':
    mjApp = MishyJazzyApp()
    mjApp.run()
