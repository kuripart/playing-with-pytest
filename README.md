# Mocking AWS Services in Python Tests

## Getting started with Moto

> [Check Git Repo](https://github.com/spulec/moto)

## Installing Dependencies

```bash
python3.7 -m pip install boto3 moto pytest
```

## Great tutorials here:

> [How To Mock AWS Services in Python Unit Tests](https://betterprogramming.pub/how-to-mock-aws-services-in-python-unit-tests-d6a8eacf725e) <br/>
> [How to test your AWS code using Moto and Pytest](https://www.learnaws.org/2020/12/01/test-aws-code/)


## Running tests in this repo

```bash
> pytest
================= test session starts ================
collected 6 items

test_ec2.py .                           [ 16%]
test_s3.py ...                          [ 66%]
test_sqs.py ..                          [100%]
```
