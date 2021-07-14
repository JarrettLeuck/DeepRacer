def reward_function(params):
    #Input parameters
    all_wheels_on_track = params['all_wheels_on_track'] # boolean, flag to indicate if the agent is on the track
    x = params['x'] # float, agent's x-coordinate in meters
    y = params['y'] # float, agent's y-coordinate in meters
    closest_objects = params['closest_objects'] # [int, int], zero-based indices of the two closest objects to the agent's current position of (x, y).
    closest_waypoints = params['closest_waypoints'] # [int, int], indices of the two nearest waypoints.
    distance_from_center = params['distance_from_center'] # float, distance in meters from the track center
    is_crashed = params['is_crashed'] # Boolean, flag to indicate whether the agent has crashed.
    is_left_of_center = params['is_left_of_center'] # Boolean, Flag to indicate if the agent is on the left side to the track center or not.
    is_offtrack = params['is_offtrack'] # Boolean, flag to indicate whether the agent has gone off track.
    is_reversed = params['is_reversed'] # Boolean, flag to indicate if the agent is driving clockwise (True) or counter clockwise (False).
    heading = params['heading'] # float, agent's yaw in degrees
    progress = params['progress'] # float, percentage of track completed
    speed = params['speed'] # float, agent's speed in meters per second (m/s)
    steering = abs(params['steering_angle']) # float, agent's steering angle in degrees
    steps = params['steps']# int, number steps completed
    track_length = params['track_length']  # float,track length in meters.
    track_width = params['track_width'] # float, width of the track
    waypoints = params['waypoints'] # [(float, float), ], Calculate 3 markers that are at varying distances away from the center line

    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width
    reward = 1e-3
    distance_reward = 0.0
    if is_offtrack:
        reward *= -1
    else:
        if distance_from_center <= marker_1:
            distance_reward = 1
        elif distance_from_center <= marker_2:
            distance_reward = 0.5
        elif distance_from_center <= marker_3:
            distance_reward = 0.1
        else:
            reward = 1e-3  # likely crashed/ close to off track

    reward += (speed * .05) + (distance_reward * .25)

     # Steering penality threshold, change the number based on your action space setting
    ABS_STEERING_THRESHOLD = 15

    # Penalize reward if the agent is steering too much
    if steering > ABS_STEERING_THRESHOLD:
        reward *= 0.8
    return float(reward)
