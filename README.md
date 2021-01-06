
# Welcome to your CDK Python project!
# This is S3 Bucket Example considering Multi-Region, Multi-Enviornemt , Tagging Stack, Tagging Resources

The `cdk.json` file tells the CDK Toolkit how to execute your app.

This project is set up like a standard Python project.  The initialization
process also creates a virtualenv within this project, stored under the `.venv`
directory.  To create the virtualenv it assumes that there is a `python3`
(or `python` for Windows) executable in your path with access to the `venv`
package. If for any reason the automatic creation of the virtualenv fails,
you can create the virtualenv manually.

To manually create a virtualenv on MacOS and Linux:

```
$ python -m venv .venv
```
After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```
If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```
Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```
At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```
To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command.

## Useful commands


* `aws configure --profile prod`  # configuratin of AWSCLI for prod
* `aws configure --profile dev`   # configuratin of AWSCLI for Dev

 * `cdk ls`   list all stacks in the app
    Output:
    mycloudzone-master-s3-dev
    mycloudzone-master-s3-prod

 * `cdk synth mycloudzone-master-s3-dev`       emits the synthesized CloudFormation template
 * `cdk mycloudzone-master-s3-prod`

 * `cdk deploy mycloudzone-master-s3-dev`      deploy this stack to your default AWS account/region
 * `cdk deploy mycloudzone-master-s3-prod`   deploy this stack to your default AWS account/region

 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

Enjoy!
