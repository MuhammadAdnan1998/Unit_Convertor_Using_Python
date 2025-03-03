# Importing Libraries
import streamlit as st
from pint import UnitRegistry
# streamlit is a Python library for creating web apps easily.
# pint is a library used for unit conversions.

# Streamlit page configuration
st.set_page_config(page_title="Unit Converter", page_icon="🔄", layout="centered")
# set_page_config() sets up the Streamlit app's page.
# page_title="Unit Converter" sets the browser tab title.
# page_icon="🔄" adds a refresh emoji as the favicon.
# layout="centered" centers the app layout.

# Main Function
def main():
    # Defines the main() function where the app's logic is implemented.

    # Custom Styling
    st.markdown(
        """
        <style>
            body {
                background-color: #f4f4f4;
                font-family: Arial, sans-serif;
            }
            .stApp {
                max-width: 600px;
                margin: auto;
                padding: 20px;
                background: white;
                border-radius: 10px;
                box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
            }
            .stTitle {
                color: #2E3B55;
                text-align: center;
            }
        </style>
        """,
        unsafe_allow_html=True
    )
    # Uses Markdown to inject custom CSS styling.
    # Sets a light gray background for the entire page.
    # Centers the app inside a white box with rounded corners and a shadow.
    # Defines a .stTitle class for styling titles.


    st.title("🔄Unit Converter(Length, Mass, Time)")
    # st.title() sets the main heading of the app.
    
    st.markdown("<h3 style='text-align: center; color: gray;'>This is a simple unit converter app using streamlit and pint libraries.</h3>", unsafe_allow_html=True)
    # Uses HTML inside Markdown to display a centered subtitle in gray.
    # unsafe_allow_html=True allows direct HTML usage.

    # Unit Registry
    ureg = UnitRegistry()
    # Creates an instance of UnitRegistry, which helps in handling units and conversions.

    # Select conversion category
    category = st.selectbox("Select Category", ["Length", "Mass", "Time"])
    # st.selectbox() creates a dropdown menu with three categories: Length, Mass, and Time.
    # The selected category is stored in the category variable.

    # Defining Available Units
    if category == "Length":
        units = ["meter", "kilometer", "centimeter", "millimeter", "micrometer", "nanometer", "mile", "yard", "foot", "inch"]
    elif category == "Mass":
        units = ["kilogram", "gram", "milligram", "microgram", "ton", "pound", "ounce"]
    elif category == "Time":
        units = ["second", "minute", "hour", "day", "week", "year"]
    # Depending on the selected category, a list of units is assigned to the units variable.

    # Taking User Input
    input_value = st.number_input("Enter Value", min_value=0.0, value=1.0)
    # st.number_input() creates a numeric input box where the user enters a value to convert.
    # min_value=0.0 ensures only positive values are entered.
    # value=1.0 sets a default value of 1.0.

    from_unit = st.selectbox("From Unit", units)
    to_unit = st.selectbox("To Unit", units)
    # Creates dropdown menus to select the units for conversion.
    # from_unit: The unit the user wants to convert from.
    # to_unit: The unit the user wants to convert to.

    # Performing Unit Conversion
    try:
        converted_value = (input_value * ureg(from_unit)).to(to_unit)
        # Uses the pint library to convert the value from from_unit to to_unit.
        # (input_value * ureg(from_unit)) creates a quantity object.
        # .to(to_unit) converts it to the target unit.

        # Displaying Results
        st.success(f"✅{input_value} {from_unit} = {converted_value.magnitude:4f} {to_unit}")
        # Displays the conversion result in a formatted string.
        # .magnitude extracts the numeric value from the converted unit.
        # .4f ensures the output is displayed with four decimal places.

    # Handling Errors
    except Exception as e:
        st.error(f"❌Error in conversion: {e}")
        # If an error occurs (e.g., invalid conversion), it catches the error and displays it.

# Running the App
if __name__ == "__main__":
    main()
    # Ensures that the main() function runs when the script is executed.