from IkologikApiCredentials import IkologikApiCredentials
from services.DashboardService import DashboardService
from services.DashboardWidgetTypeService import DashboardWidgetTypeService
from services.InstallationService import InstallationService
from services.TagService import TagService


class IkologikAPI:

    def __init__(self, url: str, username: str, password: str):
        self.apiCredentials = IkologikApiCredentials(url, username, password)
        self.dashboard = DashboardService(self.apiCredentials)
        self.dashboardWidgetType = DashboardWidgetTypeService(self.apiCredentials)
        self.installation = InstallationService(self.apiCredentials)
        self.tag = TagService(self.apiCredentials)
