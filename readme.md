# Project Goals
- Acqure the data from sql
- ensure the data is clean
- create a model
- test the model
- make the presentation

### Source link for the FIPS
> https://www.nrcs.usda.gov/wps/portal/nrcs/detail/national/home/?cid=nrcs143_013697

# Data Dictionary
| Pandas Dataframe | SQL Database                 | Field Description                | Field Purpose                                                                        |
|------------------|------------------------------|----------------------------------|--------------------------------------------------------------------------------------|
| bedroom_count    | bedroomcnt                   | # of bedrooms in the home        | Feature to be used to predict property value                                         |
| bathroom_count   | bathroomcnt                  | # of bathrooms in the home       | Feature to be used to predict property value                                         |
| total_sqft       | calculatedfinishedsquarefeet | Total amount of square feet      | Used calculated sqft due to it being the overall sqft as opposed to a rough estimate |
| property_value   | taxvaluedollarcnt            | Value of the home                | Goal of the project is to attempt to predict the property value using other fiels    |
| tax_amount       | taxamount                    | Tax value of the home            | Used to help identify tax trends by county                                           |
| county           | n/a                          | Which county the home resides in | Data pulled from external source; used to get statistics by county                   |
| state            | n/a                          | Which state the home resides in  | Data pulled from external source; useful to see which state the houses are in        |


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

# Instructions for Reproducability
- Env.py is required. Inside env.py there are three required variables:
    * sql password
    * sql username (variable is called 'user')
    * sql host

## MODELING & EVALUATION
Goal: develop a regression model that performs better than a baseline.

You must evaluate a baseline model, and show how the model you end up with performs better than that.

model.py: will have the functions to fit, predict and evaluate the model

Your notebook will contain various algorithms and/or hyperparameters tried, along with the evaluation code and results, before settling on the final algorithm.

Be sure and evaluate your model using the standard techniques: plotting the residuals, computing the evaluation metric (SSE, RMSE, and/or MSE), comparing to baseline, plotting y by yhat