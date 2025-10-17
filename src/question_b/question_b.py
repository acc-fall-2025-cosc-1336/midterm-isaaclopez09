#write functions here, don't add input('') statements here!

def get_miles_per_hour(kilometers, minutes):
    
    
    miles = kilometers * 0.621371
    hours = minutes / 60
    
    miles_per_hour = miles / hours
    
    return miles_per_hour