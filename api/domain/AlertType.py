from api.domain.AbstractIkologikInstallationsObject import AbstractIkologikInstallationsObject


class AlertType(AbstractIkologikInstallationsObject):
	severity: str = None
	message: str = None
	autoAchnowledge: bool = None
	active: bool = None
	timeoutActivation: int = None
	activationMessageEnabled: bool = None
	timeoutDeactivation: int = None
	deactivationMessageEnabled: bool = None
	deactivationMessage: str = None
	availabilityRelated: bool = None
	operationRelated: bool = None
	connectivitiyRelated: bool = None
	criteria: list = None
	notificationReceivers: list = None
	notificationMessageLanguage: str = None
	notificationMessageRepeat: int = None

	def __init__(self, customer: str, installation: str):
		super().__init__(customer, installation)
