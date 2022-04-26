from skimage import color
hls = cv2.cvtColor(image, cv2.COLOR_RGB2HLS)
h_channel=hls[:,:,0]
l_channel=hls[:,:,1]
s_channel=hls[:,:,2]
canny_image = cv2.Canny(s_channel, 100, 200)
cropped_image = region_of_interest(canny_image,
                np.array([region_of_interest_vertices], np.int32),)
show_image(cropped_image,"S channel")
