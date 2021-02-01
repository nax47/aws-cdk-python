#!/usr/bin/env python3

from aws_cdk import core

from workshop_python.workshop_python_stack import WorkshopPythonStack


app = core.App()
WorkshopPythonStack(app, "workshop-python", env={'region': 'us-east-1'})

app.synth()
