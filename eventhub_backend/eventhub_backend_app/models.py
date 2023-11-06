from django.db import models
from django.contrib.auth.models import User

class Users(models.Model):
    User_ID = models.IntegerField(max_length=10)
    User_Name = models.CharField(max_length=50)
    User_Email = models.CharField(max_length=50)
    User_Password = models.CharField(max_length=50)
    User_PhoneNumber = models.IntegerField(max_length=10)
    User_FirstName = models.CharField(max_length=50)
    User_LastName = models.CharField(max_length=50)
    User_ProfilePicture = models.ImageField(upload_to='THE_EVENT_HUB/Profile_Pictures')
    User_PaymentInfo = models.TextField(max_length=120)
    
    def __str__(Users):
        return Users.User_Name
    
    
class Events(models.Model):
    Event_ID = models.IntegerField(max_length=10)
    Event_Name = models.CharField(max_length=50)
    Event_Description = models.TextField(max_length=120)
    Event_Location = models.CharField(max_length=50)
    Event_StartDate_Time = models.DateTimeField()
    Event_EndDate_Time = models.DateTimeField()
    Category_ID = models.IntegerField(max_length=10)
    Event_Capacity = models.IntegerField(max_length=10)
    Event_Price = models.IntegerField(max_length=10)
    Event_Picture = models.ImageField(upload_to='THE_EVENT_HUB/Event_Pictures')
    Event_Organizer = models.CharField(max_length=50)
    Organizer_ID = models.IntegerField(max_length=10)
    Ticket_ID = models.IntegerField(max_length=10)
    Event_Host = models.CharField(max_length=50)
    Image_Logo = models.ImageField(upload_to='THE_EVENT_HUB/Event_Logo')
    Event_Status = models.CharField(max_length=50)
    
    def __str__(Events):
        return Events.Event_Name
    
class Categories(models.Model):
    Category_ID = models.IntegerField(max_length=10)
    Category_Name = models.CharField(max_length=50)
    Category_Description = models.TextField(max_length=120)
    
    def __str__(Categories):
        return Categories.Category_Name

class Tickets(models.Model):
    Ticket_ID = models.IntegerField(max_length=10)
    Event_ID = models.IntegerField(max_length=10)
    Ticket_Quantity = models.IntegerField(max_length=10)
    Ticket_Price = models.IntegerField(max_length=10)
    Ticket_Available = models.IntegerField(max_length=50)
    Ticket_url = models.TextField(max_length=120)
    
    def __str__(Tickets):
        return Tickets.Ticket_Name

class User_Events(models.Model):
    User_Event_ID = models.IntegerField(max_length=10)
    User_ID = models.IntegerField(max_length=10)
    Event_ID = models.IntegerField(max_length=10)
    
    def __str__(User_Events):
        return User_Events.User_Event_ID


class Recommendations(models.Model):
    Recommendation_ID = models.IntegerField(max_length=10)
    User_ID = models.IntegerField(max_length=10)
    Event_ID = models.IntegerField(max_length=10)
    
    def __str__(Recommendations):
        return Recommendations.Recommendation_ID


class Locations(models.Model):
    Location_ID = models.IntegerField(max_length=10)
    Event_ID = models.IntegerField(max_length=10)
    Location_Pin = models.BinaryField(max_length=10)
    Location_Address = models.CharField(max_length=50)
    Location_City = models.CharField(max_length=20)
    Location_State = models.CharField(max_length=20)
    Location_ZipCode = models.IntegerField(max_length=10)
    Location_Country = models.CharField(max_length=20)
    
    def __str__(Locations):
        return Locations.Location_ID

class Reviews(models.Model):
    Review_ID = models.IntegerField(max_length=10)
    User_ID = models.IntegerField(max_length=10)
    Event_ID = models.IntegerField(max_length=10)
    Review_Rating = models.IntegerField(max_length=10)
    Review_Comment = models.TextField(max_length=120)
    Review_Date = models.DateField(max_length=20)
    
    
    def __str__(Reviews):
        return Reviews.Review_ID

class Messages(models.Model):
    Message_ID = models.IntegerField(max_length=10)
    User_ID = models.IntegerField(max_length=10)
    Message_text = models.TextField(max_length=120)
    Message_Date = models.DateField(max_length=20)
    
    def __str__(Messages):
        return Messages.Message_ID

class Event_Categories(models.Model):
    Event_Category_ID = models.IntegerField(max_length=10)
    Event_ID = models.IntegerField(max_length=10)
    Category_ID = models.IntegerField(max_length=10)
    
    def __str__(Event_Categories):
        return Event_Categories.Event_Category_ID

class Event_Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Events, on_delete=models.CASCADE)
    reminder = models.BooleanField(default=False)
    
    
class ChatRooms(models.Model):
    event = models.ForeignKey(Events, on_delete=models.CASCADE)
    users = models.ManyToManyField(User)
    Chatroom_ID = models.IntegerField(max_length=10)
    User_ID = models.IntegerField(max_length=10)
    Event_ID = models.IntegerField(max_length=10)
    Chatroom_name = models.TextField(max_length=120)
   
    def __str__(Chat):
        return Chat.Chat_ID
    
class ChatRoom_Messages(models.Model):
    ChatRoom_Message_ID = models.IntegerField(max_length=10)
    ChatRoom_ID = models.IntegerField(max_length=10)
    User_ID = models.IntegerField(max_length=10)
    ChatRoom_Message_text = models.TextField(max_length=120)
    ChatRoom_Message_Date = models.DateField(max_length=20)
    
    def __str__(ChatRoom_Messages):
        return ChatRoom_Messages.ChatRoom_Message_ID
    
