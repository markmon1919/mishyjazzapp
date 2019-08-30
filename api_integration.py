__author__ = 'Mark Mon Monteros'

import os, sys, pyfacebook, json, requests, facebook
import pandas as pd


class ApiIntegration():

	def __init__(self):	
		self.path = os.path.dirname(os.path.realpath(__file__))
		self.logs = self.path + '\\logs'

		self.app_id = ''
		self.access_token = ''
		self.api = ''
		self.json_string = ''

		# self.check_loggedin()
		# self.get_token()
		self.authenticate()

	def get_token(self):
		self.app_id = '1194867230686918'
		app_secret = '4faccbc8c6aae79e0aeb3d32b2c11d92'
		client_token = 'cfdd77be8de6ee97d19b37aee5c8d786'
		domain = 'https://mjposh.com'
		url = 'https://graph.facebook.com/oauth/access_token?'       
		payload = { 'grant_type': 'client_credentials', 'client_id': self.app_id, 'client_secret': app_secret, 'redirect_url': domain}
		response = requests.get(url, params=payload)
		
		if (response.status_code != 200):
			print('Failed to get token! Retrying...') 
			self.get_token()
		else:
			self.access_token = response.json()['access_token']
			print(self.access_token)
			#self.authenticate()

	def check_loggedin(self):
		access_token = 'EAAQZBubTWvsYBAAJklTeBZCZCHukrPt16XKjf1rXDL5tff343QfodA8xLdAnZCBZBbMRe6zVoN0l91xp8nvhuAci3L8sY7dsrZBZAVk1NSZCpDgg4P0j2G4wqQXm4RRXaJaRJsvdyxqCxxOnresJZAiIDdeO35X8nK90ZD'
		app_secret = '4faccbc8c6aae79e0aeb3d32b2c11d92'
		domain = 'https://mjposh.com'
		url = "https://graph.facebook.com/oauth/access_token?"
		payload = { 'client_id': self.app_id, 'client_secret': app_secret, 'fb_exchange_token': fb_exchange_token, 'grant_type':  fb_exchange_token}
		response =  requests.get(url, params=payload)
		print(response)


	def authenticate(self):		
		access_token = 'EAAQZBubTWvsYBAAJklTeBZCZCHukrPt16XKjf1rXDL5tff343QfodA8xLdAnZCBZBbMRe6zVoN0l91xp8nvhuAci3L8sY7dsrZBZAVk1NSZCpDgg4P0j2G4wqQXm4RRXaJaRJsvdyxqCxxOnresJZAiIDdeO35X8nK90ZD'
		graph = facebook.GraphAPI(access_token=access_token)
		pages_data = graph.get_object("/me")

		print(pages_data)

	def parse_json(self):
		return




if __name__ == '__main__':
	ApiIntegration()