# House price predictor
Predicts the value of the house based on:
- housingMedianAge
- totalRooms
- totalBedrooms
- medianIncome

### Features
- Uses batch gradient descent to find the weights
- All features were normalized
- Cost function visualisation

`main.py` trains the model using batch gradient descent, the weights returned are used by `prediction.py` to estimate the value of the house based on user input.
