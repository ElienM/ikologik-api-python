from api.domain.AbstractIkologikInstallationsObject import AbstractIkologikInstallationsObject


class Dashboard(AbstractIkologikInstallationsObject):
	name: str = None

	def __init__(self, customer: str, installation: str):
		super().__init__(customer, installation)
