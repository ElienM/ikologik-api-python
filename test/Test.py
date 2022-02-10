import os

from ikologikapi.IkologikApi import IkologikAPI

## Prepare the API
api = IkologikAPI(
    url=os.getenv('URL'),
    username=os.getenv('USERNAME'),
    password=os.getenv('PASSWORD'),
)

## Load the customer and installation id's
customerId = os.getenv('CUSTOMER')
installationId = os.getenv('INSTALLATION')
dataImportTypeId = os.getenv('DATAIMPORTTYPE')
dataImportId = os.getenv('DATAIMPORT')

## List installations
print('## Installations ##')
installations = api.installation.list(customerId)
for installation in installations:
    print(installation.name)
print('')

## List tags
print('## Tags ##')
tags = api.tag.list(customerId, installationId)
for tag in tags:
    print(tag.name)
print('')

## List dashboards
print('## Dashboards ##')
dashboards = api.dashboard.list(customerId, installationId)
for dashboard in dashboards:
    print(dashboard.name)
print('')

## List dashboard widget types
print('## Dashboard widget type ##')
dashboardWidgetTypes = api.dashboardWidgetType.list()
for dashboardWidgetType in dashboardWidgetTypes:
    print(dashboardWidgetType.name)
print('')

## List data import types
print('## Data import type ##')
dataImportTypes = api.dataImportType.list(customerId, installationId)
for dataImportType in dataImportTypes:
    print(dataImportType.name)
print('')
