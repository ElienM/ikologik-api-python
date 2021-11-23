from api.domain.AbstractIkologikCustomerObject import AbstractIkologikCustomerObject


class AbstractIkologikInstallationsObject(AbstractIkologikCustomerObject):
	installation: str = None

	def __init__(self, customer: str, installation: str):
		super().__init__(customer)
		self.installation = installation
