
# CDK Application for Receiving Data Metrics from Device

This is a CDK (Cloud Development Kit) application written in Python that is designed to receive data 
metrics sent from a device. The application contains an SQS (Simple Queue Service) queue that receives messages 
from the device, a Lambda function that is triggered by messages in the SQS queue, and a DynamoDB table that 
stores the payload coming from the device using the device's unique identifier as the reference.

## What is the CDK?
The AWS Cloud Development Kit (CDK) is an open source software development framework 
to define cloud infrastructure in code and provision it through AWS CloudFormation. 
It provides a high-level object-oriented abstraction on top of AWS CloudFormation that
makes it easier to provision and manage AWS resources.

## Prerequisites
Before you can use this CDK application, you will need to have the following:

* AWS Account
* AWS CLI installed and configured
* Python 3.7 or later
* Node.js 18.16.0 or later
* AWS CDK installed (version 2.75.0 or later)

## Getting Started
1. Clone this repository to your local machine.
2. Navigate to the root directory of the project.
3. Create virtual environment ``` python3 -m venv .venv```
4. Activate virtual environment. 
* Linux: ```source .venv/bin/activate``` 
* Windows: ```.venv\Scripts\activate```
5. Install the required dependencies ``` pip install -r requirements.txt ```
6. Synthesize the CloudFormation template for this code ``` cdk synth ```
7. Deploy the code ``` cdk deploy <stack_name> ```

## Resources Created
This CDK application creates the following resources in your AWS account:

* An SQS queue that receives messages from the device.
* A Lambda function that is triggered by messages in the SQS queue.
* A DynamoDB table that stores the payload coming from the device using the device unique identifier as the reference.

All resources have a common prefix and environment suffix assigned to them, and all resources have names defined.

## Cleanup
To delete all the resources created by this CDK application, run ```cdk destroy <stack_name> ``` in the root directory 
of the project. This will delete the CloudFormation stack and all resources associated with it. Don't forget to 
also delete the virtual environment by running deactivate in your terminal.