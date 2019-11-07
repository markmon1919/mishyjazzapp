__author__ = 'Mark Mon Monteros'

import MishyJazzyApp
import os, sys, pyfacebook, json, requests, facebook
import pandas as pd


class Facebook():

	def __init__(self):
		self.APP_ID = '1194867230686918'
		self.DOMAIN = 'https://graph.facebook.com'
		self.USER_TOKEN = 'EAAQZBubTWvsYBAAJklTeBZCZCHukrPt16XKjf1rXDL5tff343QfodA8xLdAnZCBZBbMRe6zVoN0l91xp8nvhuAci3L8sY7dsrZBZAVk1NSZCpDgg4P0j2G4wqQXm4RRXaJaRJsvdyxqCxxOnresJZAiIDdeO35X8nK90ZD'
		self.request = ''
		self.usr_fields = ['id', 'name', 'first_name', 'last_name', 'email', 'birthday']

	def get_app(self):
		self.request = requests.get(self.DOMAIN + '/' + self.APP_ID)
		return self.response_body()

	def get_appToken(self):
		CLIENT_TOKEN = 'cfdd77be8de6ee97d19b37aee5c8d786'
		APP_SECRET = '4faccbc8c6aae79e0aeb3d32b2c11d92'
		PARAMS = {'grant_type': 'client_credentials', 'client_id': self.APP_ID, 'client_secret': APP_SECRET}
		ENDPOINT = 'oauth/access_token?'
		self.request = requests.get(self.DOMAIN + '/' + ENDPOINT, params=PARAMS)
		return self.response_body()

	def get_fields(self):
		return self.usr_fields

	def authenticate(self):
		graph = facebook.GraphAPI(access_token=self.USER_TOKEN)
		ENDPOINT = '/me?fields='
		self.request = graph.get_object(ENDPOINT + str(self.usr_fields))
		return self.graph_response()

	def response_body(self):
		if self.request.status_code != 200:
			print('Failed! Retrying...')
			MishyJazzyApp.Root.login_fb()
		else:
			print('\nSuccess!')
			return self.request.json()

	def graph_response(self):
		print('\nSuccess!')
		return self.request
