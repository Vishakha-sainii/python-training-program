#Q1. Object Modeling & Core OOP
#Design a multi-role User Management System where:
#A base class defines common identity attributes.
#Multiple specialized user types inherit from the base class.
#Each subclass overrides at least one behavior from the parent class.
#A class-level attribute tracks the total number of active users across all subclasses.

from collections import namedtuple
import time
from functools import wraps

class User:
    active_users = 0  # class-level attribute

    def __init__(self, user_id: int, name: str):
        self.user_id = user_id
        self.name = name
        User.active_users += 1

    def role(self):
        return "Generic User"

    def access_level(self):
        return "basic"

    def deactivate(self):
        User.active_users -= 1

    def __del__(self):
        User.active_users -= 1


class Admin(User):
    def role(self):
        return "Admin"

    def access_level(self):
        return "full"


class Customer(User):
    def role(self):
        return "Customer"

    def access_level(self):
        return "limited"
        
# Q2: Advanced Class Construction

class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    @classmethod
    def from_string(cls, data: str):
        """Creates object from serialized string"""
        name, price = data.split(",")
        return cls(name.strip(), float(price.strip()))

    @staticmethod
    def is_valid_price(price):
        """Validation independent of class state"""
        return price > 0

# Q3: Deep Usage of Special Methods

class Order:
    def __init__(self, order_id: int, items: list):
        self.order_id = order_id
        self.items = items

    def __str__(self):
        return f"Order {self.order_id} with {len(self.items)} items"

    def __repr__(self):
        return f"Order(order_id={self.order_id}, items={self.items})"

    def __len__(self):
        return len(self.items)

    def __eq__(self, other):
        return self.order_id == other.order_id

    def __lt__(self, other):
        return len(self) < len(other)

    def __call__(self):
        return f"Processing order {self.order_id}"
        

#Q4 & Q9: Decorator-Driven Behavior Control

def execution_timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"[TIMER] {func.__name__} took {end - start:.4f}s")
        return result
    return wrapper


def log_execution(enabled=True):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if enabled:
                print(f"[LOG] Executing {func.__name__}")
            return func(*args, **kwargs)
        return wrapper
    return decorator


def require_admin(func):
    @wraps(func)
    def wrapper(user, *args, **kwargs):
        if user.role() != "Admin":
            raise PermissionError("Admin access required")
        return func(user, *args, **kwargs)
    return wrapper



# Q5: Generator-Based Data Streaming
class DataStore:
    def __init__(self, data):
        self.data = data

    def stream_data(self):
        """Generator for lazy processing"""
        for item in self.data:
            yield item



# Q6: Immutable Data Modeling (namedtuple)

Config = namedtuple("Config", ["env", "debug", "version"])


class AppConfig:
    def __init__(self):
        self.config = Config(env="prod", debug=False, version="1.0")

    def get_config(self):
        return self.config



# Q7: Control Flow with loop-else

def find_user(user_list, user_id):
    for user in user_list:
        if user.user_id == user_id:
            return user
    else:
        print("User not found")
        return None



# Q8: Module Execution Boundary

def run_demo():
    print("\n--- USER MANAGEMENT SYSTEM DEMO ---\n")

    # Users
    admin = Admin(1, "Alice")
    customer = Customer(2, "Bob")

    print(f"{admin.name} -> {admin.role()}, Access: {admin.access_level()}")
    print(f"{customer.name} -> {customer.role()}, Access: {customer.access_level()}")
    print(f"Active users: {User.active_users}")

    # Product
    product = Product.from_string("Laptop, 75000")
    print(f"\nProduct created: {product.name}, Price: {product.price}")
    print("Valid price:", Product.is_valid_price(product.price))

    # Order
    order1 = Order(101, ["item1", "item2"])
    order2 = Order(102, ["item1"])

    print("\n", order1)
    print("Order length:", len(order1))
    print("Order comparison:", order1 > order2)
    print(order1())

    # Decorators
    @execution_timer
    @log_execution(enabled=True)
    def sample_task():
        time.sleep(0.2)
        print("Task executed")

    sample_task()

    # Access control decorator
    @require_admin
    def delete_system(user):
        print("System deleted")

    delete_system(admin)

    # Generator
    print("\nStreaming data:")
    store = DataStore(range(5))
    for value in store.stream_data():
        print(value)

    # namedtuple immutability
    config = AppConfig().get_config()
    print("\nApp Config:", config)

    # Loop-else
    users = [admin, customer]
    find_user(users, 99)

    print("\n--- DONE WITH DEMO ---")



# Q8: Execution Logic Guard


if __name__ == "__main__":
    run_demo()

