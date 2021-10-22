import cv2
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub

detector = hub.load("https://tfhub.dev/tensorflow/efficientdet/lite2/detection/1")
customDetector = tf.saved_model.load('customDetector/saved_model')

# ================== [ CONFIG ] ================

DETECTION_PRECISION = 0.5
DETECTION_CLASS = [1]
CUSTOM_DETECTOR_PRECISION = 0.3

WHEELCHAIR_COLOR = (204, 51, 000)
BABY_CARRIAGE_COLOR = (204, 51, 000)
CANE_COLOR = (204, 51, 000)
AMBULANCE_COLOR = (255, 51, 000)

WHEELCHAIR_TEXT = "Wheelchair"
BABY_CARRIAGE_TEXT = "Baby_carriage"
CANE_TEXT = "Cane"
AMBULANCE_TEXT = "Ambulance"

WHEELCHAIR_CLASS = 0
BABY_CARRIAGE_CLASS = 1
CANE_CLASS = 2
AMBULANCE_CLASS = 3

# Please Check :: LabelMap Index = Real Class Number - 1
LabelMap = [[WHEELCHAIR_TEXT, WHEELCHAIR_COLOR],
            [BABY_CARRIAGE_TEXT, BABY_CARRIAGE_COLOR],
            [CANE_TEXT, CANE_COLOR],
            [AMBULANCE_TEXT, AMBULANCE_COLOR]]


# ===============================================

# image = Pure Image that not drew anything
def Detector(image):
    rgb_tensor = cvImgToRGBTensor(image)
    boxes, scores, classes, num_detections = detector(rgb_tensor)

    pred_labels = classes.numpy().astype('int')[0]
    pred_boxes = boxes.numpy()[0].astype('int')
    pred_scores = scores.numpy()[0]

    pos_result = []

    # TODO: Remove Feature that return Img and make that Static Function(img, pos, custom_pos)...
    # loop throughout the detections and place a box around it
    for score, (ymin, xmin, ymax, xmax), label in zip(pred_scores, pred_boxes, pred_labels):
        if score < DETECTION_PRECISION or label not in DETECTION_CLASS:
            continue

        pos_result.append([int(xmin), int(ymax), int(xmax), int(ymin)])

    return pos_result


# image = Pure Image that not drew anything
def CustomDetector(image):
    rgb_tensor = cvImgToRGBTensor(image)
    output_dict = customDetector(rgb_tensor)

    num_detections = int(output_dict.pop('num_detections'))
    output_dict = {key: value[0, :num_detections].numpy()
                   for key, value in output_dict.items()}
    output_dict['num_detections'] = num_detections

    # detection_classes should be ints.
    output_dict['detection_classes'] = output_dict['detection_classes'].astype(np.int64)

    pred_labels = output_dict['detection_classes']
    pred_boxes = output_dict['detection_boxes']
    pred_scores = output_dict['detection_scores']

    h, w, c = image.shape

    pos_result = []
    for i in range(0, len(LabelMap)):
        pos_result.append([])

    # loop throughout the detections and place a box around it
    # TODO: Remove Feature that return Img and make that Static Function(img, pos, custom_pos)...
    for score, (ymin, xmin, ymax, xmax), label in zip(pred_scores, pred_boxes, pred_labels):
        if score < CUSTOM_DETECTOR_PRECISION:
            continue

        y_min = int(ymin * h)
        x_min = int(xmin * w)
        y_max = int(ymax * h)
        x_max = int(xmax * w)

        pos_result[label - 1].append([int(x_min), int(y_max), int(x_max), int(y_min)])

    return pos_result


def cvImgToRGBTensor(image):
    # Convert img to RGB
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Is optional but i recommend (float conversion and convert img to tensor image)
    rgb_tensor = tf.convert_to_tensor(rgb, dtype=tf.uint8)

    # Add dims to rgb_tensor
    rgb_tensor = tf.expand_dims(rgb_tensor, 0)

    return rgb_tensor