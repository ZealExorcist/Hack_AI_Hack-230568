from datetime import datetime # datetime is a library for working with dates and times
from uagents import Agent, Context # uagents is a library for creating agents
import requests # requests is a library for making HTTP requests
import tkinter as tk # tkinter is a library for creating GUIs
from tkinter import messagebox # messagebox is a library for displaying alerts


agent = Agent(name='weather', endpoint="http://127.0.0.1:8000", port=8000) # Create an agent

URL = "https://api.open-meteo.com/v1/forecast?" # URL of the API
# no API key needed

latitude = float(input("Enter latitude: "))
longitude = float(input("Enter longitude: "))
min_temp = float(input("Enter minimum temperature: "))
max_temp = float(input("Enter maximum temperature: "))

# Function to display an alert
def show_alert(message):
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    messagebox.showinfo("Notification", message)
    root.destroy()


def get_data(ctx, latitude, longitude) -> dict or None: # Function to get data from the API
    url = (
        URL
        + f"latitude={latitude}&longitude={longitude}"
        + "&hourly=temperature_2m&forecast_days=1"
    )
    current_date = datetime.utcnow().date().isoformat() # Get the current date
    cached_data = ctx.storage.get("last_request") # Get the last request from the storage of the agent (if any)
    data = requests.get(url).json() # Get the data from the API
    if cached_data:
        if data["date"] == current_date and data["url"] == url:
            return data["response"]

    response = requests.get(url=url, timeout=5) # Get the data from the API with a timeout of 5 seconds (in case the API is down)
    if response.status_code == 200:
        return data
    return None


@agent.on_interval(1800) # 30 minutes
async def query_data(ctx: Context): # Function to query the data from the API every 30 minutes
    data = get_data(ctx, latitude, longitude) 
    current_date = datetime.utcnow() 
    time = int(current_date.strftime("%H")) # Get the current time in hours 
    temp = data['hourly']['temperature_2m'][time] 
    message_to_display = f"Your local temperature at {time} is {temp}°C."
    if temp < min_temp or temp > max_temp:
        ctx.logger.info(message_to_display) # Log the message to the console of the agent
        if temp < min_temp:
            message_to_display += "Temperature is lower than the minimum" 
        elif temp > max_temp:
            message_to_display += "Temperature is higher than maximum"     
        show_alert(message_to_display) # Display an alert with the message

if __name__ == '__main__':
    agent.run() # Run the agent
