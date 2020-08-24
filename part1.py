import os 
os.system("clear")
print("\n\n###############################################")
print("Inside Part1 --> Clicking Photos")
print("##############################################\n\n")



import cv2
from time import sleep
cap = cv2.VideoCapture(0)
for i in range (5):
	while(cap.isOpened()):
		ret,img1 = cap.read()
		cv2.imwrite('test\img'+str(i)+'.png',img1)
		break
	sleep(1)
cap.release()
cv2.destroyAllWindows()
print("Part1 Complete")



