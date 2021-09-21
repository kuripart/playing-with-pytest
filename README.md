# Mocking AWS Services in Python Tests

## Getting started with Moto

> [Check Git Repo](https://github.com/spulec/moto)

## Installing Dependencies

```bash
python3.7 -m pip install boto3 moto pytest
```

## Great tutorials here:

> [How To Mock AWS Services in Python Unit Tests](https://betterprogramming.pub/how-to-mock-aws-services-in-python-unit-tests-d6a8eacf725e) <br/>
> [How to test your AWS code using Moto and Pytest](https://www.learnaws.org/2020/12/01/test-aws-code/) <br/>
> [How to use SQS and SNS](https://medium.com/analytics-vidhya/how-to-use-aws-sns-and-sqs-528c485db051)


## Testing EC2, S3 and SQS

```bash
> pytest
================= test session starts ================
collected 6 items

test_ec2.py .                           [ 16%]
test_s3.py ...                          [ 66%]
test_sqs.py ..                          [100%]
```

## Testing SNS and SQS together

```bash
> pytest .\test_sns.py .\test_sns_and_sqs.py
================= test session starts ================
test_sns.py .                           [ 50%]
test_sns_and_sqs.py .                   [100%]
```
# Playing with `pytest-mock`


## Install

```bash
>  pip install pytest-mock
```

## Run tests

```bash
> pytest .\tests\
================= test session starts ================
collected 3 items

tests\test_demo_a.py .                  [ 33%] 
tests\test_demo_b.py .                  [ 66%] 
tests\test_demo_c.py .                  [100%] 
```