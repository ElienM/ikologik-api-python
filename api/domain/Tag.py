from api.domain.AbstractIkologikInstallationsObject import AbstractIkologikInstallationsObject


class Tag(AbstractIkologikInstallationsObject):
	type: str = None
	name: str = None
	identification: str = None
	description: str = None
	group: str = None
	importStatus: str = None
	unit: int = None
	valueType: str = None
	valueTimeUnit: str = None
	decimalPrecision: int = None
	color: str = None
	visible: bool = None
	visibleTroubleshooting: bool = None
	gridAlignmentValue: int = None
	gridAlignmentUnit: int = None
	transformationActive: bool = None
	transformationMultiplier: int = None
	transformationAdd: float = None
	transformationRounding: int = None
	minLimit: float = None
	lowLowLimit: float = None
	lowLimit: float = None
	highLimit: float = None
	maxLimit: float = None
	highHighLimit: float = None
	maxLimit: float = None
	medianActive: bool = None
	epsilon: int = None
	medianActive: bool = None
	medianSampleSize: int = None
	trendActive: bool = None
	trendSampleSize: int = None
	epsilon: float = None
	dataImportStatus: str = None
	lastDataImportStatusUpdate: int = None

	def __init__(self, customer: str, installation: str):
		super().__init__(customer, installation)
