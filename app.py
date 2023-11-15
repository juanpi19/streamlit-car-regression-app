import streamlit as st
import pickle
import pandas as pd
import numpy as np
from datetime import datetime
# Image Reading
from PIL import Image
#from streamlit_gsheets import GSheetsConnection
#from google_analytics import GoogleAnalytics



# Google Sheets Connection

# Google Analytics tracking code
google_analytics_code = """
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-528WH0B4V6"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-528WH0B4V6');
</script>
"""


#model = pickle.load(open('car_prediction_model_ols_v0.pkl','rb'))
image = Image.open('project_pic.jpg')

model_params = {'const': 32.71668536188933,
                'manufacturer': -0.09013379123620063,
                'condition': 0.09234686664940653,
                'cylinders': 1.1050918731940933,
                'fuel': -0.8954358887961962,
                'odometer': -0.020473041672087123,
                'title_status': -0.24787457267150187,
                'transmission': 0.2374010560521393,
                'VIN': 0.8129391733185263,
                'drive': -0.7255796847744701,
                'type': 0.010627998263776653,
                'paint_color': 0.026071629840995637,
                'state': -0.0031757478115481976,
                'is_expensive': 1.6781910560061322,
                'is_missing_cylinders': -3.6518457156973136,
                'is_missing_drive': 1.299968978312413,
                'is_missing_type': -0.17887046020062067,
                'car_age': -0.3637197826893971}



################################################ SLIDERS | SELECT BOXES | USER INPUT

manufacturer_selectbox = st.sidebar.selectbox("Manufacturer",
                                options= ['other',
                                          'ford',
                                          'chevrolet',
                                          'toyota',
                                          'honda',
                                          'jeep',
                                          'nissan',
                                          'ram',
                                          'gmc',
                                          'bmw',
                                          'dodge'])


condition_selectbox = st.sidebar.selectbox("Condition",
                                options= ['unknown', 'good', 'excellent', 'like new', 
                                          'fair', 'new', 'salvage'])


cylinders_selectbox = st.sidebar.selectbox("Cylinders",
                                options= ['unknown',
                                            '6 cylinders',
                                            '4 cylinders',
                                            '8 cylinders',
                                            '5 cylinders',
                                            '10 cylinders',
                                            'other',
                                            '3 cylinders',
                                            '12 cylinders']
                                            )


fuel_selectbox = st.sidebar.selectbox("Fuel",
                                options= ['gas', 'other', 'diesel', 'hybrid', 'electric']
                                            )

title_status_selectbox = st.sidebar.selectbox("Title Status",
                                options= ['clean', 'rebuilt', 'unknown', 'salvage', 
                                          'lien', 'missing', 'parts only']
                                            )

transmission_selectbox = st.sidebar.selectbox("Transmission",
                                options= ['automatic', 'other', 'manual']
                                            )

vin_selectbox = st.sidebar.selectbox("VIN",
                                options= ['known', 'unknown']
                                            )

drive_selectbox = st.sidebar.selectbox("Drive",
                                options= ['4wd', 'unknown', 'fwd', 'rwd']
                                            )

type_selectbox = st.sidebar.selectbox("Type",
                                options= ['unknown',
                                        'sedan',
                                        'SUV',
                                        'pickup',
                                        'truck',
                                        'other',
                                        'coupe',
                                        'hatchback',
                                        'wagon',
                                        'van',
                                        'convertible',
                                        'mini-van',
                                        'offroad',
                                        'bus']
                                            )


paint_color_selectbox = st.sidebar.selectbox("Color",
                                options= ['unknown',
                                        'white',
                                        'black',
                                        'silver',
                                        'blue',
                                        'red',
                                        'grey',
                                        'green',
                                        'brown',
                                        'custom',
                                        'orange',
                                        'yellow',
                                        'purple']
                                            )

state_color_selectbox = st.sidebar.selectbox("State",
                                options= ['ca', 'fl','tx','ny','oh','or','mi','nc','wa','pa',
                                        'wi','tn','co','va','il','nj','id','az','ia','ma',
                                        'mn','ga','ok','sc','ks','mt','in','ct','al','md','nm',
                                        'mo','ky','ar','ak','la','nv','nh','dc','me','hi','vt',
                                        'ri','sd','ut','wv','ms','ne','de','wy','nd']
                                            )

year_slider = st.sidebar.select_slider("Year",
                                    options= range(1970, 2024),
                                    value=2020 )

odometer_text_input = st.sidebar.text_input("Odometer", 100000)

################################################


################################################ 



####### Manufacturer
if manufacturer_selectbox == 'other':
    manufacturer_pred = 8
elif manufacturer_selectbox == 'ford':
    manufacturer_pred = 3
elif manufacturer_selectbox == 'chevrolet':
    manufacturer_pred = 1
elif manufacturer_selectbox == 'toyota':
    manufacturer_pred = 10
elif manufacturer_selectbox == 'honda':
    manufacturer_pred = 5
elif manufacturer_selectbox == 'jeep':
    manufacturer_pred = 6
elif manufacturer_selectbox == 'nissan':
    manufacturer_pred = 7
elif manufacturer_selectbox == 'ram':
    manufacturer_pred = 9
elif manufacturer_selectbox == 'gmc':
    manufacturer_pred = 4
elif manufacturer_selectbox == 'bmw':
    manufacturer_pred = 0
elif manufacturer_selectbox == 'dodge':
    manufacturer_pred = 2


######### Condition

if condition_selectbox == 'unknown':
    condition_pred = 6
elif condition_selectbox == 'good':
    condition_pred = 2
elif condition_selectbox == 'excellent':
    condition_pred = 0
elif condition_selectbox == 'like new':
    condition_pred = 3
elif condition_selectbox == 'fair':
    condition_pred = 1
elif condition_selectbox == 'new':
    condition_pred = 4
elif condition_selectbox == 'salvage':
    condition_pred = 5


######### Cylinder

if cylinders_selectbox == 'unknown':
    cylinders_pred = 8
elif cylinders_selectbox == '6 cylinders':
    cylinders_pred = 5
elif cylinders_selectbox == '4 cylinders':
    cylinders_pred = 3
elif cylinders_selectbox == '8 cylinders':
    cylinders_pred = 6
elif cylinders_selectbox == '5 cylinders':
    cylinders_pred = 4
elif cylinders_selectbox == '10 cylinders':
    cylinders_pred = 0
elif cylinders_selectbox == 'other':
    cylinders_pred = 7
elif cylinders_selectbox == '3 cylinders':
    cylinders_pred = 3
elif cylinders_selectbox == '12 cylinders':
    cylinders_pred = 1

######### Fuel

if fuel_selectbox == 'gas':
    fuel_pred = 2
elif fuel_selectbox == 'other':
    fuel_pred = 4
elif fuel_selectbox == 'diesel':
    fuel_pred = 0
elif fuel_selectbox == 'hybrid':
    fuel_pred = 3
elif fuel_selectbox == 'electric':
    fuel_pred = 1


######### Title Status

if title_status_selectbox == 'clean':
    title_status_pred = 0
elif title_status_selectbox == 'rebuilt':
    title_status_pred = 4
elif title_status_selectbox == 'unknown':  #######
    title_status_pred = 6
elif title_status_selectbox == 'salvage':
    title_status_pred = 5
elif title_status_selectbox == 'lien':
    title_status_pred = 1
elif title_status_selectbox == 'missing':
    title_status_pred = 2
elif title_status_selectbox == 'parts only':
    title_status_pred = 3


######### Transmission

if transmission_selectbox == 'automatic':
    transmission_pred = 0
elif transmission_selectbox == 'other':
    transmission_pred = 2
elif transmission_selectbox == 'manual':
    transmission_pred = 1


######### VIN
                  
if vin_selectbox == 'known':
    vin_pred = 1
elif vin_selectbox == 'unknown':
    vin_pred = 0


########## Drive

if drive_selectbox == '4wd':
    drive_pred = 0
elif drive_selectbox == 'unknown':
    drive_pred = 3
elif drive_selectbox == 'fwd':
    drive_pred = 1
elif drive_selectbox == 'rwd':
    drive_pred = 2

########## Type


if type_selectbox == 'unknown':
    type_pred = 11
elif type_selectbox == 'sedan':
    type_pred = 9
elif type_selectbox == 'SUV':
    type_pred = 0
elif type_selectbox == 'pickup':
    type_pred = 8
elif type_selectbox == 'truck':
    type_pred = 10
elif type_selectbox == 'other':
    type_pred = 7
elif type_selectbox == 'coupe':
    type_pred = 3
elif type_selectbox == 'hatchback':
    type_pred = 4
elif type_selectbox == 'wagon':
    type_pred = 13
elif type_selectbox == 'van':
    type_pred = 12
elif type_selectbox == 'convertible':
    type_pred = 2
elif type_selectbox == 'mini-van':
    type_pred = 5
elif type_selectbox == 'offroad':
    type_pred = 6
elif type_selectbox == 'bus':
    type_pred = 1



########## Color

if paint_color_selectbox == 'unknown':
    paint_color_pred = 10
elif paint_color_selectbox == 'white':
    paint_color_pred = 11
elif paint_color_selectbox == 'black':
    paint_color_pred = 0
elif paint_color_selectbox == 'silver':
    paint_color_pred = 9
elif paint_color_selectbox == 'blue':
    paint_color_pred = 1
elif paint_color_selectbox == 'red':
    paint_color_pred = 8
elif paint_color_selectbox == 'grey':
    paint_color_pred = 5
elif paint_color_selectbox == 'green':
    paint_color_pred = 4
elif paint_color_selectbox == 'brown':
    paint_color_pred = 2
elif paint_color_selectbox == 'custom':
    paint_color_pred = 3
elif paint_color_selectbox == 'orange':
    paint_color_pred = 6
elif paint_color_selectbox == 'yellow':
    paint_color_pred = 12
elif paint_color_selectbox == 'purple':
    paint_color_pred = 7


########## State

if state_color_selectbox == 'ca':
    state_pred = 4
elif state_color_selectbox == 'fl':
    state_pred = 9
elif state_color_selectbox == 'tx':
    state_pred = 43
elif state_color_selectbox == 'ny':
    state_pred = 34
elif state_color_selectbox == 'oh':
    state_pred = 35
elif state_color_selectbox == 'or':
    state_pred = 37
elif state_color_selectbox == 'mi':
    state_pred = 22
elif state_color_selectbox == 'nc':
    state_pred = 27
elif state_color_selectbox == 'wa':
    state_pred = 47
elif state_color_selectbox == 'pa':
    state_pred = 38
elif state_color_selectbox == 'wi':
    state_pred = 48
elif state_color_selectbox == 'tn':
    state_pred = 42
elif state_color_selectbox == 'co':
    state_pred = 5
elif state_color_selectbox == 'va':
    state_pred = 45
elif state_color_selectbox == 'il':
    state_pred = 14
elif state_color_selectbox == 'nj':
    state_pred = 31
elif state_color_selectbox == 'id':
    state_pred = 13
elif state_color_selectbox == 'az':
    state_pred = 3
elif state_color_selectbox == 'ia':
    state_pred = 12
elif state_color_selectbox == 'ma':
    state_pred = 19
elif state_color_selectbox == 'mn':
    state_pred = 23
elif state_color_selectbox == 'ga':
    state_pred = 10
elif state_color_selectbox == 'ok':
    state_pred = 36
elif state_color_selectbox == 'sc':
    state_pred = 40
elif state_color_selectbox == 'ks':
    state_pred = 16
elif state_color_selectbox == 'mt':
    state_pred = 26
elif state_color_selectbox == 'in':
    state_pred = 15
elif state_color_selectbox == 'ct':
    state_pred = 6
elif state_color_selectbox == 'al':
    state_pred = 1
elif state_color_selectbox == 'md':
    state_pred = 20
elif state_color_selectbox == 'nm':
    state_pred = 32
elif state_color_selectbox == 'mo':
    state_pred = 24
elif state_color_selectbox == 'ky':
    state_pred = 17
elif state_color_selectbox == 'ar':
    state_pred = 2
elif state_color_selectbox == 'ak':
    state_pred = 0
elif state_color_selectbox == 'la':
    state_pred = 18
elif state_color_selectbox == 'nv':
    state_pred = 33
elif state_color_selectbox == 'nh':
    state_pred = 30
elif state_color_selectbox == 'dc':
    state_pred = 7
elif state_color_selectbox == 'me':
    state_pred = 21
elif state_color_selectbox == 'hi':
    state_pred = 11
elif state_color_selectbox == 'vt':
    state_pred = 46
elif state_color_selectbox == 'ri':
    state_pred = 39
elif state_color_selectbox == 'sd':
    state_pred = 41
elif state_color_selectbox == 'ut':
    state_pred = 44
elif state_color_selectbox == 'wv':
    state_pred = 49
elif state_color_selectbox == 'ms':
    state_pred = 25
elif state_color_selectbox == 'ne':
    state_pred = 29
elif state_color_selectbox == 'de':
    state_pred = 8
elif state_color_selectbox == 'wy':
    state_pred = 50
elif state_color_selectbox == 'nd':
    state_pred = 28


########## Year
car_age_pred = 2023  - int(year_slider)

########## Odometer

# Box-Cox transformation: (x^lambda - 1) / lambda
lambda_odometer = 0.41146181711823154
odometer_converted_pred = (int(odometer_text_input)**lambda_odometer - 1) / lambda_odometer # applying conversion because that is how the model was trained
#odometer_pred = int(odometer_text_input)

########## is_expensive
top_expensive_cars_list = ['ferrari','aston-martin','tesla','alfa-romeo','jaguar',
                            'porsche','ram','rover','audi','gmc']

if manufacturer_selectbox in top_expensive_cars_list:
    is_expensive_pred = 1
else:
    is_expensive_pred = 0

########## is_missing_cylinders
if cylinders_selectbox == 'unknown':
    is_missing_cylinders_pred = 1
else:
    is_missing_cylinders_pred = 0

########## is_missing_drive
if drive_selectbox == 'unknown':
    is_missing_drive_pred = 1
else:
    is_missing_drive_pred = 0

########## is_missing_type
if type_selectbox == 'unknown':
    is_missing_type_pred = 1
else:
    is_missing_type_pred = 0


########################################################################################
################################### PREDICTION FUNCTION #################################
#########################################################################################

def predict_car_price(manufacturer, condition, cylinders, fuel, odometer, title_status, transmission, VIN, 
                      drive, type, paint_color, state, is_expensive, is_missing_cylinders, is_missing_drive,
                    is_missing_type, car_age):
    

    '''This function takes all the parameters to make predictions using the trained model'''
    const = 1.0

    input_parameter = [const, manufacturer, condition, cylinders, fuel, odometer, title_status, transmission, VIN, 
                      drive, type, paint_color, state, is_expensive, is_missing_cylinders, is_missing_drive,
                      is_missing_type, car_age]

    #prediction = model.predict(input_parameter)

    prediction = sum(value * input_value for value, input_value in zip(model_params.values(), input_parameter))

    return prediction


st.title("Estimate Your Car's Price")
st.caption('Update all the information on the left sidebar and then press "Estimate"')
#st.header("", divider='gray')


# Every form must have a submit button.
# Create a button
if st.button('Estimate'):

    # new_data_sheet = pd.DataFrame({'Date': datetime.now(), 'Estimate Button Pressed': 'Yes'}, index=[1])

    # sheet.append(new_data_sheet, ignore_index=True)

    # st.write(sheet)

     # get prediction
    result = predict_car_price(manufacturer=manufacturer_pred, 
                            condition=condition_pred, 
                            cylinders=cylinders_pred, 
                            fuel=fuel_pred, 
                            odometer=odometer_converted_pred, 
                            title_status=title_status_pred, 
                            transmission=transmission_pred, 
                            VIN=vin_pred, 
                            drive=drive_pred, 
                            type=type_pred,
                            paint_color=paint_color_pred, 
                            state=state_pred, 
                            is_expensive=is_expensive_pred, 
                            is_missing_cylinders=is_missing_cylinders_pred, 
                            is_missing_drive=is_missing_drive_pred,
                            is_missing_type=is_missing_type_pred, 
                            car_age=car_age_pred)
    
    #st.write(result)
    

    # This result has been applied box-cox conversion so I need to revert the conversion
    # ((y * λ) + 1)^(1/λ)
    lambda_price = 0.18549405930233057
    result_reverted = ((result * lambda_price) + 1)**(1/lambda_price)

   #st.write(result_reverted)

    st.subheader(f'The estimated price of your car is ${round(result_reverted, 0)}!')

'''

'''

st.divider()
st.text("")



# """
# ####  | Estimate the Price of Your Car in Minutes
#  - This ML model and User Interface were developed by **Juan Herrera**
#     - **Code**
#         - [Model Source Code](https://github.com/juanpi19/regression-analysis-cars-dataset/blob/main/kaggle_cars_dataset_regression_analysis.pdf)
#         - [UI Source Code](https://github.com/juanpi19/streamlit-car-regression-app)

#     - **Let's Connect!**
#         - [Connect on LinkedIn](https://www.linkedin.com/in/juanherreras/)
#         - [GitHub](https://github.com/juanpi19)
#         - jjh80024@usc.edu
# """

st.subheader('About the Project')
st.markdown('''

- [ML Model Source Code](https://github.com/juanpi19/regression-analysis-cars-dataset/blob/main/kaggle_cars_dataset_regression_analysis.pdf)
- [Streamlit App Source Code](https://github.com/juanpi19/streamlit-car-regression-app)
''')

st.markdown("**Let's Collaborate!**")

st.markdown('''

- [Connect on LinkedIn](https://www.linkedin.com/in/juanherreras/)
- [GitHub](https://github.com/juanpi19)
- jjh80024@usc.edu
''')

st.text("")
st.text("")

# Displaying Project Process Picture
st.image(image)
