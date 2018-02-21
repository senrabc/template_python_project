""" {{ cookiecutter.project_slug }}
Usage: example.py [options]
#time python dxster_v2.py -i ../temp/top100_nacc_dataset_0302217.csv -e ../docs/ealgdx_algorithm_table.csv
Options:
    -h, --help
    -c, --config=<file>  Path to the config file [TODO: MAKE THIS WORK]
    -i, --input_file=<file>  Path to CSV data file [ex. '/home/senrabc/mydata.csv']
    -o, --output_file=<file>  Path to output CSV file [ex. '~/myoutput.csv']
    -d, --debug  turn on all debug statements
"""
#CONSTANTS

CONFIG_FILE='./config.json'

# example of reading the config file


from docopt import docopt
import json



with open('config.json', 'r') as f:
    config = json.load(f)

secret_key = config['DEFAULT']['SECRET_KEY'] # 'secret-key-of-myapp'
ci_hook_url = config['CI']['HOOK_URL'] # 'web-hooking-url-from-ci-service'



if __name__ == '__main__':
  #do stuff here  
  args = docopt(__doc__)
