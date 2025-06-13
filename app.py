from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from datetime import datetime
import uuid
import json
import os

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'

# In-memory storage (use database in production)
orders = {}
action_logs = []

class Order:
    def __init__(self, number_of_items, delivery_date, sender_name, recipient_name, recipient_address):
        self.id = str(uuid.uuid4())[:8]  # Short unique ID
        self.number_of_items = number_of_items
        self.delivery_date = delivery_date
        self.sender_name = sender_name
        self.recipient_name = recipient_name
        self.recipient_address = recipient_address
        self.status = "Ongoing"
        self.created_at = datetime.now()

    def to_dict(self):
        return {
            'id': self.id,
            'number_of_items': self.number_of_items,
            'delivery_date': self.delivery_date,
            'sender_name': self.sender_name,
            'recipient_name': self.recipient_name,
            'recipient_address': self.recipient_address,
            'status': self.status,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S')
        }

def log_action(action_type, order_id, performed_by="System"):
    """Log an action to the action logs"""
    log_entry = {
        'id': len(action_logs) + 1,
        'action_type': action_type,
        'order_id': order_id,
        'performed_by': performed_by,
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    action_logs.append(log_entry)

@app.route('/')
def index():
    """Display all orders"""
    return render_template('index.html', orders=orders)

@app.route('/add_order', methods=['GET', 'POST'])
def add_order():
    """Add a new order"""
    if request.method == 'POST':
        try:
            number_of_items = int(request.form['number_of_items'])
            delivery_date = request.form['delivery_date']
            sender_name = request.form['sender_name']
            recipient_name = request.form['recipient_name']
            recipient_address = request.form['recipient_address']
            
            # Create new order
            order = Order(number_of_items, delivery_date, sender_name, recipient_name, recipient_address)
            orders[order.id] = order
            
            # Log the action
            log_action("Created", order.id, "User")
            
            flash(f'Order {order.id} created successfully!', 'success')
            return redirect(url_for('index'))
            
        except ValueError:
            flash('Please enter valid number of items', 'error')
        except Exception as e:
            flash(f'Error creating order: {str(e)}', 'error')
    
    return render_template('add_order.html')

@app.route('/edit_order/<order_id>', methods=['GET', 'POST'])
def edit_order(order_id):
    """Edit an existing order"""
    if order_id not in orders:
        flash('Order not found', 'error')
        return redirect(url_for('index'))
    
    order = orders[order_id]
    
    if request.method == 'POST':
        try:
            order.number_of_items = int(request.form['number_of_items'])
            order.delivery_date = request.form['delivery_date']
            order.sender_name = request.form['sender_name']
            order.recipient_name = request.form['recipient_name']
            order.recipient_address = request.form['recipient_address']
            
            # Log the action
            log_action("Edited", order_id, "User")
            
            flash(f'Order {order_id} updated successfully!', 'success')
            return redirect(url_for('index'))
            
        except ValueError:
            flash('Please enter valid number of items', 'error')
        except Exception as e:
            flash(f'Error updating order: {str(e)}', 'error')
    
    return render_template('edit_order.html', order=order)

@app.route('/mark_delivered/<order_id>')
def mark_delivered(order_id):
    """Mark an order as delivered"""
    if order_id not in orders:
        flash('Order not found', 'error')
    else:
        orders[order_id].status = "Delivered"
        log_action("Marked Delivered", order_id, "User")
        flash(f'Order {order_id} marked as delivered!', 'success')
    
    return redirect(url_for('index'))

@app.route('/delete_order/<order_id>')
def delete_order(order_id):
    """Delete an order"""
    if order_id not in orders:
        flash('Order not found', 'error')
    else:
        del orders[order_id]
        log_action("Deleted", order_id, "User")
        flash(f'Order {order_id} deleted successfully!', 'success')
    
    return redirect(url_for('index'))

@app.route('/logs')
def view_logs():
    """View action logs"""
    return render_template('logs.html', logs=action_logs)

@app.route('/api/orders')
def api_orders():
    """API endpoint to get all orders"""
    return jsonify([order.to_dict() for order in orders.values()])

@app.route('/api/logs')
def api_logs():
    """API endpoint to get all logs"""
    return jsonify(action_logs)

if __name__ == '__main__':
    app.run(debug=True)