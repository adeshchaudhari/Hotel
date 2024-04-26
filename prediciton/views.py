from django.shortcuts import render
import pickle

# Create your views here.
def predicitons(no_of_adults,
    no_of_children,
    no_of_weekend_nights,
    no_of_week_nights,
    type_of_meal_plan,
    required_car_parking_space,
    room_type_reserved,
    lead_time,
    arrival_year,
    arrival_month,
    arrival_date,
    market_segment_type,
    repeated_guest,
    no_of_previous_cancellations,
    no_of_previous_bookings_not_canceled,
    avg_price_per_room,
    no_of_special_requests):

    model = pickle.load(open("Hotel_price.pkl", "rb"))

    predicitons = model.predict([[no_of_adults,
    no_of_children,
    no_of_weekend_nights,
    no_of_week_nights,
    type_of_meal_plan,
    required_car_parking_space,
    room_type_reserved,
    lead_time,
    arrival_year,
    arrival_month,
    arrival_date,
    market_segment_type,
    repeated_guest,
    no_of_previous_cancellations,
    no_of_previous_bookings_not_canceled,
    avg_price_per_room,
    no_of_special_requests]])

    if predicitons == 1:
        return "Not_Cancelled"

    else:
        return "Cancelled"


def status(request):
    if request.method == 'post':
        no_of_adults = eval(request.post.get("adults")) 
        no_of_children = eval(request.post.get("childerns")) 
        no_of_weekend_nights = eval(request.post.get("weekends")) 
        no_of_week_nights = eval(request.post.get("week_nights")) 
        type_of_meal_plan = eval(request.post.get("meal_plan")) 

        required_car_parking_space = eval(request.post.get("parking")) 
        room_type_reserved = eval(request.post.get("reserved")) 
        lead_time = eval(request.post.get("lead_time")) 

        arrival_year = eval(request.post.get("arrival_year")) 
        arrival_date = eval(request.post.get("date")) 
        market_segment_type = eval(request.post.get("type")) 
        repeated_guest = eval(request.post.get("guest")) 
        no_of_previous_cancellations = eval(request.post.get("cancellations")) 
        no_of_previous_bookings_not_canceled = eval(request.post.get("not_canceled"))
        avg_price_per_room = eval(request.post.get("price_room"))
        no_of_special_requests = eval(request.post.get("special_request"))
        arrival_month = eval(request.post.get("arrival_month"))

        result = predicitons(no_of_adults,
        no_of_children,
        no_of_weekend_nights,
        no_of_week_nights,
        type_of_meal_plan,
        required_car_parking_space,
        room_type_reserved,
        lead_time,
        arrival_year,
        arrival_month,
        arrival_date,
        market_segment_type,
        repeated_guest,
        no_of_previous_cancellations,
        no_of_previous_bookings_not_canceled,
        avg_price_per_room,
        no_of_special_requests)

        return render(request)
    
