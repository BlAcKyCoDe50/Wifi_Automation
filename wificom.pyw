import threading
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import PhotoImage
from PIL import ImageTk, Image
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys
import os
import queue  # Import the queue module


driver_queue = queue.Queue()

def login():
    try:
        # Set path to Microsoft Edge webdriver executable
        edge_driver_path = 'Z:\My_World\Creativity\edgedriver_win64'  # Replace with the actual path to the msedgedriver

        # Create a new EdgeOptions instance
        edge_options = webdriver.EdgeOptions()

        # Remove the --headless option to make the browser visible
        edge_options.add_argument('--headless')

        # Allow handling of alerts and pop-ups
        edge_options.set_capability("ms:edgeOptions", {"w3c": False})

        # Create a new Edge driver with the EdgeOptions
        driver = webdriver.Edge(service=Service(edge_driver_path), options=edge_options)

        # Open the login page in the browser
        login_url = 'https://internet.lpu.in/24online/webpages/client.jsp'
        driver.get(login_url)

        # Handle the pop-up automatically
        try:
            alert = driver.switch_to.alert
            alert.accept()
        except:
            pass

        # Get the ID and password from the user
        username = entry_id.get()   # Replace with the actual default username
        password = entry_pass.get()   # Replace with the actual default password

        # Wait for the username input field to be visible
        username_input = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.NAME, 'username'))
        )

        # Enter the username and password
        username_input.send_keys(username)
        password_input = driver.find_element(By.NAME, 'password')
        password_input.send_keys(password)

        checkbox = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, 'agreepolicy'))
        )

         # Scroll the checkbox into view
        driver.execute_script("arguments[0].scrollIntoView();", checkbox)
        time.sleep(2)  # Add a small delay to allow scrolling to complete

        # Click the checkbox
        checkbox.click()

        # Wait for the login button to be clickable
        login_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//button[@id="loginbtn"]'))
        )

        # Scroll the login button into view
        driver.execute_script("arguments[0].scrollIntoView();", login_button)

        # Click the login button
        login_button.click()

        print('Login successful')

        # Save the driver object in the queue
        driver_queue.put(driver)

    except Exception as e:
        messagebox.showerror('Error', f'An error occurred during login: {str(e)}')
        # Close the browser and end the script
        driver.quit()

def handle_logout():
    try:
        # Retrieve the driver object from the queue
        driver = driver_queue.get()

        # Find and click the Logout button
        logout_button = driver.find_element(By.XPATH, '//input[@name="logout"]')
        logout_button.click()

        print('Logout successful')

        # Close the browser
        driver.quit()

        # Enable the Login button
        login_button.config(state=tk.NORMAL)

    except Exception as e:
        messagebox.showerror('Error', f'An error occurred during logout: {str(e)}')


def handle_login():
    # Disable the Login button
    login_button.config(state=tk.DISABLED)

    # Start the login process in a separate thread
    login_thread = threading.Thread(target=login_task)
    login_thread.start()

def login_task():
    # Perform login operation
    login()

    # Enable the Logout button
    logout_button.config(state=tk.NORMAL)

    # Update the Logout button state on the main thread
    window.after(0, update_logout_button_state)

def update_logout_button_state():
    # Schedule GUI update on main thread
    logout_button.config(state=tk.NORMAL)

# Create the main window
window = tk.Tk()
window.title('Login')
window.geometry('400x250')

# Set the background image
# Get the base directory of the executable (PyInstaller)
try:
    base_dir = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))

# Construct the absolute path to the image file 
    image_path = os.path.join(base_dir, "Z:\My_World\Wifi_APP/Blacky_1.jpg")
    background_image = ImageTk.PhotoImage(Image.open("Z:\My_World\Wifi_APP/Blacky_1.jpg"))
except FileNotFoundError:
    print("Error: 'Blacky_1.jpg' not found. Check the file path.")
background_label = tk.Label(window, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create the ID label and entry
label_id = tk.Label(window, text="ID:")
label_id.place(x=50, y=50)
entry_id = ttk.Entry(window)
entry_id.place(x=150, y=50)

# Create the Password label and entry
label_pass = tk.Label(window, text="Password:")
label_pass.place(x=50, y=100)
entry_pass = ttk.Entry(window, show="*")
entry_pass.place(x=150, y=100)
# Create the Login button
login_button = tk.Button(window, text='Login', command=handle_login)
login_button.place(x=50, y=150)

# Create the Logout button
logout_button = tk.Button(window, text='Logout', state=tk.DISABLED, command=handle_logout)
logout_button.place(x=150, y=150)

# Start the GUI event loop
window.mainloop()
