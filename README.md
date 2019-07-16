# aws-cognito-boilerplate
 
## Setup

### Installation

```bash
./setup.sh
```

### Amazon SES (Simple Email Service)

This particular setup utilizes SES as the email delivery service rather than the default AWS Cognito 

_**Step 1:**_ Add the email address you wish to use to AWS SES, and verify it

_**Step 2:**_ Click on the email you created in SES and replace the `Resource` value in the policy statement below with the ARN provided under `Identity ARN` (top of the page)

```json
{
    "Version": "2008-10-17",
    "Statement": [
        {
             "Effect": "Allow",
             "Principal": {
                "Service": "cognito-idp.amazonaws.com"
             },
             "Action": [
                 "ses:SendEmail",
                 "ses:SendRawEmail"
             ],
             "Resource": "arn:aws:ses:us-east-1:<AWS::AccountId>:identity/<Email>"
        }
    ]
}
```

_**Step 3:**_ On the same page, under the `Identity Policies` dropdown, select `Create Policy`, and click `Custom Policy`

![alt text](https://github.com/anigenero/aws-cognito-boilerplate/raw/master/images/idenity_policies.png "Identity Policies")

_**Step 4:**_ Copy and paste the policy statement from step 2 into the text field and click `Submit`

![alt text](https://github.com/anigenero/aws-cognito-boilerplate/raw/master/images/create_policy.png "Create Policy")


## Deploy

Run the following script, using the ARN from `Amazon SES (Simple Email Service)` in Setup to replace `email-arn`

```bash
npm run deploy -- --sesArn <email-arn>
```