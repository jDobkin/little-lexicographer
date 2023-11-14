import ckanapi, csv

base_url = 'url_to_your_ckan_instance'
api_key = ''
output_file = 'new_data_dicts.csv'

package_urls = [
'link to dataset',
'link to dataset'
]

ckan = ckanapi.RemoteCKAN(base_url, apikey=api_key)

resource_data = []

for package_url in package_urls:
    # Extract package ID from the URL
    package_id = package_url.split('/')[-1]

    # Retrieve package metadata
    package_info = ckan.action.package_show(id=package_id)

    # Retrieve resources for the package
    for resource in package_info['resources']:
        resource_id = resource['id']
        resource_info = ckan.action.resource_show(id=resource_id)
        resource_url = resource_info['url']
        resource_data.append([package_id, resource['name'], resource_url])

with open(output_file, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Package ID', 'Resource Name', 'Resource URL'])
    for data in resource_data:
        writer.writerow(data)