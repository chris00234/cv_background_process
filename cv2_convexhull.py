import cv2

capture = cv2.VideoCapture(0)

while True:
    ret, frame = capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (7, 7), 0)
    _,thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
    
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    
    for contour in contours:
        # Compute the convex hull of the contour
        hull = cv2.convexHull(contour)

        # Draw the convex hull on the original image
        cv2.drawContours(frame, [hull], -1, (0, 255, 0), 2)
    
    # cv2.drawContours(frame, contours, -1, (150,255,0), 2)
    
    
    cv2.imshow('video', frame)
    if (cv2.waitKey(1) & 0xFF == ord('q')):
        break