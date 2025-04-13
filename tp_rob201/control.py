""" A set of robotics control functions """

import random
import numpy as np


def reactive_obst_avoid(lidar):
    """
    Simple obstacle avoidance
    lidar : placebot object with lidar data
    """
    laser_distances = lidar.get_sensor_values()
    laser_angles = lidar.get_ray_angles()

    # Afficher les résultats reçus des capteurs
    # print("Laser distances:", laser_distances)
    # print("Laser angles:", laser_angles * 180 / np.pi) # Convert radians to degrees

    idx = np.where(np.isclose(laser_angles, 0))[0]
    # print("Indices of angles close to 0°:", idx)
    distance_at_zero = laser_distances[idx[0]]

    # Vérification de la distance en face
    if distance_at_zero <= 20:
        # Obstacle détecté : arrête l'avance et tourne d'un angle aléatoire entre 0 et 1
        # command = {"forward": 0.5, "rotation": random.uniform(0, 1)}

        # Si la distance n'est pas acceptable, on commande une rotation de 0.5
        command = {"forward": 0.5, "rotation": 0.5}
    else:
        # Distance acceptable : avancer sans rotation
        command = {"forward": 0.5, "rotation": 0.0}
    
    return command

def potential_field_control(lidar, current_pose, goal_pose):
    """
    Control using potential field for goal reaching and obstacle avoidance
    lidar : placebot object with lidar data
    current_pose : [x, y, theta] nparray, current pose in odom or world frame
    goal_pose : [x, y, theta] nparray, target pose in odom or world frame
    Notes: As lidar and odom are local only data, goal and gradient will be defined either in
    robot (x,y) frame (centered on robot, x forward, y on left) or in odom (centered / aligned
    on initial pose, x forward, y on left)
    """
    # TODO for TP2

    command = {"forward": 0,
               "rotation": 0}

    return command
