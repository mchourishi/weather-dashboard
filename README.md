# Weather Dashboard

A simple weather dashboard application built with Flask that allows users to check the current weather information for various locations.

## Features

- Fetches weather data from an external weather API
- User-friendly interface to input location
- Displays current temperature, weather conditions, and more

## Requirements

- Python 3.x
- Flask
- Requests

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/mchourishi/weather-dashboard.git
   cd weather-dashboard
   ```

2. **Set up a virtual environment (optional but recommended):**

   ```
   python -m venv venv
   ```

3. **Set up a virtual environment (optional but recommended):**

   ```
   python -m venv venv
   ```

   - Activate the virtual environment:

     - On Windows: `venv\Scripts\activate`
     - On Linux: `source venv/bin/activate`

4. **Install the required packages:**

   ```
   pip install -r requirements.txt
   ```

5. **Set up environment variables:**

   Rename .env copy to .env and replace <YOUR_OPEN_WEATHER_MAP_API_KEY> with Open Weather API Key

## Running the Application

To run the application, use the following command:

```
python app.py
```

The application will start and can be accessed in your web browser at http://127.0.0.1:5001/.

## Usage

- Open your web browser and go to http://127.0.0.1:5001/.
- Enter the location for which you want to check the weather.
- Click the "Get Weather" button to retrieve the weather information.

## Contributing

Contributions are welcome! If you have suggestions or improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

- Flask - A micro web framework for Python
- Requests - A simple HTTP library for Python
- Weather API - The weather data provider
