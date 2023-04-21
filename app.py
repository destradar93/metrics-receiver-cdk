#!/usr/bin/env python3
import aws_cdk as cdk

from metrics_receiver_cdk.metrics_receiver_cdk_stack import MetricsReceiverCdkStack


app = cdk.App()
prefix = app.node.try_get_context("prefix")
environments = app.node.try_get_context("environments")

for environment, configuration in environments.items():
    construct_id = f"{prefix}CdkStack{environment.capitalize()}"
    MetricsReceiverCdkStack(app, construct_id, prefix=prefix, environment=environment, config=configuration)

app.synth()
