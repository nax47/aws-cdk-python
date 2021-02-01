from aws_cdk import (
    aws_iam as iam,
    aws_sqs as sqs,
    aws_sns as sns,
    aws_s3 as s3,
    aws_lambda as lamb,
    aws_sns_subscriptions as subs,
    aws_apigateway as api,
    core
)


class WorkshopPythonStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

    queue = sqs.Queue(
            self, "PycdkworkshopQueue",
            visibility_timeout=core.Duration.seconds(300),
        )

        topic = sns.Topic(
            self, "PycdkworkshopTopic"
        )
        
        bucket = s3.Bucket(
            self, 's3cdkbucket',
            versioned=True
        )
        
        lambdafunction = lamb.Function(
            self, 'lambdafunction',
            runtime=_lambda.Runtime.PYTHON_3_8,
            handler='hello.handler',
            code=_lambda.Code.from_asset(path='lambdacode')
        )
                            
        lambapi = api.LambdaRestApi(
            self, 'restapi',
            handler=lambdafunction
        )                    

        topic.add_subscription(subs.SqsSubscription(queue))
