def fit_model(train):
    x = train[['total_sqft', 'bedroom_count', 'bathroom_count']]
    y = train.property_value
    
    return = LinearRegression().fit(x, y)