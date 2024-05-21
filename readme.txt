Hello, its a readme file about the procedure I have taken to create my model for predicting the price for houses based on locations of Banglore. So here are the steps taken......-------------------->>>>>

1--> Downloaded the "Bengaluru_House_Data.csv"  dataset from google.


2--> It has column names as =[area_type,	availability,	location,	size,	society	total_sqft,	bath,	balcony	price]
     I removed the area_type, society, balcony and avilability columns as these are not affecting the result as that much.


3--> I checked the nullity and remove those rows as they were not in huge according to out original dataset.


4--> Modified the size columns to bhk removing uncertainity like Bedroom,BHK in size column.


5--> For reducing dimension I removed the locations that were appearing less than 10 times in dataset.


6--> I removed the other outliers like less than 300 for price per square fit.


7--> Plotted the scatter charts and histogram for assurity.(for removal of outliers)


8--> Removed the unnecessary "size, price_per_sqft" columns.


9--> Created dummie variables for locations.Dropped price column to make it inputs and price column as output.


10--> Performed train_test_split with tezt_size 20 %. First I checked for LinearRegression and got accuracy of 84% then performed cross_val_score method and got [0.82430186, 0.77166234, 0.85089567, 0.80837764, 0.83653286] as result with avg of 0.81.


11-> Performed GridSearchCV for the algos = LinearRegression, Lasso, Decision_Tree_Regressor and got the best result for Linear_Regression. Created function for prediction.


12--> I used the help of gradio by google to use it for showcasing the model performence.

13--> There will be flagged folder created to take the record of users that what they have got as result with their inputs.

Thankyou so much for putting your valuable efforts.
                                                   
- Devam Singh
