from IkologikApiCredentials import IkologikApiCredentials
from api.domain.Search import Search
from api.services.AbstractIkologikService import AbstractIkologikService


class DashboardWidgetTypeService(AbstractIkologikService):

    def __init__(self, jwtHelper: IkologikApiCredentials):
        super().__init__(jwtHelper)

    # CRUD Actions

    def get_url(self):
        return f'{self.jwtHelper.get_url()}/api/v2/dashboardwidgettype'

    def get_by_name(self, name: str):
        # Prepare the search
        search = Search()
        search.add_filter("name", "EQ", [name])
        search.add_order("name", "ASC")
        search.set_pagination(0, 1)

        # Query
        result = self.search(search)
        return result[0]

    def get_by_type(self, type: str):
        # Prepare the search
        search = Search()
        search.add_filter("type", "EQ", [type])
        search.add_order("name", "ASC")
        search.set_pagination(0, 1)

        # Query
        result = self.search(search)
        return result[0]
