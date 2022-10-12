#%% Imports
 
import cv2 as cv

#%% Camera
cap = cv.VideoCapture(0)
cv.namedWindow('Frame', cv.WINDOW_NORMAL)

# VideoWriter
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('Video gravado.avi', fourcc, 20.0, (640,  480))

# ROI 
p1, p2 = None, None
state = 0

# Called every time a mouse event happen
def on_mouse(event, x, y, flags, userdata):
    global state, p1, p2
    
    # Left click
    if event == cv.EVENT_LBUTTONUP:
        # Select first point
        if state == 0:
            p1 = (x,y)
            state += 1
        # Select second point
        elif state == 1:
            p2 = (x,y)
            state += 1
    # Right click (erase current ROI)
    if event == cv.EVENT_RBUTTONUP:
        p1, p2 = None, None
        state = 0

# Register the mouse callback
cv.setMouseCallback('Frame', on_mouse)

if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    if state > 1:
        cv.rectangle(frame, p1, p2, (255, 0, 0), 10)

    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # Flip horizontally
    frame = cv.flip(frame, 1)

    # Write frame
    out.write(frame)

    # Display the resulting frame
    cv.imshow('frame', frame)
    if cv.waitKey(1) == ord('q'):
        break

# Release capture
cap.release()
out.release()   
cv.destroyAllWindows()
# %%
