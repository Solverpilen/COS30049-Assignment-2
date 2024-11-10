

def affordability_category(house_price, borrowing_price):

    if  house_price <= borrowing_price/4:
        return 'high'
    elif borrowing_price/4 <= house_price <= borrowing_price:
        return 'medium'
    elif borrowing_price <= house_price <= borrowing_price + 300000:
        return 'low'
    else:
        return 'very low'

# 'data' is the pandas data frame used to process the raw data from the AI models
def pie_chart_ratings(borrowing_price,data):
    high = medium = low = very_low = 0

    # this allows the 'Price' column to be used as a parameter for affordabiility_category. It goes through all the prices in the data dataframe
    # and puts it through the function which then returns an array of ratings.
    ratings = data['Price'].apply(lambda price: affordability_category(price, borrowing_price))

    for rating in ratings:
        if rating == 'high':
            high += 1
        elif rating == 'medium':
            medium += 1
        elif rating == 'low':
            low += 1
        elif rating == 'very low':
            very_low += 1

    return high, medium, low, very_low

# obsolete function used for the second pie chart
def cluster_pie_chart_ratings(data):

    high, moderate, low = 0

    for rating in data['data']:
        if rating.Level == "High":
            high += 1
        elif rating.Level == "Moderate":
            moderate += 1
        elif rating.Level == "low":
            low += 1

    return high, moderate, low