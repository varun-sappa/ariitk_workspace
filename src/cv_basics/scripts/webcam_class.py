#!/usr/bin/env python
import cv2
from threading import Thread
import time
import numpy as np


# Load YOLOv3 weights and configuration
path1 = r"/home/varun/rotors_ariitk_ws/src/cv_basics/src/yolov4-tiny.cfg"
path2 = r"/home/varun/rotors_ariitk_ws/src/cv_basics/src/yolov4-tiny.weights"
net = cv2.dnn.readNetFromDarknet(path1, path2)

# Load object classes
with open(r"/home/varun/rotors_ariitk_ws/src/cv_basics/src/coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]

# Set minimum confidence threshold and non-maximum suppression threshold
conf_threshold = 0.8
nms_threshold = 0.2

class Webcam():
    def __init__(self, id=0) -> None:
        self.stream_id = id
        self.vcap = cv2.VideoCapture(self.stream_id)
        if self.vcap.isOpened() is False :
            print("[Exiting]: Error accessing webcam stream.")
            exit(0)
        fps_input_stream = int(self.vcap.get(5)) # hardware fps
        print("FPS of input stream: {}".format(fps_input_stream))
        # reading a single frame from vcap stream for initializing 
        self.grabbed , self.frame = self.vcap.read()
        if self.grabbed is False :
            print('[Exiting] No more frames to read')
            exit(0)
        # self.stopped is initialized to False 
        self.stopped = True
        # thread instantiation  
        self.t = Thread(target=self.update, args=())
        self.t.daemon = True # daemon threads run in background 

    def start(self):
        self.stopped = False
        self.t.start()

    # method passed to thread to read next available frame  
    def update(self):
        while True :
            if self.stopped is True :
                break   
            self.grabbed , self.frame = self.vcap.read()

            if self.grabbed is False :
                print('[Exiting] No more frames to read')
                self.stopped = True
                break 
        self.vcap.release()
    # method to return latest read frame 
    def read(self):
        return self.frame
    # method to stop reading frames 
    def stop(self):
        self.stopped = True

def processing(net, frame):
    # Initialize lists for bounding boxes, confidences, and class IDs
    boxes = []
    confidences = []
    class_ids = []
    frame = frame
    output_layer_names = net.getUnconnectedOutLayersNames()
    layer_outputs = net.forward(output_layer_names)

    # Loop over each output layer
    for output in layer_outputs:
        # Loop over each detection in the output
        for detection in output:
            # Get class probabilities and class ID
            class_probabilities = detection[5:]
            class_id = np.argmax(class_probabilities)

            # Filter out low-confidence detections
            confidence = detection[4] * class_probabilities[class_id]
            if confidence > conf_threshold:
                # Get bounding box coordinates
                box = detection[0:4] * np.array(
                    [frame.shape[1], frame.shape[0], frame.shape[1], frame.shape[0]]
                )
                box = box.astype(int)

                # Add bounding box, confidence, and class ID to lists
                boxes.append(box.tolist())
                confidences.append(float(confidence))
                class_ids.append(class_id)

    # Apply non-maximum suppression to remove overlapping bounding boxes
    indices = cv2.dnn.NMSBoxes(boxes, confidences, conf_threshold, nms_threshold)
    return indices, boxes, confidences, class_ids, frame, classes

def show(indices, boxes, confidences, class_ids, frame, classes):
    if len(indices) > 0:
        for i in indices.flatten():
            x, y, w, h = boxes[i]
            label = classes[class_ids[i]]
            confidence = confidences[i]
            color = (0, 255, 0)
            cv2.rectangle(
                frame,
                (int(x - w / 2), int(y - h / 2)),
                (int(x + w / 2), int(y + h / 2)),
                color,
                2,
            )
            cv2.putText(
                frame,
                f"{label} {confidence:.2f}",
                (x, y - 5),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                color,
                2,
            )
            # Display frame
    return frame

if __name__ == "__main__":
    webcam_stream = Webcam(id=0) # 0 id for main camera
    webcam_stream.start()
    start_time = time.time()
    while True:
        if webcam_stream.stopped is True :
            break
        frame = webcam_stream.read()
        blob = cv2.dnn.blobFromImage(frame, 1 / 255, (256, 256), swapRB=True, crop=True)
        net.setInput(blob)
        indices, boxes, confidences, class_ids, frame, classes = processing(net, frame)
        frame = show(indices, boxes, confidences, class_ids, frame, classes)
        delay = 0.03 # delay value in seconds
        time.sleep(delay)
        
        # displaying frame 
        cv2.imshow('frame' , frame)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
    end = time.time()
    cv2.destroyAllWindows()