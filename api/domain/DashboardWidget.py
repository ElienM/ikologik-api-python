from api.domain.AbstractIkologikInstallationsObject import AbstractIkologikInstallationsObject


class Parameter:
	key: str = None
	value: str = None

	def __init__(self, key: str, value: str):
		self.key = key
		self.value = value


class DashboardWidget(AbstractIkologikInstallationsObject):
	dashboard: str = None
	dashboardWidgetType: str = None
	type: str = None
	order: int = None
	parameters: [] = []

	def __init__(self, customer: str, installation: str, dashboard: str):
		super().__init__(customer, installation)
		self.dashboard = dashboard
