import ckanapi, csv

base_url = 'https://catalog.dvrpc.org'
api_key = ''
output_file = 'new_data_dicts.csv'

package_urls = [
'https://catalog.dvrpc.org/dataset/air-quality-violations',
'https://catalog.dvrpc.org/dataset/bridge-conditions',
'https://catalog.dvrpc.org/dataset/business-formations',
'https://catalog.dvrpc.org/dataset/community-integration',
'https://catalog.dvrpc.org/dataset/commute-mode',
'https://catalog.dvrpc.org/dataset/traffic-reliability',
'https://catalog.dvrpc.org/dataset/educational-attainment',
'https://catalog.dvrpc.org/dataset/greenhouse-gas-emissions',
'https://catalog.dvrpc.org/dataset/gross-domestic-product',
'https://catalog.dvrpc.org/dataset/housing-permits',
'https://catalog.dvrpc.org/dataset/housing-affordability',
'https://catalog.dvrpc.org/dataset/income',
'https://catalog.dvrpc.org/dataset/job-growth',
'https://catalog.dvrpc.org/dataset/labor-force',
'https://catalog.dvrpc.org/dataset/land-consumption',
'https://catalog.dvrpc.org/dataset/vehicle-miles-traveled',
'https://catalog.dvrpc.org/dataset/mortgage-lending',
'https://catalog.dvrpc.org/dataset/pavement-conditions',
'https://catalog.dvrpc.org/dataset/population-estimates',
'https://catalog.dvrpc.org/dataset/roadway-safety',
'https://catalog.dvrpc.org/dataset/transit-conditions',
'https://catalog.dvrpc.org/dataset/transit-ridership-ntd',
'https://catalog.dvrpc.org/dataset/water-quality'
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