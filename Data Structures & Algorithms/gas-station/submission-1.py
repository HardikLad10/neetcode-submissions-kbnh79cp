"""
The problem hints that there is a circuit,(last idx proceeds to 0th idx)
If we check each idx as a start while making sure total_tank > 0 for the complete loop, it 
will take O(n)^2. 

A better solution is to *greedily* search for the start_station.

For this, we can maintain current_tank and total_tank, init stat_station at 0. 
As we iterate both arrays, we will maintain and update gain = gas - cost. Update both current_tank and total_tank with curr_gain. 

Then check if curr_tank < 0: 
> if yes, that means we cant complete a loop, so we reset start_station to i+1
> reset current_tank as well

We maintain the same total tank so that while we seach for the optimal start_station(there is at max 1)
we dont need to loop back to the idx, so after finishing the loop, we just need to check
if the total_tank >=0 -> this means we can complete the loop -> i.e. path already taken from idx 0 to curr start_station

Fin, return start_station

"""

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # init curr station
        start_station = 0

        curr_tank, total_tank = 0, 0
        
        # Loop for the len of any of the 2 arrays, since its given they are eq
        for i in range(len(gas)):
            # calc curr/local net_gain
            net_gain = gas[i] - cost[i]

            # update both tanks with the curr gain
            curr_tank += net_gain
            total_tank += net_gain

            if curr_tank < 0:
                # Since curr_tank is -ve, we cant complete loop, so shift start
                start_station = i+1
                # reset curr_tank
                curr_tank = 0
        
        # Since we know at max 1 sol exists, we can check the circuit logic at last and return start

        return start_station if total_tank >= 0 else -1

