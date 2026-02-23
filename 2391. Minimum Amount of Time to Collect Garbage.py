class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        # 1. Total picking time is just the total number of characters
        total_time = sum(len(g) for g in garbage)
        
        # 2. Track the last house index for each type
        last_m = last_g = last_p = 0
        for i, house in enumerate(garbage):
            if 'M' in house: last_m = i
            if 'G' in house: last_g = i
            if 'P' in house: last_p = i
            
        # 3. Create a prefix sum for travel times to quickly get distance to any house
        # travel_pref[i] = travel time from house 0 to house i
        travel_pref = [0] * (len(garbage))
        for i in range(len(travel)):
            travel_pref[i + 1] = travel_pref[i] + travel[i]
            
        # 4. Add travel times for each truck
        total_time += travel_pref[last_m]
        total_time += travel_pref[last_g]
        total_time += travel_pref[last_p]
        
        return total_time