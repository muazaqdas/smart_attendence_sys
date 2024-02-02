from cv2 import VideoCapture,imshow,waitKey,imwrite
cam_port = 0
cam = VideoCapture(cam_port)
# reading the input using the camera

inp = input('Enter person name: ')
# If image will detected without any error,
# show result
while(1): 
        result,image = cam.read()
        imshow(inp, image)
        if waitKey(0):
         imwrite(inp+".png", image)
         print("image taken")

# If captured image is corrupted, moving to else part
else:
	print("No image detected. Please! try again")
