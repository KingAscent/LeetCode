var findingUsersActiveMinutes = function(logs, k) {
    uam = Array(k).fill(0);

    // Store each user's activity into a map
    activity = new Map();
    logs.forEach((i) => {
        if(!activity.has(i[0]))
            activity.set(i[0], new Map());
        activity.get(i[0]).set(i[1]);
    })

    // Count the size of each user's activity, and store it
    // in the uam array
    activity.forEach((value) => {
        uam[value.size - 1]++;
    })

    // Return the uam array
    return uam;
};
