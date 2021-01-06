#!/usr/bin/env python3

from aws_cdk import core

from master_ex.master_ex_stack import MasterExStack


app = core.App()
MasterExStack(app, "master-ex")

app.synth()
