def write_on_image (img,x_min) :
  font = cv2.FONT_HERSHEY_COMPLEX_SMALL
  text1=get_car_position(x_min,1280)
  direction=get_direction(text1)
  text=abs(get_car_position(x_min,1280))
  text = '{:04.3f}'.format(text) + 'm ' + direction + ' of center'
  edited_photo=cv2.putText(img, text,(40,70), cv2.FONT_HERSHEY_COMPLEX_SMALL,1.5,(255,255,255),2,cv2.LINE_AA)
  return edited_photo;
ex=write_on_image (last_image,x_min)
show_image(ex)
