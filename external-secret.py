#!/usr/bin/python3

import yaml
import json
import subprocess
import sys, getopt

def main(argv):
    inputfile = ''
    description = "Create Secret Manager"
    secret_name = ''
    region = 'us-east-1'
    profile = 'default'
    if (len(sys.argv) <= 1 ) or (len(sys.argv) > 11):
        print('external-secret.py -i <inputfile> -d <description> -n <external secret name> -r <region> -p <profile> ')
        sys.exit()
    try:
        opts, args = getopt.getopt(argv,"hi:d:n:r:p:",["ifile=","name=","description=","region=","profile="])
        print(opts)
    except getopt.GetoptError:
        print('external-secret.py -i <inputfile> -d <description> -n <external secret name> -r <region> -p <profile> ')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('external-secret.py -i <inputfile> -d <description> -n <external secret name> -r <region> -p <profile> ')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-d", "--description"):
            description = arg
        elif opt in ("-n", "--name"):
            secret_name = arg
        elif opt in ("-r", "--region"):
            region = arg
        elif opt in ("-p", "--profile"):
            profile = arg
        else:
            print("Else")
            print('external-secret.py -i <inputfile> -d <description> -n <external secret name> -r <region> -p <profile> ')
            sys.exit()
    #print('Secret value file is ', inputfile)
    #print('External secret is %s. Desciption passed is %s. Region selected is %s. Profile passed is %s.' % (secret_name,description,region,profile))
    with open(inputfile) as yaml_file:
        data = yaml.safe_load(yaml_file)
    secrets = {}
    for key,values  in data.items():
        secrets.update(values)
    cmd = ['aws', 'secretsmanager', 'create-secret', '--region', region, '--profile', profile, '--description', description, '--name', secret_name, '--secret-string', json.dumps(secrets)]
    result  = subprocess.run(cmd)
    print(result)

if __name__ == "__main__":
   main(sys.argv[1:])

