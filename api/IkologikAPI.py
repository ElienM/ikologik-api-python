from JwtHelper import JwtHelper
from services.DashboardService import DashboardService
from services.DashboardWidgetTypeService import DashboardWidgetTypeService
from services.InstallationService import InstallationService
from services.TagService import TagService


class IkologikAPI:

    def __init__(self, url: str, username: str, password: str):
        self.jwtHelper = JwtHelper(url, username, password)
        self.dashboards = DashboardService(self.jwtHelper)
        self.dashboardWidgetTypes = DashboardWidgetTypeService(self.jwtHelper)
        self.installations = InstallationService(self.jwtHelper)
        self.tags = TagService(self.jwtHelper)
