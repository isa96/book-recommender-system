# Dataset

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Download the dataset on [Kaggle -  Book Recommendation Dataset](https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset) 

![image](https://user-images.githubusercontent.com/91602612/206841314-eaefe4e1-2fa0-4e2a-b6ce-bb7b70bb6d2f.png)

# Dataset Info

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; There are several csv on that dataset:
1. Book's lists dataset
2. Book's users dataset
3. Book's Ratings dataset

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Total of the dataset if you merge them is **1.149.780 rows and 12 columns** but there are also several missing values and several duplicate book's title, therefore I handle it by remove them and I got **205.170 rows and 12 columns** but In this case I only used 10.000 dataset because my computer can not handle more dataset, but you can used dataset as much as you want.

# How to use REST API for Book's Recommendation System

1. download the clean books dataset on [books_data.csv](https://drive.google.com/file/d/1gbS0ArrQExkqEjE4l3gm7P_fB-BQiKxW/view?usp=share_link)
2. download cosine similarity on [cosine_similarity.csv](https://drive.google.com/file/d/17drmU-ncXP5UCwzQrfqy7uIYeyJZUNcI/view?usp=share_link)
3. download requirements.txt with **pip install -r requirements.txt**
4. run **python3 app.py**
5. Test on your postman with method POST and endpoint **/books_recommendations**
6. Use key on your body as **book_title** and type your favorite's book title as value

### You will get this result

![image](https://user-images.githubusercontent.com/91602612/206841953-9dfd102a-0925-4471-ac9b-d77b36a5ee58.png)

![image](https://user-images.githubusercontent.com/91602612/206841973-91712ed5-8e74-4fb8-9404-e8ea3f8b5c94.png)



