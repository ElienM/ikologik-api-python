from api.domain import Dashboard
from api.domain.Search import Search
from api.services.AbstractIkologikInstallationService import AbstractIkologikInstallationService


class DashboardService(AbstractIkologikInstallationService):

	# CRUD Actions

	def get_url(self, customer, installation):
		return f'{self.api_helper.get_url()}/api/v2/customer/{customer}/installation/{installation}/dashboard'

	def get_by_name(self, customer: str, installation: str, name: str) -> Dashboard:
		# Prepare the search
		search = Search()
		search.add_filter("name", "EQ", [name])
		search.add_order("name", "ASC")
		search.set_pagination(0, 1)

		# Query
		result = self.search(customer, installation, search)
		return result[0]
