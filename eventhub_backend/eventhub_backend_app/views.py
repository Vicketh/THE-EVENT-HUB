from django.shortcuts import render
from .models import Users, Events, Categories, Tickets, User_Events, Locations, Event_Categories

def event_list(request):
    Events = Events.objects.all()
    Categories = Categories.objects.all()
    Locations = Locations.objects.all()
    Event_Categories = Event_Categories.objects.all()
    
    categorized_events = {}
    
    for Category in Categories:
        category_events = Events.objects.filter(category=Category)
        category_data = {
            Event_Name: category_events.Event_Name,
            Event_Description: category_events.Event_Description,
            Event_Location: category_events.Event_Location,
            Event_StartDate_Time: category_events.Event_StartDate_Time,
            Category_Name: category_events.Category_Name,
        }
        categorized_events.append(category_data)
    
    for Location in Locations:
        Location_events = Events.objects.filter(location=Location)
        location_data = {
            Location_Name: Location_events.Location_Name,
            Location_Pin: Location_events.Location_Pin,
            Location_Address: Location_events.Location_Address,
            Event_ID: Location_events.Event_ID,
        }
        Location_events.append(location_data)

def Categories(request):
    Categories = Categories.objects.all()
    Events = Events.objects.all()
    Event_Categories = Event_Categories.objects.all()
    
    Events_by_Category = {}
    
    for category in Categories:
        category_events = Events.objects.filter(category=category)
        category_data = {
            Event_Name: category_events.Event_Name,
            Event_Description: category_events.Event_Description,
            Event_Location: category_events.Event_Location,
            Event_StartDate_Time: category_events.Event_StartDate_Time,
            Category_Name: category_events.Category_Name,
        }
        Events_by_Category.append(category_data)
    
    for event in Events:
        event_categories = Categories.objects.filter(event=event)
        event_data = {
            Event_Name: event_categories.Event_Name,
            Event_Description: event_categories.Event_Description,
            Event_Location: event_categories.Event_Location,
            Event_StartDate_Time: event_categories.Event_StartDate_Time,
            Category_Name: event_categories.Category_Name,
        }
        Events_by_Category.append(event_data)
    
    for event_category in Event_Categories:
        event_category_data = {
            Event_Name: event_category.Event_Name,
            Category_Name: event_category.Category_Name,
        }
        Events_by_Category.append(event_category_data)
        
        return render(request, Users, Events)
