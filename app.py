#!/usr/bin/env python3

from aws_cdk import core
from master_ex.master_ex_stack import MasterExStack

env_prod = core.Environment(account="304962413949", region="us-east-1")
env_dev = core.Environment(account="304962413949", region="us-east-2")

props = {'namespace':'mycloudzone'}

app = core.App()

master_dev_stack = MasterExStack(app, f"{props['namespace']}-master-s3-dev", props, is_prod=False, env=env_dev)
master_prod_stack = MasterExStack(app, f"{props['namespace']}-master-s3-prod", props, is_prod=True, env=env_prod)

# Add a tag to all constructs in the stack

core.Tags.of(master_dev_stack).add("StackType", "Development")
core.Tags.of(master_prod_stack).add("StackType", "Production")

app.synth()
