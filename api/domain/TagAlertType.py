from api.domain.AbstractIkologikObject import AbstractIkologikObject


class TagAlertType(AbstractIkologikObject):
	meter: str = None
	value: int = None
	# TODO: check enum
	type: str = None
	# TODO: check enum
	severity: str = None
	message: str = None
	autoAcknowledge: bool = None
	active: str = None
	activationMessageEnabled: bool = None
	activationMessage: str = None
	deactivationMessageEnabled: bool = None
	deactivationMessage: str = None
	availabilityRelated: str = None
	operationRelated: bool = None
	connectivityRelated: bool = None
	notificationReceivers: list = None

	def __init__(self):
		super().__init__()
