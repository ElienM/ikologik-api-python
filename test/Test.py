import os

from IkologikAPI import IkologikAPI

## Prepare the API
api = IkologikAPI(
    url=os.getenv('URL'),
    username=os.getenv('USERNAME'),
    password=os.getenv('PASSWORD')
)

## Load the customer and installation id's
customerId = os.getenv('CUSTOMER')
installationId = os.getenv('INSTALLATION')

## List installations
print('## Installations ##')
installations = api.installations.list(customerId)
for installation in installations:
    print(installation.name)
print('')

## List dashboards
print('## Dashboards ##')
dashboards = api.dashboards.list(customerId, installationId)
for dashboard in dashboards:
    print(dashboard.name)
print('')

## List dashboard widget types
print('## Dashboard widget type ##')
dashboardWidgetTypes = api.dashboardWidgetTypes.list()
for dashboardWidgetType in dashboardWidgetTypes:
    print(dashboardWidgetType.name)
print('')

## List tags
print('## Tags ##')
tags = api.tags.list(customerId, installationId)
for tag in tags:
    print(tag.name)
print('')
