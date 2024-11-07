from pandas import DataFrame

def affordability_category(house_price: int, borrowing_price: int):
    if  house_price <= borrowing_price/4:
        return 'high'
    elif borrowing_price/4 <= house_price <= borrowing_price:
        return 'medium'
    elif borrowing_price <= house_price <= borrowing_price + 300000:
        return 'low'
    else:
        return 'very low'


def affordability_chart_ratings_old(borrowing_price: int, data: DataFrame):
    high = medium = low = very_low = 0
    ratings = data['Price'].apply(lambda price: affordability_category(price, borrowing_price))

    for r in ratings:
        match r:
            case 'high':
                high += 1
            case 'medium':
                medium += 1
            case 'low':
                low += 1
            case 'very low':
                very_low += 1

    return high, medium, low, very_low

def affordability_chart_ratings_new(borrowing_price: int, data: DataFrame):
    high = medium = low = very_low = 0
    ratings = data['Price']

    for r in ratings:
        if  r <= (borrowing_price / 4):
            high += 1
        elif (borrowing_price / 4) <= r <= borrowing_price:
            medium += 1
        elif borrowing_price <= r <= (borrowing_price + 300000):
            low += 1
        else:
            very_low += 1

    return high, medium, low, very_low