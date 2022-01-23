# Smart-Parking-system-deep_learning-

Our goal in this project is to serve The General Saudi Department of Traffic from a side and the
civil from the other side by building a smart parcking system that will capture the parcking lot frames from videos and do object detection to determine:

• Occupied parking.

• Available parking.

• Disabled parking.

• Parked in wrong space.

• One in two parking.

# FIRST APPROACH: Object detection with (Drone)

The Dataset: the Dataset has been collected from captured frames of videos with more  than 12 thousand images with different angels of cam
• The Annotation: in this approach Roboflow application was used for Annotation labeles as follows:

  ▪ Empty-space
  
  ▪ Occupied-space
  
  ▪ Wrong-parking
  
• The used model: in this approach the used model is YOLOv5 (last version of yolo) which is has been released within the last 6 months, the model got trained on
yolov5x.pt(wight) and epochs 5000 and batch size 16 .

• The output of model: the output of the model shows Number of spaces of the occupied parking spaces and available space using object detection to achieve this goal.

![image](https://user-images.githubusercontent.com/78117752/150651710-b116af34-5749-43ed-9984-d5dc1a20e656.png)

to use this approach use this file 'video_car_Drone_copy_5000_epochs.ipynb'
the output weight of this model is drone_je.pt 

# Second APPROACH: Real time detection and object tracking

• The Dataset: the Dataset has been collected from captured frames of videos, Since we don’t have dataset of double parking, we took a tracking object as an alternative approach.

• The used model: in this approach the used model is resnet50 with algorithms includes MOG and KNN which implemented with OpenCV.

• The output of model: the output of the model shows Number of spaces of the occupied parking spaces and available space using object detection to achieve this goal,also the model shows the wrong parking’s in different types, also the model calculate thetime for every detected car.

The figure below represents how the model will be processed:

![image](https://user-images.githubusercontent.com/78117752/150651917-ef81a6c5-dd58-467c-a383-61174f3a3f15.png)



![car detection and tracking](https://user-images.githubusercontent.com/78117752/150652315-af159824-365d-41af-b23f-5216053e5c6f.png)


to use this approach 'car_detection_final.py'

# Third APPROACH: Combining two models. 

Combining two models Resnet50 and YOLOv5, due to the fact that yolov5 works better with 1500 image for each class.

• The Dataset: The Dataset has been collected from captured frames of videos with more than 12 thousand images with different angels of cam

• The used model: in this approach the used model is YOLOv5 since it is the best model for detection and tracking object and Resnet50 is the best in classification we made combination of two of these models which enhanced the accuracy and speed up the model in processing.

• The output of model: the output of the model shows Number of spaces of the occupied parking spaces and available space using object detection to achieve this goal, also the model shows the wrong parking’s in different types, also the model calculate the time for every detected car. 

The figure below represents how the model will be processed:

![image](https://user-images.githubusercontent.com/78117752/150652529-077563b0-a562-4bff-9074-7565486834b3.png)

to use this approach use these files :

1-identify_parking_spots last1.ipynb.zip

2-The model-last1.ipynb

3-detect.py

4-object_detection_yolov5.py

# Referances

github /ultralytics

Roboflow

# done by 

- Jamilah Alharbi  -   Mohammed almalki 
- Ghliah Maher     -   Yahya Alyoubi
- Ghadeer Alghamdi -  Mohammeh Alajmi
