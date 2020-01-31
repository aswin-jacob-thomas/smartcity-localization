# Advantages of lambda lambda functions
* Run code without provisioning servers
* Pay only for the compute time
* No need to maintain the server
* Can scale horizontally
* Can process data in parallel
* Support various languages like Javascript, java, python, c#

## First install all the dependencies in a folder and then zip the site-packages 
### [aws link describing the process](https://docs.aws.amazon.com/lambda/latest/dg/lambda-python-how-to-create-deployment-package.html#python-package-venv)

```
python3 -m venv v-env
source v-env/bin/activate
pip3 install requests utm sklearn 
deactivate
cd v-env/lib/python3.7/site-packages/
zip -r9 /home/aswin/Documents/SmartCity-Localization/lambda_function.zip .
cd /home/aswin/Documents/SmartCity-Localization/
zip -g lambda_function.zip lambda_function.py 
```

## Now upload the zip file to aws s3 bucket and copy the zip location to aws lambda
Current zip file is located at: [s3 link](https://import.s3.amazonaws.com/lambda.zip)



