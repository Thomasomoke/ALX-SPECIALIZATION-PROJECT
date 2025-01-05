**EVENT EASE APP**



**Ticketing System and Booking System**
![Registration Page](event_images/homepage.png)


**Overview**


The Ticketing System is a Django-based web application that simplifies event management by offering features such as user registration,<br> event booking, and ticket categorization. <br> <br> The platform is designed with a focus on providing a seamless user experience, security, and scalability. <br> <br>
**Core Features** <br>
**User Registration and Authentication:** <br> <br>


![Registration Page](event_images/signup.png)

Secure user registration with email verification.<br>

Login, "Forgot Password," and "Sign Up" functionalities.<br>
![Registration Page](event_images/login.png)

Hashed passwords for enhanced security<br> <br>
**Event Listings:** <br> <br>
Browse available events with details such as date, time, location, and slots.<br>
Detailed event pages for additional information and registration.<br> <br>
![Registration Page](event_images/events.png)
**Booking System:**<br>
User-friendly booking interface with ticket categorization (e.g., VIP, Regular, Early Bird).<br>

Automatic confirmation emails upon successful booking.<br> <br>
![Registration Page](event_images/booking.png)
**Admin Panel:**


Manage events, user registrations, and permissions.


Analytics for tracking registrations and popular events. <br>
**Additional Enhancements**<br>
**User Profiles:**<br>
Dashboard for viewing booking history and upcoming events.<br>

Profile updates, including pictures and contact details.<br> <br>
![Registration Page](event_images/createevent.png)
**Accessibility:** <br>
WCAG-compliant design with screen reader support.

Keyboard navigation for enhanced accessibility. <br> <br>
**Scalability:** <br>


Ready for deployment on cloud platforms like AWS and Heroku.

Caching mechanisms to optimize performance. <br><br>
**Installation**
**Prerequisites**<br>
Python 3.8+

Django 3.2+

PostgreSQL (or SQLite for development)

Node.js and npm (for optional frontend enhancements) <br><br>
**Setup**
**Clone the repository:**
git clone https://github.com/yourusername/ticketing-system.git
cd ticketing-system
<br><br>
Create a virtual environment and install dependencies:
<br>
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt


**Configure the database in settings.py:**
<br><br>
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_database_name',
        'USER': 'your_database_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}



**Apply migrations:**

python manage.py migrate


**run the development server**

python manage.py runserver

**Access the application at http://127.0.0.1:8000.**


**Usage**

**Admin Panel** (For users with Priviledges) <br>
Access the admin panel at http://127.0.0.1:8000/admin.
<br>
Use the admin interface to create, update, and delete events

![Registration Page](event_images/admin.png)

**User Features**
Register or log in to view events and make bookings.

Manage bookings and profiles through the dashboard.


**API Endpoints**


**User Authentication**


POST /api/register: Register a new user.

POST /api/login: Authenticate a user.


**Events**


GET /api/events: Retrieve a list of available events.

POST /api/book: Book tickets for an event.


**Pending Features**


Payment Integration: Secure payment gateway support (e.g., Stripe, PayPal).

QR Code Scanning: Automated QR code generation for event check-ins.

Enhanced Notifications: SMS or push notifications for reminders.


**Lessons Learned**


The importance of responsive design for a seamless user experience.

Balancing feature richness with development timelines.

Leveraging Django’s built-in tools for rapid development.


**Next Steps**


Finalize payment integration.

Implement advanced analytics for event tracking.

Deploy the application on Heroku or AWS.


**License**

This project is licensed under the MIT License. See the LICENSE file for details.


**Contributing**


Contributions are welcome! Please fork the repository and submit a pull request for review.