# Project Goals
- Acqure the data from sql
- ensure the data is clean
- create a model
- test the model
- make the presentation

# Thought processes for SQL
- Identify what a single unit property is. Going with the assumption that everything in the sql database that isn't listed as having mutliple units, is therefor a single unit property. Also making an assuming that it's only houses.


# Plan
    * Find the states and counties each property tax is in
        - This will require outside data to be pulled in
    * Calculate the distribution rates for each county
        - Need to include distribution of tax rates for each county in deliverable
        - Also need to include a median for where the bulk of houses sit within those rates
        (* Note, these have to be seperate from the model)

    * For the first iteration of the model, the only features we'll be using are *square feet of the home*, *number of bedrooms*, *number of bathrooms*. This will return an estimate of the properties assesed value 'taxvaluedollarcnt'
    
    

# Deliverables:
    * Link to presentation: https://docs.google.com/presentation/d/1GrdKzLJi8I9rXibDwru5aTWgpe7Zy_yEOBjALV0eXJU/edit?usp=sharing
    * Github repository includeds:
        - Stuff and things to be filled out later
        - Model which answers the stakeholder's question about the data

# Pipeline:
 
## ACQUIRE:
Goal: leave this section with a dataframe ready to prepare.

The ad hoc part includes summarizing your data as you read it in and begin to explore, look at the first few rows, data types, summary stats, column names, shape of the data frame, etc.

acquire.py: The reproducible part is the gathering data from SQL.

## PREP:
Goal: leave this section with a dataset that is ready to be analyzed. Data types are appropriate, missing values have been addressed, as have any data integrity issues.

The ad hoc part includes plotting the distributions of individual variables and using those plots to identify outliers and if those should be handled (and if so, how), identify unit scales to identify how to best scale the numeric data, as well as finding erroneous or invalid data that may exist in your dataframe.

Add a data dictionary in your notebook that defines all fields used in either your model or your analysis, and answers the question: why did you use the fields you used, e.g. why did you use bedroom_field1 over bedroom_field2, not why did you use number of bedrooms!

prep.py: The reproducible part is the handling of missing values, fixing data integrity issues, changing data types, etc.

## SPLIT & SCALE:
Goal: leave this section with 2 dataframes (train & test) and scaled data

split_scale.py: split data, scale data (create scaler, fit the scaler to train and transform the train and test using that scaler)

## DATA EXPLORATION
Goal: Address each of the questions you posed in your planning and brainstorming and any others you have come up with along the way through visual or statistical analysis.

When you have completed this step, you will have the findings from your analysis that will be used in your final report, answers to specific questions your customers has asked, and information to move forward toward building a model.

Run at least 1 t-test and 1 correlation test (but as many as you need!)

Visualize all combinations of variables in some way(s).

What independent variables are correlated with the dependent? (this is good)

Which independent variables are correlated with other independent variables? (this is not so good and needs to be addressed)

Summarize your takeaways and conclusions.

## FEATURE SELECTION
Goal: leave this section with a dataframe with the features to be used to build your model.

Are there new features you could create based on existing features that might be helpful?

You could use feature selection techniques to see if there are any that are not adding value to the model.

feature_selection.py: to run whatever functions need to be run to end with a dataframe that contains the features that will be used to model the data.

## MODELING & EVALUATION
Goal: develop a regression model that performs better than a baseline.

You must evaluate a baseline model, and show how the model you end up with performs better than that.

model.py: will have the functions to fit, predict and evaluate the model

Your notebook will contain various algorithms and/or hyperparameters tried, along with the evaluation code and results, before settling on the final algorithm.

Be sure and evaluate your model using the standard techniques: plotting the residuals, computing the evaluation metric (SSE, RMSE, and/or MSE), comparing to baseline, plotting y by yhat