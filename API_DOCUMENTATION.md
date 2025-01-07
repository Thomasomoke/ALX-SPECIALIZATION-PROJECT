# API Documentation

This document provides details about the endpoints in my EVENT EASE Application.

---
## **Authentication and User Management**

### **1. Register User**
- **URL:** `/register/`
- **Method:** `GET` | `POST`
- **Description:** Register a new user account.
- **Response:** Redirects to the login page upon successful registration.

---

### **2. Login User**
- **URL:** `/login/`
- **Method:** `GET` | `POST`
- **Description:** Authenticate a user and start a session.
- **Response:** Redirects to the dashboard on success.

---

### **3. Logout User**
- **URL:** `/logout/`
- **Method:** `GET`
- **Description:** Logs out the current user and ends the session.

---

### **4. Password Reset Workflow**
- **Password Reset Request:**  
  - **URL:** `/password_reset/`  
  - **Method:** `GET` | `POST`  
  - **Template:** `accounts/password_reset.html`  
  - **Description:** Starts the password reset process.  
  - **Response:** Redirects to `/password_reset_done/` upon success.

- **Password Reset Done:**  
  - **URL:** `/password_reset_done/`  
  - **Method:** `GET`  
  - **Template:** `accounts/password_reset_done.html`  
  - **Description:** Displays a confirmation that the reset email has been sent.

- **Password Reset Confirm:**  
  - **URL:** `/reset/<uidb64>/<token>/`  
  - **Method:** `GET` | `POST`  
  - **Template:** `accounts/password_reset_confirm.html`  
  - **Description:** Confirms the password reset request and allows the user to set a new password.

- **Password Reset Complete:**  
  - **URL:** `/reset_done/`  
  - **Method:** `GET`  
  - **Template:** `accounts/password_reset_complete.html`  
  - **Description:** Displays a success message after the password reset process is complete.

---

## **Dashboard**

### **5. Dashboard**
- **URL:** `/dashboard/`
- **Method:** `GET`
- **Description:** Displays an overview of user activities, orders, and events.


## **Event and Booking Management**

### **11. Create Event**
- **URL:** `/create_event/`
- **Method:** `GET` | `POST`
- **Description:** Creates a new event.

---

### **12. Event List**
- **URL:** `/events/`
- **Method:** `GET`
- **Description:** Lists all events.

---

### **13. Event Detail**
- **URL:** `/events/<int:pk>/`
- **Method:** `GET`
- **Description:** Retrieves details for a specific event.

---

### **14. Create Booking**
- **URL:** `/create_booking/`
- **Method:** `GET` | `POST`
- **Description:** Creates a new booking for an event.

---

### **15. Booking List**
- **URL:** `/bookings/`
- **Method:** `GET`
- **Description:** Lists all bookings.

- **Filtered Booking List:**  
  - **URL:** `/bookings/<int:event_pk>/`  
  - **Method:** `GET`  
  - **Description:** Lists bookings for a specific event.

---

### **16. Booking Confirmation**
- **URL:** `/booking-confirmation/`
- **Method:** `GET`
- **Description:** Displays a confirmation page after a successful booking.

---

### **17. Delete Booking**
- **URL:** `/bookings/delete/`
- **Method:** `POST`
- **Description:** Deletes a specified booking.

---

## **Ticket Management**

### **18. Create Ticket Category**
- **URL:** `/create_ticket_category/`
- **Method:** `GET` | `POST`
- **Description:** Creates a new ticket category for events.

---

## **API Documentation (Swagger UI)**

### **19. Swagger UI**
- **URL:** `/swagger/`
- **Method:** `GET`
- **Description:** Displays the Swagger UI for API documentation.

---

## Notes
- Some endpoints require user authentication.
- Response formats and error handling should be based on the provided templates.
- Swagger UI facilitates API exploration and testing.
