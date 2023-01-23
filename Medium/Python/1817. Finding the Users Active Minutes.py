class Solution(object):
    def findingUsersActiveMinutes(self, logs, k):
        uam = [0] * k

        # Store each user's activity into a dict
        activity = {}
        for id, time in logs:
            if id not in activity:
                activity[id] = set()
            activity[id].add(time)
        
        # Count the size of each user's activity, and store it
        # in the uam list
        for i in activity:
            uam[len(activity[i]) - 1] += 1
        
        # Return the uam list
        return uam
