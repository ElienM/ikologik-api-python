from api.services.AbstractIkologikInstallationService import AbstractIkologikInstallationService


class ReportTypeService(AbstractIkologikInstallationService):

	# CRUD Actions

	def get_url(self, customer: str, installation: str):
		return f'{self.api_helper.get_url()}/api/v2/customer/{customer}/installation/{installation}/reporttype'
