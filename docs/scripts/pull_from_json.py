"""Script to pull from the hosted JSON and populate collection information."""
import os
import requests

# URL with the hosted JSON
url = 'https://climateknowledgeportal.worldbank.org/themes/cckp/data/catalog/tree_all.json'

# read json from url
r = requests.get(url)
data = r.json()

# plan to make an md file for each top level dictionary
for collection in data.keys():
    # delete file if it exists
    if os.path.exists('docs/collections/' + collection + '.md'):
        os.remove('docs/collections/' + collection + '.md')
    # create file for writing
    f = open('docs/collections/' + collection + '.md', 'w+')
    # write to file
    # write collection
    f.write('# ' + collection + ' File Structure\n \n')
    # second-level of dictionary are Type
    for _type in data[collection].keys():
        # write Type
        f.write('## Type: ' + _type + '\n \n')
        # third-level of dictionary are Variables
        for variables in data[collection][_type].keys():
            # write variable
            f.write('### Variable: ' + variables + '\n \n')
            # fourth-level of dictionary are Product
            for product in data[collection][_type][variables].keys():
                # write product
                f.write('  - Product: ' + product + '\n')
                # fifth-level of dictionary are Aggregation
                for aggregation in data[collection][_type][variables][product].keys():
                    # write aggregation
                    f.write('    - Aggregation: ' + aggregation + '\n')
                    # sixth-level of dictionary are Time Interval
                    for time_interval in data[collection][_type][variables][product][aggregation].keys():
                        # write time interval
                        f.write('      - Time Interval: ' + time_interval + '\n')
                        # seventh-level of dictionary are Percentiles
                        for percentile in data[collection][_type][variables][product][aggregation][time_interval].keys():
                            # write percentile
                            f.write('        - Percentile: ' + percentile + '\n')
                            # eighth-level of dictionary are Scenario
                            for scenario in data[collection][_type][variables][product][aggregation][time_interval][percentile].keys():
                                # write scenario
                                f.write('          - Scenario: ' + scenario + '\n')
                                # ninth-level of dictionary are Model
                                for model in data[collection][_type][variables][product][aggregation][time_interval][percentile][scenario].keys():
                                    # write model
                                    f.write('            - Model: ' + model + '\n')
                                    # tenth-level of dictionary are values
                                    for values in data[collection][_type][variables][product][aggregation][time_interval][percentile][scenario][model].keys():
                                        # write values
                                        f.write('              - ' + values + '\n \n')
