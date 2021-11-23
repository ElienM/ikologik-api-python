from api.domain.AbstractIkologikInstallationsObject import AbstractIkologikInstallationsObject


class Batch(AbstractIkologikInstallationsObject):
	batchType: str = None
	code: str = None
	description: str = None
	status: str = None
	startDate: float = None
	endDate: float = None
	active: bool = None
	fields: dict = None

	def __init__(self, customer: str, installation: str):
		super().__init__(customer, installation)
