import boto3
import argparse

def list_untagged_instances(region, profile):
    """
    Lists EC2 instances that have no tags or empty tag lists.
    """

    # Create a session using your named AWS CLI profile
    session = boto3.Session(profile_name=profile, region_name=region)
    ec2 = session.client("ec2")

    print(f"\nScanning region {region} for untagged EC2 instances...\n")

    response = ec2.describe_instances()
    untagged = []

    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            instance_id = instance["InstanceId"]
            tags = instance.get("Tags", [])
            if not tags:  # Empty or None
                untagged.append(instance_id)

    if untagged:
        print(f"Found {len(untagged)} untagged instances:\n")
        for instance_id in untagged:
            print(f"  - {instance_id}")
    else:
        print("✅ All instances in this region are tagged.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="List untagged EC2 instances in a given AWS region."
    )
    parser.add_argument("--region", required=True, help="AWS region (e.g., us-west-2)")
    parser.add_argument("--profile", default="auto-tagger-dev", help="AWS CLI profile name")
    args = parser.parse_args()

    list_untagged_instances(args.region, args.profile)
