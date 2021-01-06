from aws_cdk import core
from aws_cdk import aws_s3 as _s3
from aws_cdk import aws_s3_assets as _s3assets
from aws_cdk import aws_s3_deployment as s3deploy
import os


class MasterExStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, props, is_prod=None, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here 
        # is_prod check the value passed to the class
       
        if is_prod:
            bucket = _s3.Bucket(self, "myprodbucket", 
            bucket_name=f"{props['namespace'].lower()}-prodcontainer", 
            versioned=True,
            encryption=_s3.BucketEncryption.KMS,
            removal_policy=core.RemovalPolicy.RETAIN,
            auto_delete_objects=False
            )            
            
            # File asset direct uploaded to S3 during deployment
            s3deploy.BucketDeployment(self, "Delpoydiraszip", 
                                      sources=[s3deploy.Source.asset("./src-code")],
                                      destination_bucket=bucket,
                                      destination_key_prefix="code/python",
                                      prune=True)

            #asset = _s3assets.Asset(self, "SampleAsset", path=os.path.join(os.getcwd(), "README.md"))
            # core.CfnOutput(self, "S3BucketName", value=asset.s3_bucket_name)
            # core.CfnOutput(self, "S3ObjectKey", value=asset.s3_object_key)

            # Tagging the bucket
            core.Tags.of(bucket).add('Team', 'Prod-Team-bucket')

            #Output Section
            core.CfnOutput(self, "S3ProdBucketName",description="Prod S3 Bucket",value=bucket.bucket_name)
            core.CfnOutput(self, "S3ProdBucketARN",description="Prod S3 Bucket Arn",value=bucket.bucket_arn)

        else:
            bucket = _s3.Bucket(self, "mydevbucket", 
            bucket_name=f"{props['namespace'].lower()}-devcontainer",
            versioned=False,
            encryption=_s3.BucketEncryption.UNENCRYPTED,
            removal_policy=core.RemovalPolicy.DESTROY,
            auto_delete_objects=True
            )

            #Tagging the bucket
            core.Tags.of(bucket).add('Team', 'Dev-Team-bucket')

            s3deploy.BucketDeployment(self, "Delpoydiraszip", 
                                      sources=[s3deploy.Source.asset("./src-code")],
                                      destination_bucket=bucket,
                                      destination_key_prefix="code/python",
                                      prune=True)

            #Output Section
            core.CfnOutput(self, "S3DevBucketName", description="Prod S3 Bucket", value=bucket.bucket_name)
            core.CfnOutput(self, "S3DevBucketARN", description="Prod S3 Bucket Arn", value=bucket.bucket_arn)



