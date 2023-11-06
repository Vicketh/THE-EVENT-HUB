CREATE TABLE Users (
    User_ID SERIAL PRIMARY KEY,
    User_Name VARCHAR(50) NOT NULL,
    User_Email VARCHAR(100) NOT NULL,
    User_Password VARCHAR(100) NOT NULL hash,
    User_PhoneNumber VARCHAR(20),
    User_FirstName VARCHAR(50),
    User_LastName VARCHAR(50),
    User_ProfilePicture image,
    User_PaymentInfo TEXT,
    User_Role VARCHAR(20) NOT NULL
);

CREATE TABLE Events (
    Event_ID SERIAL PRIMARY KEY,
    Organizer_ID INT NOT NULL,
    Event_Name VARCHAR(50) NOT NULL,
    Event_Description TEXT,
    Event_Location VARCHAR(100) NOT NULL,
    Category_ID INT NOT NULL,
    Event_StartDate_Time TIMESTAMP NOT NULL,
    Event_EndDate_Time TIMESTAMP NOT NULL,
    Event_Capacity INT NOT NULL,
    Ticket_url TEXT,
    Event_Picture bytea,
    Event_Host INT NOT NULL,
    Category INT NOT NULL,
    Image_Logo bytea,
    Event_Status VARCHAR(20) NOT NULL
);

CREATE TABLE Categories (
    Category_ID SERIAL PRIMARY KEY,
    Category_Name VARCHAR(50) NOT NULL
);

CREATE TABLE TICKETS (
    Ticket_ID SERIAL PRIMARY KEY,
    Event_ID INT NOT NULL References Events(Event_ID),
    Ticket_Quantity INT NOT NULL,
    Ticket_Price INT NOT NULL,
    Ticket_Available INT NOT NULL,
    Ticket_url TEXT
);

CREATE TABLE User_Events (
    User_Event_ID SERIAL PRIMARY KEY,
    User_ID INT NOT NULL References Users(User_ID),
    Event_ID INT NOT NULL References Events(Event_ID),
    User_Event_Status VARCHAR(20) NOT NULL
);

CREATE TABLE Recommendations (
    Recommendation_ID SERIAL PRIMARY KEY,
    User_ID INT NOT NULL References Users(User_ID),
    Event_ID INT NOT NULL References Events(Event_ID)
);

CREATE TABLE Locations (
    Location_ID SERIAL PRIMARY KEY,
    Event_ID INT NOT NULL References Events(Event_ID),
    Location_pin point NOT NULL,
    Location_Address VARCHAR(100) NOT NULL,
    Location_City VARCHAR(50) NOT NULL,
    Location_State VARCHAR(50) NOT NULL,
    Location_ZipCode INT NOT NULL,
    Location_Country VARCHAR(50) NOT NULL
);

CREATE TABLE Reviews (
    Review_ID SERIAL PRIMARY KEY,
    User_ID INT NOT NULL References Users(User_ID),
    Event_ID INT NOT NULL References Events(Event_ID),
    Review_Rating INT NOT NULL,
    Review_Comment TEXT,
    Review_Date TIMESTAMP NOT NULL
);

CREATE TABLE Messages (
    Message_ID SERIAL PRIMARY KEY,
    User_ID INT NOT NULL References Users(User_ID),
    Event_ID INT NOT NULL References Events(Event_ID),
    Message_Text TEXT NOT NULL,
    Message_Date TIMESTAMP NOT NULL
);

CREATE TABLE Event Categories (
    Event_Category_ID SERIAL PRIMARY KEY,
    Event_ID INT NOT NULL References Events(Event_ID),
    Category_ID INT NOT NULL References Categories(Category_ID)
);

CREATE TABLE ChatRooms (
    ChatRoom_ID SERIAL PRIMARY KEY,
    User_ID INT NOT NULL References Users(User_ID),
    Event_ID INT NOT NULL References Events(Event_ID),
    ChatRoom_Name VARCHAR(50) NOT NULL
);

CREATE TABLE ChatRoom Messages (
    ChatRoom_Message_ID SERIAL PRIMARY KEY,
    ChatRoom_ID INT NOT NULL References ChatRooms(ChatRoom_ID),
    User_ID INT NOT NULL References Users(User_ID),
    ChatRoom_Message_Text TEXT NOT NULL,
    ChatRoom_Message_Date TIMESTAMP NOT NULL
);
