def process_dist(proc_traj, intervals, T):
"""- 'proc_traj' - list of trajectories of some define processes from pystoch.
   - 'intervals' - list of sets of the following type: ('lower border', 'higher border', 'specific time'). borders for trajectories.
   - 'T' - the duration of the process.

"""
    dt = T/len(proc_traj[0])
    counter = 0

    for traj in proc_traj:
        Flag = True
        for inter in intervals:
            if not (traj[int(inter[2]//dt)] > inter[0] and traj[int(inter[2]//dt)] < inter[1]):
                Flag = False
                break
        if Flag == True:
            counter+=1

    return counter/len(proc_traj)
