from django.http import JsonResponse
from .models import Users, Events, Categories, Tickets, User_Events, Locations, Event_Categories

# Endpoint to retrieve a list of all events
def event_list(request):
    events = Events.objects.all()
    data = [{'Event_Name': event.Event_Name,
             'Event_Description': event.Event_Description,
             'Event_Location': event.Event_Location,
             'Event_StartDate_Time': event.Event_StartDate_Time,
             'Event_EndDate_Time': event.Event_EndDate_Time,
             'Event_Capacity': event.Event_Capacity,
             'Event_Price': event.Event_Price,
             'Event_Organizer': event.Event_Organizer,
             'Organizer_ID': event.Organizer_ID,
             'Event_Host': event.Event_Host,
             'Event_Status': event.Event_Status} for event in events]
    return JsonResponse(data, safe=False)

# Endpoint to retrieve a list of all categories
def category_list(request):
    categories = Categories.objects.all()
    data = [{'Category_Name': category.Category_Name,
             'Category_Description': category.Category_Description} for category in categories]
    return JsonResponse(data, safe=False)

# Endpoint to retrieve a list of all users
def user_list(request):
    users = Users.objects.all()
    data = [{'User_Name': user.User_Name,
             'User_Email': user.User_Email,
             'User_PhoneNumber': user.User_PhoneNumber,
             'User_FirstName': user.User_FirstName,
             'User_LastName': user.User_LastName,
             'User_ProfilePicture': user.User_ProfilePicture,
             'User_PaymentInfo': user.User_PaymentInfo} for user in users]
    return JsonResponse(data, safe=False)
