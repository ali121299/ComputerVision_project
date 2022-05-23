#input video line 113,input video line 114
import cv2
from matplotlib import pyplot as plt
import numpy as np
import pylab
from google.colab.patches import cv2_imshow
from moviepy.editor import VideoFileClip
%matplotlib inline

def region_of_interest(img, vertices):
    mask = np.zeros_like(img)
    #channel_count = img.shape[2]
    match_mask_color = 255
    cv2.fillPoly(mask, vertices, match_mask_color)
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image


def drow_the_lines(img, lines):
    img = np.copy(img)
    blank_image = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)

    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(blank_image, (x1,y1), (x2,y2), (0, 255, 0), thickness=10)

    img = cv2.addWeighted(img, 1, blank_image, 1, 0.0)
    return img, blank_image


def paint (img,vertices):
  mask = np.zeros_like(img)
  channel_count = img.shape[2]
  cv2.fillPoly(mask, vertices, color=(0, 255, 255))
  return mask

 def get_car_position(x_min=285,w):
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


def write_on_image (img,x_min) :
    font = cv2.FONT_HERSHEY_COMPLEX_SMALL
    text1=get_car_position(x_min,1280)
    direction=get_direction(text1)
    text=abs(get_car_position(x_min,1280))
    text = '{:04.3f}'.format(text) + 'm ' + direction + ' of center'
    edited_photo=cv2.putText(img, text,(40,70), cv2.FONT_HERSHEY_COMPLEX_SMALL,1.5,(255,255,255),2,cv2.LINE_AA)
    return edited_photo;

def process(image):
      print(image.shape)
      region_of_interest_vertices = [
        (200, 665),
        (620,410),
        (1130, 665)
      ]
      hls = cv2.cvtColor(image, cv2.COLOR_RGB2HLS)
      h_channel=hls[:,:,0]
      l_channel=hls[:,:,1]
      s_channel=hls[:,:,2]
      canny_image = cv2.Canny(s_channel, 100, 200)
      cropped_image = region_of_interest(canny_image,
                    np.array([region_of_interest_vertices], np.int32))

      lines = cv2.HoughLinesP(cropped_image,
                            rho=6,
                            theta=np.pi/180,
                            threshold=160,
                            lines=np.array([]),
                            minLineLength=40,
                            maxLineGap=25)
     try :
        image_with_lines , mask = drow_the_lines(image, lines)
        c = (0,255,0)
        indices = np.where(np.all(mask == c, axis=-1))
        x_min=np.min(indices[1])
        if x_min<285 or x_min is None :
          x_min=285
        y_max=np.max(indices[0])
        x_topleft=x_min+310
        y_min=np.min(indices[0])
        if y_min<450 or y_min is None :
          y_min=450
      except:
          image_with_lines=image
          x_min=285
          x_topleft=660
          y_min=500
          y_max=670
      vertices_paint = [
        (x_min,y_max),
        (x_topleft,y_min),
        (x_topleft+45,y_min),
        (x_min+720, y_max)
      ]
      yellow_rec=paint(image,np.array([vertices_paint], np.int32))
      last_image = cv2.addWeighted(image_with_lines, 0.8, yellow_rec, 1, 0.0)
      last_edited=write_on_image (last_image,x_min)
      return last_edited

first_frame = 1
white_output = '/content/output_video.mp4'
clip1 = VideoFileClip("/content/input_video.mp4")
white_clip = clip1.fl_image(process)
white_clip.write_videofile(white_output, audio=False)
