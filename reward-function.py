import math
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

    reward = 1e-3
    
    if is_offtrack:
        return reward
    
    # (x,y) of previous and next waypoints
    prev_waypoint = params['waypoints'][params['closest_waypoints'][0]]
    next_waypoint = params['waypoints'][params['closest_waypoints'][1]]

    y_dif = next_waypoint[1] - prev_waypoint[1]
    x_dif = next_waypoint[0] - prev_waypoint[0]

    track_direction = math.atan2(y_dif, x_dif) * math.pi/180

    # reward based on track_direction and car heading
    # track_direction - heading => want to be close to 0

    direction_diff = abs(track_direction - heading)

    if direction_diff > 180:
        direction_diff = 360 - direction_diff

    direction_reward = 1 - (direction_diff / 180.0)

    reward += (speed * .25) + (direction_reward)

     # Steering penality threshold, change the number based on your action space setting
    ABS_STEERING_THRESHOLD = 15

    # Penalize reward if the agent is steering too much
    if steering > ABS_STEERING_THRESHOLD:
        reward *= 0.8
    return float(reward)
