c = (0,255,0)
indices = np.where(np.all(mask == c, axis=-1))
x_min=np.min(indices[1])
x_max=np.max(indices[1])
y_max=np.max(indices[0])
x_topleft=x_min+280
y_min=np.min(indices[0])
if y_min<450 :
  y_min=450

def paint (img,vertices):
  mask = np.zeros_like(img)
  channel_count = img.shape[2]
  cv2.fillPoly(mask, vertices, color=(0, 255, 0))
  return mask

vertices_paint = [
    (x_min,y_max),
    (x_topleft,y_min),
    (x_topleft+45,y_min),
    (x_min+720, y_max)
  ]

mask = np.zeros_like(image)
channel_count = image.shape[2]
cv2.fillPoly(mask,  np.array([vertices_paint], np.int32), color=(255, 255, 0))
plt.imshow(mask)

last_image = cv2.addWeighted(image_with_lines, 0.8, mask, 1, 0.0)
