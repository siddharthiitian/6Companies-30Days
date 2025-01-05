def JobSequencing(id, deadline, profit):
    # Combine job details into a list of tuples and sort by profit (descending)
    jobs = sorted(zip(id, deadline, profit), key=lambda x: x[2], reverse=True)
    
    # Find the maximum deadline to determine the timeline of slots
    max_deadline = max(deadline)
    
    # Initialize a hashmap (dictionary) for storing jobs in their respective slots
    slot_map = {}
    
    for job_id, job_deadline, job_profit in jobs:
        # Check from the job's deadline to the earliest possible slot
        for time in range(job_deadline, 0, -1):
            if time not in slot_map:  # If the slot is free
                slot_map[time] = (job_id, job_profit)  # Assign the job to the slot
                break  # Move to the next job
    
    # Extract the scheduled jobs and calculate total profit
    scheduled_jobs = [slot_map[time][0] for time in sorted(slot_map.keys())]
    total_profit = sum(slot_map[time][1] for time in slot_map)
    
    return scheduled_jobs, total_profit


# Example usage
job_ids = [1, 2, 3, 4,5]
deadlines = [2, 1, 2, 1,1]
profits = [100, 19, 27, 25, 15]

scheduled_jobs, max_profit = JobSequencing(job_ids, deadlines, profits)
print("Scheduled Jobs:", scheduled_jobs)
print("Maximum Profit:", max_profit)
