from aws_cdk import (
    Stack,
    Duration,
    aws_sqs as sqs,
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
