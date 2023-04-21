from aws_cdk import (
    Stack,
    Duration,
    aws_sqs as sqs,
    aws_logs as logs,
    aws_iam as iam,
    aws_lambda as _lambda_,
    aws_dynamodb as dynamodb,
    aws_lambda_event_sources as lambda_event_sources
)
from constructs import Construct


class MetricsReceiverCdkStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, prefix: str, environment: str, config: dict,
                 **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.prefix = prefix
        self.suffix = environment.capitalize()
        self.configuration = config

        queue = sqs.Queue(self, f"{self.prefix}Queue{self.suffix}",
                          queue_name=f"{self.prefix}Queue{self.suffix}",
                          visibility_timeout=Duration.minutes(15))

        dynamo_table = dynamodb.Table(
            self, f"{self.prefix}Table{self.suffix}",
            table_name=f"{self.prefix}Table{self.suffix}",
            partition_key=dynamodb.Attribute(
                name='deviceId',
                type=dynamodb.AttributeType.STRING,
            ),
            sort_key=dynamodb.Attribute(
                name='timestamp',
                type=dynamodb.AttributeType.NUMBER,
            ),
            billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST,
            deletion_protection=True
        )

        lambda_ = _lambda_.Function(self, f"{self.prefix}Function{self.suffix}",
                                    function_name=f"{self.prefix}Function{self.suffix}",
                                    runtime=_lambda_.Runtime.PYTHON_3_9,
                                    handler="index.lambda_handler",
                                    timeout=Duration.minutes(1),
                                    code=_lambda_.Code.from_asset("./lambdas"),
                                    reserved_concurrent_executions=10,
                                    log_retention=logs.RetentionDays.ONE_WEEK,
                                    environment={
                                        "DYNAMODB_TABLE": dynamo_table.table_name
                                    })

        lambda_.add_event_source(lambda_event_sources.SqsEventSource(
            queue,
            batch_size=20,
            max_concurrency=10,
            max_batching_window=Duration.minutes(5)
        ))

        lambda_.add_to_role_policy(
            statement=iam.PolicyStatement(
                actions=[
                    'dynamodb:PutItem',
                ],
                resources=[
                    dynamo_table.table_arn,
                ],
            ),
        )
