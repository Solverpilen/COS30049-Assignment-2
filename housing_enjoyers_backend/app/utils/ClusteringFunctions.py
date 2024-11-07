

def affordability_category(house_price, borrowing_price):
    if  house_price <= borrowing_price/4:
        return 'high'
    elif borrowing_price/4 <= house_price <= borrowing_price:
        return 'medium'
    elif borrowing_price <= house_price <= borrowing_price + 300000:
        return 'low'
    else:
        return 'very low'


def affordability_chart_ratings(borrowing_price, data):
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