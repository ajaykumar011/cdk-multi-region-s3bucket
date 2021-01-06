import setuptools


with open("README.md") as fp:
    long_description = fp.read()


setuptools.setup(
    name="master_ex",
    version="0.0.1",

    description="An Multi Region-Multi Environment Bucket CDK Python app",
    long_description=This example creates separate buckets for Dev and Prod in multiple regions. Dev and Prod contains separate naming convenstion
    long_description_content_type="text/markdown",

    author="Ajay Kumar",

    package_dir={"": "master_ex"},
    packages=setuptools.find_packages(where="master_ex"),

    install_requires=[
        "aws-cdk.core==1.81.0",
        "aws-cdk.aws_ec2",
        "aws-cdk.aws_s3",
        "aws-cdk.aws_iam",
        "aws-cdk.aws_s3_deployment",
        ],

    python_requires=">=3.6",

    classifiers=[
        "Development Status :: 4 - Beta",

        "Intended Audience :: Developers",

        "License :: OSI Approved :: Apache Software License",

        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",

        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",

        "Typing :: Typed",
    ],
)
