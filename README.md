# Random City Explorer

## Overview
**Random City Explorer** is a Python-based application that selects a random city from a predefined list and provides information such as weather details and fun facts about the city. It retrieves weather data using the OpenWeatherMap API and city facts using the Wikipedia API.

This is another fun project by me. It's kinda useless lmao...

## Features
- **Random City Selection**: Explore a different city every time you run the program.
- **City Facts**: Provides interesting facts about the city from its Wikipedia page.
- **Weather Information**: Fetches real-time(yep, I'm serious) weather data for the selected city using OpenWeatherMap API.

## How It Works
1. The program selects a random city from a list of pre-defined cities.
2. It fetches a brief summary of the city from Wikipedia using the Wikipedia API.
3. The program retrieves real-time weather data for the selected city using the OpenWeatherMap API.
4. The user can explore multiple cities in a single session or quit at any time.

- You can also try it!!

  
## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Saharsh000/City-Explorer.git
   cd City-Explorer
   ```
2. **Install Dependencies**:
   Ensure you have Python installed. Install the required dependencies by running:
   ```bash
   pip install -r requirements.txt
   ```
3. **Get Your OpenWeatherMap API Key**:
  - Sign up for a free account at OpenWeatherMap.
  - Get your API key and replace `your_openweathermap_api_key` in the `city_explorer.py` file.

4. **Run the Program**: Start the program by running:
```bash
python city_explorer.py
```
## Dependencies

The project requires the following libraries:
- `requests`: To make API calls to Wikipedia and OpenWeatherMap.

You can install these dependencies with:

```bash
pip install -r requirements.txt
```
## Usage
1. Run the `city_explorer.py` script.
2. The program will select a random city from the list and display basic information and weather data.
3. After viewing the information, you'll have the option to explore another city or quit the program.

## APIs Used
**OpenWeatherMap**: Provides real-time weather data for any city in the world.
**Wikipedia API**: Fetches a brief summary of the selected city from its Wikipedia page.

## To Do(Updates)
- Add more cities to the list(doing this currently).
- Display additional information about the cities (e.g., population, time zone).
- Allow user input for cities.
- Save the explored cities' information to a text or CSV file.


## Thank You
- Well, thank you for using my code.
- As always, if you have any issues with the program, you can contact me on discord(metagross2010ss) or email me.
- Have a nice day :D !!!!

