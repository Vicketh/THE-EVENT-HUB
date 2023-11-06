from django.contrib import admin
from .models import Users, Events, Categories, Tickets, User_Events, Recommendations, Locations, Reviews, Messages, Event_Categories, ChatRooms, ChatRoom_Messages

admin.site.register(Users)
admin.site.register(Events)
admin.site.register(Categories)
admin.site.register(Tickets)
admin.site.register(User_Events)
admin.site.register(Recommendations)
admin.site.register(Locations)
admin.site.register(Reviews)
admin.site.register(Messages)
admin.site.register(Event_Categories)
admin.site.register(ChatRooms)
admin.site.register(ChatRoom_Messages)

class EventAdmin(admin.ModelAdmin):
    list_display = ('event_id', 'event_name', 'event_description', 'event_StartDate_Time', 'event_EndDate_Time', 'event_location', 'event_category', 'Ticket_url', 'event_host', 'event_picture', 'event_status')
    list_filter = ('event_id', 'event_name', 'event_description', 'event_StartDate_Time', 'event_EndDate_Time', 'event_location', 'event_category', 'Ticket_url', 'event_host', 'event_picture', 'event_status')
    search_fields = ('event_id', 'event_name', 'event_description', 'event_StartDate_Time', 'event_EndDate_Time', 'event_location', 'event_category', 'Ticket_url', 'event_host', 'event_picture', 'event_status')
    
class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'user_name', 'user_email', 'user_password', 'user_picture', 'user_status')
    list_filter = ('user_id', 'user_name', 'user_email', 'user_password', 'user_picture', 'user_status')
    search_fields = ('user_id', 'user_name', 'user_email', 'user_password', 'user_picture', 'user_status')
    
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('category_id', 'category_name')
    list_filter = ('category_id', 'category_name')
    search_fields = ('category_id', 'category_name')

class TicketsAdmin(admin.ModelAdmin):
    list_display = ('ticket_id', 'event_id', 'ticket_quantity', 'ticket_price', 'ticket_available', 'ticket_url')
    list_filter = ('ticket_id', 'event_id', 'ticket_quantity', 'ticket_price', 'ticket_available', 'ticket_url')
    search_fields = ('ticket_id', 'event_id', 'ticket_quantity', 'ticket_price', 'ticket_available', 'ticket_url')

class User_EventsAdmin(admin.ModelAdmin):
    list_display = ('user_event_id', 'user_id', 'event_id', 'user_event_status')
    list_filter = ('user_event_id', 'user_id', 'event_id', 'user_event_status')
    search_fields = ('user_event_id', 'user_id', 'event_id', 'user_event_status')

class RecommendationsAdmin(admin.ModelAdmin):
    list_display = ('recommendation_id', 'user_id', 'event_id')
    list_filter = ('recommendation_id', 'user_id', 'event_id')
    search_fields = ('recommendation_id', 'user_id', 'event_id')

class LocationsAdmin(admin.ModelAdmin):
    list_display = ('location_id', 'event_id', 'location_pin', 'location_Address', 'location_city', 'location_state', 'location_zipcode', 'location_country',)
    list_filter = ('location_id', 'event_id', 'location_pin', 'location_Address', 'location_city', 'location_state', 'location_zipcode', 'location_country',)
    search_fields = ('location_id', 'event_id', 'location_pin', 'location_Address', 'location_city', 'location_state', 'location_zipcode', 'location_country',)

class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('review_id', 'user_id', 'event_id', 'review_rating', 'review_comment', 'review_date')
    list_filter = ('review_id', 'user_id', 'event_id', 'review_rating', 'review_comment', 'review_date')
    search_fields = ('review_id', 'user_id', 'event_id', 'review_rating', 'review_comment', 'review_date')

class MessagesAdmin(admin.ModelAdmin):
    list_display = ('message_id', 'user_id', 'event_id', 'message_text', 'message_date')
    list_filter = ('message_id', 'user_id', 'event_id', 'message_text', 'message_date')
    search_fields = ('message_id', 'user_id', 'event_id', 'message_text', 'message_date')

class Event_CategoriesAdmin(admin.ModelAdmin):
    list_display = ('event_category_id', 'event_id', 'category_id')
    list_filter = ('event_category_id', 'event_id', 'category_id')
    search_fields = ('event_category_id', 'event_id', 'category_id')

class ChatRoomsAdmin(admin.ModelAdmin):
    list_display = ('chatroom_id', 'user_id', 'event_id', 'chatroom_name')
    list_filter = ('chatroom_id', 'user_id', 'event_id', 'chatroom_name')
    search_fields = ('chatroom_id', 'user_id', 'event_id', 'chatroom_name')

class ChatRoom_MessagesAdmin(admin.ModelAdmin):
    list_display = ('chatroom_message_id', 'chatroom_id', 'user_id', 'chatroom_message_text', 'chatroom_message_date')
    list_filter = ('chatroom_message_id', 'chatroom_id', 'user_id', 'chatroom_message_text', 'chatroom_message_date')
    search_fields = ('chatroom_message_id', 'chatroom_id', 'user_id', 'chatroom_message_text', 'chatroom_message_date')
