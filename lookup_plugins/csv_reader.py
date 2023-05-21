from ansible.errors import AnsibleError, AnsibleParserError
from ansible.plugins.lookup import LookupBase
import csv

class LookupModule(LookupBase):
    def run(self, terms, variables=None, **kwargs):
        csvfile = terms[0]
        delimiter = kwargs.get('delimiter', ',')
        result = []
        with open(csvfile, 'r') as file:
            csv_reader = csv.reader(file, delimiter=delimiter)
            for row in csv_reader:
                result.append(row)
        return result