from api.domain.AbstractIkologikInstallationsObject import AbstractIkologikInstallationsObject


class Alert(AbstractIkologikInstallationsObject):
	alertType: str = None
	startDate: int = None
	endDate: int = None
	active: bool = None
	severity: str = None
	message: str = None
	availablilityRelated: bool = None
	operationRelated: bool = None
	connectivityRelated: bool = None
	acknowledgeDate: int = None
	meters: str = None
	nrOfComments: int = None

	def __init__(self, customer: str, installation: str):
		super().__init__(customer, installation)
