TT.py
####################################### PAIR OF SONGS
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        map={}
        n=len(time)
        count=0
        res=[]
        for i in range(n):
            comp = (60-(time[i]%60))%60
            if comp in map:
                count+=map[comp]
            if time[i]%60 in map:
                map[time[i]%60]+=1
            else:
                map[time[i]%60]=1

        return count

#################################################################################################################################
VALID PALINDROME

class Solution:
    def isPalindrome(self, s: str) -> bool:
        result=''
        for char in s:
            if char.lower().isalnum():
                result+=char.lower()
        print(result)

        if result==result[::-1]:
            return True
        else:
            return False
##################################################################################################################################

LARGEST NUMBER

class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        for index,number in enumerate(nums):
            nums[index]= str(number)

        def compare(n1,n2):
            if n1+n2> n2+n1:
                return -1
            else:
                return 1
        nums=sorted(nums,key=cmp_to_key(compare))

        return str(int(''.join(nums)))

##################################################################################################

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == '0':
                return
            grid[i][j] = '0'
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    ans += 1
                    dfs(i, j)

        return and

##################################################################################################################

MEETING ROOM 2
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        freerooms=[]
        intervals.sort()
        heapq.heappush(freerooms,intervals[0][1])

        for i in intervals[1:]:
            if i[0]>=freerooms[0]:
                heapq.heappop(freerooms)
            
            heapq.heappush(freerooms,i[1])



        return len(freerooms)


#####################################################################################################################################

STATS
from collections import defaultdict
import json


def deployment_number(log_data):
    total_number=0
    successful_deps=0
    failed_deps=0

    total_number=len(log_data)

    for data in log_data:
        try:
            deployment_status=data.get("status","")
            if deployment_status=="successful":
                successful_deps+=1
            else:
                failed_deps+=1
        except(KeyError):
            continue
    return successful_deps,failed_deps,total_number
def get_recenttimestamp(log_data):
    recent_timestamp=[]
    for data in log_data:
        try:
            timestamp=data.get("timestamp","")
 #           print(timestamp)
            recent_timestamp.append(timestamp)
        except(IndexError):
            continue
#    print(recent_timestamp)
    sorted_timestamp=sorted(recent_timestamp)

    return sorted_timestamp[-1]

def errorcode_number(log_data):
    nummap={}
    count=0
    for data in log_data:
        try:
            error_code=data.get("error_code","")
            if error_code in nummap:
                nummap[error_code]+=1
            else:
                nummap[error_code]=1
        except(KeyError):
            continue
    return nummap



def main():
    with open('log_output.json','r') as file:
        log_data=json.load(file)
    success,failure,total=deployment_number(log_data)
    print(f"successfull deployment: {success}, unsuccessful deployment: {failure}, total deployments: {total}")

 #   print(get_recenttimestamp(log_data))

    print(f"most recent time stamp is {get_recenttimestamp(log_data)}")
    
    nummapresult=errorcode_number(log_data)
    for codes in nummapresult:
        print(f"Code is {codes} and count is {nummapresult[codes]}")

if __name__=="__main__":
    main()
####################################################################################################################################

FUNCTION STATS
def read_log_file(log_file):
    # Initialize variables to store statistics
    total_lines = 0
    successful_requests = 0
    failed_requests = 0
    unique_ips = set()

    try:
        # Open the log file for reading
        with open(log_file, 'r') as file:
            # Iterate through each line in the file
            for line in file:
                total_lines += 1
                parts = line.split()  # Split the line into parts based on whitespace

                # Assuming the log file format is like:
                # <IP Address> - - [<Date>] "<Request Type> <Request URL> <HTTP Protocol>" <Status Code> <Response Size>
                # The status code is in parts[-2]

                if len(parts) >= 9:
                    status_code = int(parts[-2])
                    if 200 <= status_code < 400:
                        successful_requests += 1
                    else:
                        failed_requests += 1

                    # Extract the IP address from the log
                    ip_address = parts[0]
                    unique_ips.add(ip_address)

    except FileNotFoundError:
        print(f"Error: File '{log_file}' not found.")
        return

    # Print the statistics
    print("Basic Statistics:")
    print(f"Total lines in log file: {total_lines}")
    print(f"Successful requests: {successful_requests}")
    print(f"Failed requests: {failed_requests}")
    print(f"Unique IP addresses: {len(unique_ips)}")

# Example usage
read_log_file("example.log")


192.168.1.1 - - [25/Apr/2024:12:34:56 +0000] "GET /index.html HTTP/1.1" 200 1234
192.168.1.2 - - [25/Apr/2024:12:35:01 +0000] "POST /submit_form HTTP/1.1" 400 567
192.168.1.3 - - [25/Apr/2024:12:35:12 +0000] "GET /images/logo.png HTTP/1.1" 200 4567
192.168.1.1 - - [25/Apr/2024:12:36:02 +0000] "GET /about.html HTTP/1.1" 404 789
192.168.1.4 - - [25/Apr/2024:12:36:15 +0000] "GET /index.html HTTP/1.1" 200 2345

######################################################################################################################################################################

def find_lowest(log_data):
    min_latencies=float('inf')
    user_name=None
    lines=log_data.strip().split('\n')
    second_latest=[]

    
    for line in lines:
        status,user,direc,latency=line.strip().split(',')
        if status== '200':
            latency_current=int(latency[:-2])
            if latency_current<min_latencies:
                min_latencies=latency_current
                user_name=user
    return user_name





log_data = """
200,John,/home,60ms
200,Sarah,/log,13ms
500,Jack,/home,40ms
"""

print(find_lowest(log_data))
#############################################################################################################################################################

#def validateconfig(configstr)
    
def validator(configstr):
    configlist=configstr.split('|')
    configdict={}
    barcodes=set()

    for config in configlist:
       cleanconfig=config.strip()
       if not (cleanconfig.isalnum() and len(cleanconfig)==14):
        return "Invalid Configuration"
       ordinal=cleanconfig[0:4]
       barcode=cleanconfig[4::]
       if ordinal=='0000':
           return "Invalid Configuration"
       if ordinal in configdict:
           return "Invalid Configuration"
       
       if barcode in barcodes:
          return "Invalid Configuration"
       configdict[ordinal]=barcode
       barcodes.add(barcode)
       
    finallist=[]
    for finalvals in sorted(configdict):
       finallist.append(configdict[finalvals])
    return finallist
       
        
        
        
if __name__== '__main__':
    str='0002f7c22e7904 | 000176a3a4d214 | 000305d29f4a4b'
    str2="0002f7c22e7904 | 000176a3a4d214 | 000205d29f4a4b"
    print(validator(str))
    #validateconfig(str)
#########################################################################################################################################

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

        
