while True:
    ret, frame = cap.read()

    blob = cv2.dnn.blobFromImage(frame, 1/255, (256, 256), swapRB=True, crop=True)
    net.setInput(blob)

    output_layer_names = net.getUnconnectedOutLayersNames()
    layer_outputs = net.forward(output_layer_names)
    boxes = []
    confidences = []
    class_ids = []

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

    cv2.imshow('Object Detection', frame)
    frame_count += 1
    if(time.time()-start_time>1):

        fps = frame_count /(time.time() - start_time)
        print(f"FPS: {fps:.2f}")
        start_time: float = time.time()
        frame_count = 0

    if cv2.waitKey(1) == ord('q'):
        break
