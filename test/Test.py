import os

from ikologikapi.IkologikApi import IkologikAPI

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
tag = os.getenv('TAG')
second_tag = os.getenv('TAG2')
maintenance_type_id = os.getenv('MAINTENANCE_TYPE')
maintenance_type_field_id = os.getenv('MAINTENANCE_TYPE_FIELD_TYPE')
maintenance_task = os.getenv('MAINTENANCE_TASK')

## Login
print('## Logging-in ##')
api.login()
print('')

## Get customer
print('## Customer ##')
customer = api.customer.get_by_id(customerId)
print(customer.name)
print('')

## List installations
print('## Installations ##')
installations = api.installation.list(customerId)
for installation in installations:
    print(installation.name)
print('')

# ## List tags
# print('## Tags ##')
# tags = api.tag.list(customerId, installationId)
# for tag in tags:
#     print(tag.name)
# print('')
#
# ## List dashboards
# print('## Dashboards ##')
# dashboards = api.dashboard.list(customerId, installationId)
# for dashboard in dashboards:
#     print(dashboard.name)
# print('')
#
# ## List dashboard widget types
# print('## Dashboard widget type ##')
# dashboardWidgetTypes = api.dashboardWidgetType.list()
# for dashboardWidgetType in dashboardWidgetTypes:
#     print(dashboardWidgetType.name)
# print('')
#
# ## List data import types
# print('## Data import type ##')
# dataImportTypes = api.dataImportType.list(customerId, installationId)
# for dataImportType in dataImportTypes:
#     print(dataImportType.name)
# print('')

## List shop product groups
print('## Shop - Product groups ##')
productGroups = api.customerShopProductGroup.list(customerId)
for productGroup in productGroups:
    print(productGroup.code + ' - ' + productGroup.name)
print('')

## List shop products
print('## Shop - Products ##')
products = api.customerShopProduct.list(customerId)
for product in products:
    print(product.code + ' - ' + product.description)
print('')

## List shop product images
print('## Shop - Product images ##')
images = api.customerShopProductImage.list(customerId, products[0].id)
for image in images:
    print(image.fileName)
    if hasattr(image, 'uploadUrl') and image.uploadUrl is not None:
        print(f'- Upload:    {image.uploadUrl}')
    if hasattr(image, 'imageUrl') and image.imageUrl is not None:
        print(f'- Image:     {image.imageUrl}')
    if hasattr(image, 'viewUrl') and image.viewUrl is not None:
        print(f'- View:      {image.viewUrl}')
    if hasattr(image, 'thumbnailUrl') and image.thumbnailUrl is not None:
        print(f'- Thumbnail: {image.thumbnailUrl}')
print('')

## Get shop product image - Upload
print('## Shop - Product images - Upload ##')
upload_url = api.customerShopProductImage.upload(customerId, products[0].id, images[0].id)
print(upload_url)
print('')

## Get shop product image - Image
print('## Shop - Product images - Image ##')
image_url = api.customerShopProductImage.image(customerId, products[0].id, images[0].id)
print(image_url)
print('')

## Get shop product image - View
print('## Shop - Product images - View ##')
view_url = api.customerShopProductImage.view(customerId, products[0].id, images[0].id)
print(view_url)
print('')

## Get shop product image - Thumbnail
print('## Shop - Product images - Thumbnail ##')
thumbnail_url = api.customerShopProductImage.thumbnail(customerId, products[0].id, images[0].id)
print(thumbnail_url)
print('')
