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


# Deliverables:
    * Link to presentation: https://docs.google.com/presentation/d/1GrdKzLJi8I9rXibDwru5aTWgpe7Zy_yEOBjALV0eXJU/edit?usp=sharing
    * Github repository includes:
        - readme
        - main jupyter notebook containing work to get to answer
        - model.py which creates a model to fit, predict and evaluate

# Instructions for Reproducability
- Env.py is required. Inside env.py there are three required variables:
    * sql password
    * sql username (variable is called 'user')
    * sql host


Be sure and evaluate your model using the standard techniques: plotting the residuals, computing the evaluation metric (SSE, RMSE, and/or MSE), comparing to baseline, plotting y by yhat