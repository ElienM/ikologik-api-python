from api.domain.AbstractIkologikInstallationsObject import AbstractIkologikInstallationsObject


class ReportType(AbstractIkologikInstallationsObject):
	type: str = None
	outputType: str = None
	name: str = None
	title: str = None
	fileName: str = None
	contentType: str = None
	comment: str = None
	scheduleActive: bool = None
	schedule: str = None
	dateEditable: bool = None
	titleEditable: bool = None
	filenameEditable: bool = None
	reviewEnabled: bool = None
	reviewReceivers: list = None
	reviewReceiversSendRequired: bool = None
	notificationReceivers: list = None
	notificationReceiversSendRequired: bool = None

	def __init__(self, customer: str, installation: str):
		super().__init__(customer, installation)
