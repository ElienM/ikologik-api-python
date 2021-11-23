import json
import time

import boto3
import requests


class IkologikAPI:
	secret = None
	url = None
	username = None
	password = None
	jwt = None
	access_token = None

	def get_secret(self):
		return None

	def get_url(self):
		if self.url is None:
			# Get url
			secret = self.get_secret()
			self.url = secret['url']

			return self.url
		else:
			return self.url

	def get_username(self):
		if self.username is None:
			# Get username
			secret = self.get_secret()
			self.username = secret['username']

			return self.username
		else:
			return self.url

	def get_password(self):
		if self.password == None:
			# Get password
			secret = self.get_secret()
			self.password = secret['password']

			return self.password
		else:
			return self.url

	def get_jwt(self):
		if self.jwt is None:
			# Get jwt
			data_get = {
				"username": self.get_username(),
				"password": self.get_password()
			}
			headers = {
				'Content-Type': 'application/json'
			}
			response = requests.post(
				f'{self.get_url()}/api/v2/auth/login',
				data=json.dumps(data_get),
				headers=headers,
				verify=False
			)
			access_token = json.loads(response.text)
			access_token = access_token['accessToken']
			self.jwt = access_token
			time.sleep(10)
			return self.jwt
		else:
			return self.jwt
