import os
import cv2
path='Images'
images=[]
for file in os.listdir(path):
    name,ext=os.path.splitext(file)
    if ext in ['.gif','.png','.jpg','.jpeg','.jfif']:
        fileName=path+'/'+file
        print(fileName)
        images.append(fileName)
print(len(images))
count=len(images)
frame=cv2.imread(images[0])
height,width,channels=frame.shape
size=(width,height)
print(size)
out= cv2.VideoWriter('Video of Friends.mp4', cv2.VideoWriter_fourcc(*'DIVX'),1,size)
for i in range(0,count-1):
    frame=cv2.imread(images[i])
    out.write(frame)
out.release()
print('done')