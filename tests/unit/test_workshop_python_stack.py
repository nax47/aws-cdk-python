import json
import pytest

from aws_cdk import core
from workshop-python.workshop_python_stack import WorkshopPythonStack


def get_template():
    app = core.App()
    WorkshopPythonStack(app, "workshop-python")
    return json.dumps(app.synth().get_stack("workshop-python").template)


def test_sqs_queue_created():
    assert("AWS::SQS::Queue" in get_template())


def test_sns_topic_created():
    assert("AWS::SNS::Topic" in get_template())
