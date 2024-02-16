import boto3

def lambda_handler (event,context):
    ec2 = boto3.client('ec2')

    #Get EBS Snapshots
    instance_response = ec2.describe_instances(Filters=[{'Name': 'instance-state-name','Values': ['running']}])
    active_instance_ids= set()

    response = ec2.describe_snapshots(OwnerIds=['self'])

    for reservation in instance_response['Reservations']:
        for instance in reservation['Instances']:
            active_instance_ids.add(instance['InstanceId'])
# Iterate through the snapshots and delete snapshots with no volume id,also delete volumes not attached to running instance
    for snapshot in response['Snapshots']:
        snapshot_id = snapshot['SnapshotId']
        volume_id = snapshot.get('VolumeId')

        if not volume_id:
            ec2.delete_snapshot(SnapshotId=snapshot_id)
            print(f"Deleted EBS snapshot {snapshot_id} successfully as it was not attached to any volume.")

        else:
            try:
                volume_response = ec2.describe_volumes(VolumeIds=[volume_id])
                if not volume_response['Volumes'][0]['Attachments']:
                    ec2.delete_snapshot(SnapshotId=snapshot_id)
                    print(f"Deleted Snapshot {snapshot_id} as it was taken from a volume not attached to any running instance")
            except  ec2.exceptions.ClientError as e:
                if e.response['Error']['Code'] == 'InvalidVolume.NotFound':
                    ec2.delete_snapshot(SnapshotId=snapshot_id)
                    print(f"Snapshot deleted as associated Volume not found ")


                




    