def get_car_position(x_min,w):
    xm_per_pix=3.7/720
    if x_min is not None:
        car_position = w/2
        lane_center_position = (x_min+(700/2))
        center_dist = (car_position - lane_center_position) * xm_per_pix

    return center_dist


def get_direction(center_dist):
      direction = ''
      if center_dist > 0:
          direction = 'right'
      elif center_dist < 0:
          direction = 'left'
      return direction
