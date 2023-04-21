from aws_cdk import (
    Stack
)
from constructs import Construct


class MetricsReceiverCdkStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, prefix: str, environment: str, config: dict, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.prefix = prefix
        self.suffix = environment.capitalize()
        self.configuration = config
