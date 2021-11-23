import json
from types import SimpleNamespace

import requests

from api.services.AbstractIkologikInstallationService import AbstractIkologikInstallationService


class TagAlertTypeService(AbstractIkologikInstallationService):

	def get_url(self, customer, installation, tag):
		return f'{self.api_helper.get_url()}/api/v2/customer/{customer}/installation/{installation}/tag/{tag}/tagalerttype/update'

	def update(self, customer, installation, tag, o: object):
		try:
			data = json.dumps(o, default=lambda o: o.__dict__)
			response = requests.post(
				self.get_url(customer, installation, tag),
				data=data,
				headers=self.get_headers()
			)
			result = json.loads(response.content, object_hook=lambda d: SimpleNamespace(**d))
			return result
		except requests.exceptions.HTTPError as error:
			print(error)
