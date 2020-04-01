# Analyzing Yelp Dataset

<br>

## **【[Converting Yelp Dataset to CSV using Pandas](https://link.medium.com/0k0DEb3Qy1)】** 
## **【[Analyzing Yelp Dataset with Scattertext Visualization](https://link.medium.com/k3DRTC57I1)】** 

<br>

## Data Source

**Yelp Open Dataset Challenge** (https://www.yelp.com/dataset/challenge)

Round 13 started January 15, 2019 to December 31, 2019.

<br>

## [Yelp Rating Prediction API](https://gyhou.com/2019-09-27-Yelp-Rating-Prediction/)
- http://br-yelp-predict-rating.herokuapp.com

I trained a model to predict the user’s review rating base on reviews on the Yelp dataset in the each specific category.

My API takes in a JSON string with "category" and "review". After sending the input to my API, it will respond with the predicted rating of the review.

When submitting a review, make sure to specify which category the review is for.

Example input:
```python
{"category": "Auto Repair", 
 "review": "Service is the worst and the wait time is too long."}
```
The API will return a rating base on the category and review.
Example Output:
```python
{'Category': 'Auto_Repair',
 'Review': 'Service is the worst and the wait time is too long.',
 'Predict rating': 1}
```

Below is the list of categories used in the Yelp dataset:
* Active Life
* Auto Repair
* Automotive
* Beauty Spas
* Contractors
* Doctors
* Event Planning Services
* Fashion
* Fast Food
* Hair Salons
* Health Medical
* Home Garden
* Home Services
* Local Services
* Professional Services
* Real Estate
* Shopping 

## Scattertext Visualization

**Examples base on Yelp Reviews group by categories**

[RV Parks and Campgrounds](http://gyhou.com/RV-Parks-Campgrounds-Yelp-Reviews-Scattertext.html)

[RV Repair, RV Dealers, RV Rental](http://gyhou.com/RV-Auto-Yelp-Reviews-Scattertext.html)

[RV Repair, RV Dealers, RV Rental, RV Parks and Campgrounds](http://gyhou.com/RV-Yelp-Reviews-Scattertext.html)


<img src="https://github.com/gyhou/yelp_dataset/blob/master/yelp_rv_scattertext.png?raw=true">

<br>

