# Flask Order Management System

A comprehensive backend application built with Flask for handling basic order management operations.

## Features

### Core Functionality
- **Add New Orders**: Create orders with unique IDs, item quantities, delivery dates, sender/recipient information
- **Order Management**: Edit existing orders, mark as delivered, and remove orders
- **Action Logging**: Complete audit trail of all operations (Created, Edited, Marked Delivered, Deleted)
- **Order Display**: Clean HTML interface showing all orders with their current statuses

### Technical Features
- RESTful API endpoints for orders and logs
- In-memory data storage (easily replaceable with database)
- Flash messaging for user feedback
- Form validation and error handling
- Responsive HTML tables with action buttons

## Project Structure

```
flask-order-system/
├── app.py                 # Main Flask application
├── templates/
│   ├── base.html         # Base template with navigation
│   ├── index.html        # Main orders display page
│   ├── add_order.html    # Add new order form
│   ├── edit_order.html   # Edit existing order form
│   └── logs.html         # Action logs display
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

## Setup Instructions

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repository-url>
   cd flask-order-system
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install flask
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Access the application**
   Open your browser and navigate to `http://localhost:5000`

## Usage Guide

### Adding Orders
1. Click "Add New Order" from the home page
2. Fill in all required fields:
   - Number of items (positive integer)
   - Delivery date
   - Sender name
   - Recipient name
   - Recipient address
3. Click "Create Order"

### Managing Orders
- **Edit**: Click the "Edit" button to modify order details
- **Mark Delivered**: Click "Mark Delivered" to change status from "Ongoing" to "Delivered"
- **Delete**: Click "Delete" to remove an order (with confirmation prompt)

### Viewing Logs
- Click "View Logs" in the navigation to see all actions performed
- Logs include action type, order ID, performer, and timestamp
- Logs are displayed in reverse chronological order (newest first)

## API Endpoints

The application provides REST API endpoints:

- `GET /api/orders` - Returns all orders in JSON format
- `GET /api/logs` - Returns all action logs in JSON format

Example API usage:
```bash
curl http://localhost:5000/api/orders
curl http://localhost:5000/api/logs
```

## Order Data Structure

Each order contains:
- **ID**: Unique 8-character identifier (auto-generated)
- **Number of Items**: Integer quantity
- **Delivery Date**: Date in YYYY-MM-DD format
- **Sender Name**: String
- **Recipient Name**: String
- **Recipient Address**: Text field
- **Status**: "Ongoing" (default) or "Delivered"
- **Created At**: Automatic timestamp

## Action Log Structure

Each log entry contains:
- **Log ID**: Sequential number
- **Action Type**: "Created", "Edited", "Marked Delivered", or "Deleted"
- **Order ID**: Reference to the affected order
- **Performed By**: User identifier (currently "User" or "System")
- **Timestamp**: Date and time of action

## Development Approach

### Architecture Decisions
1. **In-Memory Storage**: Used Python dictionaries for simplicity and quick development. In production, this should be replaced with a proper database (SQLite, PostgreSQL, etc.)

2. **Template-Based UI**: Used Flask's Jinja2 templating for server-side rendering instead of a separate frontend framework for simplicity

3. **UUID-based IDs**: Generated short, unique identifiers for orders to avoid collision issues

4. **Action Logging**: Implemented comprehensive logging to track all system activities for audit purposes

### Code Organization
- **Single File Application**: All Flask routes and logic in `app.py` for simplicity
- **Modular Templates**: Separate HTML templates with inheritance for maintainability
- **Class-Based Models**: `Order` class to encapsulate order data and methods

### Error Handling
- Form validation for required fields and data types
- User-friendly error messages via Flask's flash messaging
- Confirmation dialogs for destructive actions

## Future Enhancements

### Database Integration
Replace in-memory storage with SQLAlchemy:
```python
pip install flask-sqlalchemy
```

### Authentication
Add user authentication to track who performs actions:
```python
pip install flask-login
```

## Testing

To test the application:

1. **Manual Testing**
   - Create several orders with different data
   - Edit orders and verify changes
   - Mark orders as delivered
   - Delete orders and check logs
   - Verify all actions are logged correctly

2. **API Testing**
   ```bash
   # Test orders endpoint
   curl -X GET http://localhost:5000/api/orders | python -m json.tool
   
   # Test logs endpoint
   curl -X GET http://localhost:5000/api/logs | python -m json.tool
   ```

### Pages Screenshots
![image](https://github.com/user-attachments/assets/0fb3b8f1-8900-443d-afe5-4c6c6f29eb3c)
![image](https://github.com/user-attachments/assets/9764ffea-559e-4599-8605-6ea9a567338f)
![image](https://github.com/user-attachments/assets/331cc567-de8b-492b-bed0-8f70f2705f96)
![image](https://github.com/user-attachments/assets/ab4e0077-f874-4538-8636-0d8f38cdf196)
![image](https://github.com/user-attachments/assets/e3d6c7e2-e138-48ba-ab77-7ef7840f54d3)






