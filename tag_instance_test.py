import boto3

def tag_instance(instance_id, region, key, value, profile_name="auto-tagger-dev"):
    # Create a session bound to the specific profile you configured with aws configure
    session = boto3.Session(profile_name=profile_name, region_name=region)
    ec2 = session.client('ec2')

    ec2.create_tags(
        Resources=[instance_id],
        Tags=[{'Key': key, 'Value': value}]
    )

    print(f"✅ Tagged {instance_id} with {key}={value}")

if __name__ == "__main__":
    # IMPORTANT: replace this with a *real* instance ID from your account
    test_instance_id = "i-0123456789abcdef0"
    tag_instance(
        instance_id=test_instance_id,
        region="us-west-2",
        key="Environment",
        value="Dev",
        profile_name="auto-tagger-dev"
    )
