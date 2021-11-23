from api.services.AbstractIkologikInstallationService import AbstractIkologikInstallationService


class AlertService(AbstractIkologikInstallationService):

	# CRUD Actions

	def get_url(self, customer, installation):
		return f'{self.api_helper.get_url()}/api/v2/customer/{customer}/installation/{installation}/alert'
