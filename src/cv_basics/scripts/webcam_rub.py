#!/usr/bin/env python
import cv2
import numpy as np
import time
import threading
from threading import Thread
import queue


# Load YOLOv3 weights and configuration
path1 = r"/home/varun/rotors_ariitk_ws/src/cv_basics/src/yolov4.cfg"
path2 = r"/home/varun/rotors_ariitk_ws/src/cv_basics/src/yolov4.weights"
net = cv2.dnn.readNetFromDarknet(path1, path2)

# Load object classes
with open(r"/home/varun/rotors_ariitk_ws/src/cv_basics/src/coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]

# Set minimum confidence threshold and non-maximum suppression threshold
conf_threshold = 0.6
nms_threshold = 0.2

# Initialize webcam stream
cap = cv2.VideoCapture(0)


# while True:

#     # Read webcam frame
#     ret, frame = cap.read()

#     # Convert frame to blob and set input to YOLOv3 model
#     blob = cv2.dnn.blobFromImage(frame, 1/255, (256, 256), swapRB=True, crop=True)
#     net.setInput(blob)

#     # Get output layer names and forward pass through YOLOv3 model
#     output_layer_names = net.getUnconnectedOutLayersNames()
#     layer_outputs = net.forward(output_layer_names)

#     # Initialize lists for bounding boxes, confidences, and class IDs
#     boxes = []
#     confidences = []
#     class_ids = []

#     # Loop over each output layer
#     for output in layer_outputs:
#         # Loop over each detection in the output
#         for detection in output:
#             # Get class probabilities and class ID
#             class_probabilities = detection[5:]
#             class_id = np.argmax(class_probabilities)

#             # Filter out low-confidence detections
#             confidence = detection[4] * class_probabilities[class_id]
#             if confidence > conf_threshold:
#                 # Get bounding box coordinates
#                 box = detection[0:4] * np.array([frame.shape[1], frame.shape[0], frame.shape[1], frame.shape[0]])
#                 box = box.astype(int)

#                 # Add bounding box, confidence, and class ID to lists
#                 boxes.append(box.tolist())
#                 confidences.append(float(confidence))
#                 class_ids.append(class_id)

#     # Apply non-maximum suppression to remove overlapping bounding boxes
#     indices = cv2.dnn.NMSBoxes(boxes, confidences, conf_threshold, nms_threshold)

#     # Draw bounding boxes and labels on frame
#     if len(indices) > 0:
#         for i in indices.flatten():
#             x, y, w, h = boxes[i]
#             label = classes[class_ids[i]]
#             confidence = confidences[i]
#             color = (0, 255, 0)
#             cv2.rectangle(frame, (int(x-w/2), int(y-h/2)), (int(x+w/2), int(y+h/2)), color, 2)
#             cv2.putText(frame, f"{label} {confidence:.2f}", (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

#     # Display frame
#     cv2.imshow('Object Detection', frame)
#     frame_count += 1
#     if(time.time()-start_time>1):

#         fps = frame_count /(time.time() - start_time)
#         print(f"FPS: {fps:.2f}")
#         start_time: float = time.time()
#         frame_count = 0


#     # Break loop on 'q' key press
#     if cv2.waitKey(1) == ord('q'):
#         break




# ----------------------------- ################# ----------------------------- #

# def read_image(cap):
#     # Read webcam frame
#     ret, frame = cap.read()

#     # Convert frame to blob and set input to YOLOv3 model
#     blob = cv2.dnn.blobFromImage(frame, 1 / 255, (256, 256), swapRB=True, crop=True)
#     net.setInput(blob)
#     return net, frame


# def processing(net, frame):
#     # Initialize lists for bounding boxes, confidences, and class IDs
#     boxes = []
#     confidences = []
#     class_ids = []
#     frame = frame
#     output_layer_names = net.getUnconnectedOutLayersNames()
#     layer_outputs = net.forward(output_layer_names)

#     # Loop over each output layer
#     for output in layer_outputs:
#         # Loop over each detection in the output
#         for detection in output:
#             # Get class probabilities and class ID
#             class_probabilities = detection[5:]
#             class_id = np.argmax(class_probabilities)

#             # Filter out low-confidence detections
#             confidence = detection[4] * class_probabilities[class_id]
#             if confidence > conf_threshold:
#                 # Get bounding box coordinates
#                 box = detection[0:4] * np.array(
#                     [frame.shape[1], frame.shape[0], frame.shape[1], frame.shape[0]]
#                 )
#                 box = box.astype(int)

#                 # Add bounding box, confidence, and class ID to lists
#                 boxes.append(box.tolist())
#                 confidences.append(float(confidence))
#                 class_ids.append(class_id)

#     # Apply non-maximum suppression to remove overlapping bounding boxes
#     indices = cv2.dnn.NMSBoxes(boxes, confidences, conf_threshold, nms_threshold)
#     return indices, boxes, confidences, class_ids, frame, classes


# def show(indices, boxes, confidences, class_ids, frame, classes):
#     if len(indices) > 0:
#         for i in indices.flatten():
#             x, y, w, h = boxes[i]
#             label = classes[class_ids[i]]
#             confidence = confidences[i]
#             color = (0, 255, 0)
#             cv2.rectangle(
#                 frame,
#                 (int(x - w / 2), int(y - h / 2)),
#                 (int(x + w / 2), int(y + h / 2)),
#                 color,
#                 2,
#             )
#             cv2.putText(
#                 frame,
#                 f"{label} {confidence:.2f}",
#                 (x, y - 5),
#                 cv2.FONT_HERSHEY_SIMPLEX,
#                 0.5,
#                 color,
#                 2,
#             )
#             # Display frame
#     return frame


# def display(frame):
#     cv2.imshow("Object Detection", frame)
    


# # Create a shared queue to pass output of one function as input to the next function
# queue1 = queue.Queue()
# queue2 = queue.Queue()
# queue3 = queue.Queue()


# # Define the first thread to run the first function
# def thread1():
#     output1 = read_image(cap)
#     queue1.put(output1)


# # Define the second thread to run the second function
# def thread2():
#     input1 = queue1.get()
#     output2 = processing(*input1)
#     queue2.put(output2)


# # Define the third thread to run the third function
# def thread3():
#     input2 = queue2.get()
#     output3 = show(*input2)
#     queue3.put(output3)


# def thread4():
#     input3 = queue3.get()
#     output4 = display(input3)


# # Start the three threads

# t1 = threading.Thread(target=thread1)
# t2 = threading.Thread(target=thread2)
# t3 = threading.Thread(target=thread3)
# t4 = threading.Thread(target=thread4)

# t1.start()
# t2.start()
# t3.start()
# t4.start()

# while True:
#     t1.join()
#     t2.join()
#     t3.join()
#     t4.join()

# cap.release()
# cv2.destroyAllWindows()   


# ----------------------------- ################# ----------------------------- #


import multiprocessing as mp

def read(frame):
    blob = cv2.dnn.blobFromImage(frame, 1, (128, 128), swapRB=True)
    net.setInput(blob)
    output_layer_names = net.getUnconnectedOutLayersNames()
    layer_outputs = net.forward(output_layer_names)
    frame=frame
    return layer_outputs,frame

def processing(args):
    layer_outputs, frame = args
    boxes = []
    confidences = []
    class_ids = []
    frame=frame
    for output in layer_outputs:
        for detection in output:
            class_probabilities = detection[5:]
            class_id = np.argmax(class_probabilities)
            confidence = detection[4] * class_probabilities[class_id]
            if confidence > conf_threshold:
                box = detection[0:4] * np.array([frame.shape[1], frame.shape[0], frame.shape[1], frame.shape[0]])
                box = box.astype(int)
                boxes.append(box.tolist())
                confidences.append(float(confidence))
                class_ids.append(class_id)

    indices = cv2.dnn.NMSBoxes(boxes, confidences, conf_threshold, nms_threshold)

    if len(indices) > 0:
        for i in indices.flatten():
            x, y, w, h = boxes[i]
            label = classes[class_ids[i]]
            confidence = confidences[i]
            color = (0, 255, 0)
            cv2.rectangle(frame, (int(x-w/2), int(y-h/2)), (int(x+w/2), int(y+h/2)), color, 2)
            cv2.putText(frame, f"{label} {confidence:.2f}", (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    return frame

def process_frames(frames):
    with mp.Pool() as pool:
        results = pool.map(read, frames)
        results1=pool.map(processing,results)
    return results1

if __name__ == '__main__':
    fps_interval = 1  # update FPS every 5 seconds
    fps_frames = 0
    fps_start_time = time.time()
    while True:
        # Read multiple frames
        frames = []
        for i in range(60):
            ret, frame = cap.read()
            if ret:
                frames.append(frame)
        
        # Process frames in parallel
        results = process_frames(frames)
        
        # Display output frames
        for frame in results:
            cv2.imshow('Object Detection', frame)
            
        # Update FPS counter
        fps_frames += len(frames)
        if time.time() - fps_start_time > fps_interval:
            fps = fps_frames / (time.time() - fps_start_time)
            print(f'FPS: {fps:.2f}')
            fps_frames = 0
            fps_start_time = time.time()

        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# ----------------------------- ################# ----------------------------- 
