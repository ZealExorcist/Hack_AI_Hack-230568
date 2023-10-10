
# Hack_AI_Hack-230568

This is a Temparature Alert Agent created in python, which alerts the user in a specified location, when in the is a change in the expexted temperature.

It allows the user to provide their location and and required temperature, and alerts the user when the temperature is above or below the required temperature.


## Libraries
There are multiple libraries used in this program along with uagents which are listed below:

datetime(using date and time)  
uagents(Agent, Context)                                 
requests  
tkinter(importing as tk)   
tkinter(using messagebox)
## API
The weather API used in this program is called Open-meteo, which is  an open-source weather API and offers free access for non-commercial use.
Since it an free access API, there is no key to access this API.

url=https://open-meteo.com/


## Agent

The agent used to communicate with the internet server to provide the accurate temperature of the given location

Name = weather 
endpoint=http://127.0.0.1:8000

## Compilation and running
During the compilation and running, pipenv must be done on the user end before.
The user enters their locations and their preferred maximun and minimum temperatures.

The program takes these values and connects API and then to the agent, after which the agent sends realtime value of the tempertaure to the user, and is notififed when there is an increase or decrease from the preferred temperatures.

NOTE:  
pipenv is a python virtual envoirment which allows its users to run their code.  

## User inputs
The user provides his location cordinates(latitude, longitide) as inputs, along with the maximum and minimum temperature he wants.

These values are stored in respective datatypes, depending on the required input type.

## Alert Notification
The main function of the program is to notify the user when there is an increase or decrease from the specified temperature.

So when there is an increase or decrease from the specified temperature, the user gets an alert notification,which notifies them regarding the change in temperature.
## Special Notes
We have recieved and used the program from:  
1.Agentverse by https://fetch.ai/   
2.Chatgpt
