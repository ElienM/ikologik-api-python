from JwtHelper import JwtHelper
from api.services.AbstractIkologikInstallationService import AbstractIkologikInstallationService


class AlertService(AbstractIkologikInstallationService):

    def __init__(self, jwtHelper: JwtHelper):
        super().__init__(jwtHelper)

    # CRUD Actions

    def get_url(self, customer, installation):
        return f'{self.jwtHelper.get_url()}/api/v2/customer/{customer}/installation/{installation}/alert'
