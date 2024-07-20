import json
def deploymentresult(deployment):
    success=failed=error=0

    deploymentlist=json.loads(deployment)

    for nums in deploymentlist:
        depstring=nums.get('deployment_id')
        statusstring=nums.get('status')
        if statusstring=='Success' and depstring.startswith('d-') and depstring[2:].islower() and depstring[2:].isalnum() :
            success+=1
        elif statusstring=='Fail' and depstring.startswith('d-') and depstring[2:].islower() and depstring[2:].isalnum():
            failed+=1
        else:
            error+=1
    finallist=[success,failed,error]
    return finallist

if __name__=='__main__':
    deployment='''[
    {"deployment_id": "d-123456abcd", "status": "Success"},
    {"deployment_id": "d-098765efgh", "status": "Fail"},
    {"deployment_id": "d-098765efgh", "status": "Success"}
    ]'''

    print(deploymentresult(deployment))