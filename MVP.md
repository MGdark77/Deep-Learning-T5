# Smart Parking System (SPS)
This is a deep learning project marks as the last project in the data science Bootcamp presented by SDAIA (Saudi Data and artificial intelligence authority).

In line with SDAIA's vision of smart cities and with the increase of population in Saudi Arabia, parking issues become common problem especially in the large and varied landmarks, work place, malls and so on.. 

Our Smart Parking System (SPS) will:
- Check if the parking is occupied or not.
- Double parking.
- Violations about parking in non parking spot.

We used 3 pretrained models:
-	Exception
-	Vgg16
-	Resnet50 which is the best one to fit the data.

<img width="1020" alt="Screen Shot 2022-01-12 at 8 12 07 PM" src="https://user-images.githubusercontent.com/93079431/149191308-c3620065-7529-49bc-a052-2489b6d5a5f1.png">

The figure above demonstrates the train and validate in Resnet50 ,the validate Loss got 0 score in the graph (A) while the it got 1 score in the accuracy graph (B).

And then we apply the CNN model on vertical perspective as shown in the picture down

<img width="993" alt="Screen Shot 2022-01-12 at 8 11 39 PM" src="https://user-images.githubusercontent.com/93079431/149191614-5b9461da-60ce-4e93-9482-0fb75967bc32.png">

The model detects every parking spot and checks whether it is free or occupied.
