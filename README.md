# aws-secretsmanager
Create AWS secret manager secret values from yaml file.

**Options**
external-secret.py -i <inputfile> -d <description> -n <external secret name> -r <region> -p <profile>

**Example**
$ python3 external-secret.py -i "example/secret-value-file.yaml" -n "/NEW/SECRETS/EXAMPLE" -r "us-west-2" -p "aws_dev" -d "example secret manager"


#ToDo
1. Updation of secret values.
2. Handle complex yaml value files.

