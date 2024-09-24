import pickle
import streamlit as st
import streamlit_float as sts
from streamlit_card import card 
model=pickle.load(open("weather.pkl","rb"))
st.title("    Weather Predicition")
st.write(" ")

temp=st.number_input("Enter The Temperature")
hum=st.number_input("Enter The Humidity")
windspeed=st.number_input("Enter The Windspeeed")
submit=st.button("Submit")
if submit:
    op=model.predict([[temp,hum,windspeed]])
    st.write("The current climate of your area is:  ")
    if op[0]==0:
        st.write("clear")
    elif op[0]==1:
        st.write("cloudy")
    elif op[0]==2:
        st.write ("drizzle")
    elif op[0]==3:
        st.write ("drizzle,fog")
    elif op[0]==4:
        st.write ("drizzle,ice pellet,fog")
    elif op[0]==5:
        st.write ( "drizzle,snow" )
    elif op[0]==6:
        st.write ( "drizzle,snow,fog" )
    elif op[0]==7:
        st.write ( "Fog" )
    elif op[0]==8:
        st.write ( "freezing drizzle" )
    elif op[0]==9:
        st.write ( "fog,freezing drizzle" )
    elif op[0]==10:
        st.write ( "haze,freezing drizzle" )
    elif op[0]==11:
        st.write ( "snow,freezing drizzle" )
    elif op[0]==12:
        st.write ("freezing fog")
    elif op[0]==13:
        st.write ( "freezing rain" )
    elif op[0]==14:
        st.write ( "freezing rain,fog" )
    elif op[0]==15:
        st.write ( "freezing rain,haze" )
    elif op[0]==16:
        st.write ( "freezing rain,ice pellets,fog" )
    elif op[0]==17:
        st.write ("freezing rain,snow grains")
    elif op[0]==18:
        st.write ( "haze" )
    elif op[0]==19:
        st.write ( "mainly clear" )
    elif op[0]==20:
        st.write ( "moderate rain,fog" )
    elif op[0]==21:
        st.write ( "moderate snow" )
    elif op[0]==22:
        st.write ("moderate & blowing snow")
    elif op[0]==23:
        st.write ( "mostly cloudy" )
    elif op[0]==24:
        st.write ( "rain" )
    elif op[0]==25:
        st.write ( "rain shower" )
    elif op[0]==26:
        st.write ( "rain shower,fog" )
    elif op[0]==27:
        st.write ( "rain shower,snow showers" )
    elif op[0]==28:
        st.write ( "rain,fog" )
    elif op[0]==29:
        st.write ( "rain,haze" )
    elif op[0]==30:
       st.write ( "rain,ice pelletes" )
    elif op[0]==31:
        st.write ( "rain,snow" )
    elif op[0]==32:
        st.write ( "rain,snow grains" )
    elif op[0]==33:
        st.write ( "rain,snow,fog" )
    elif op[0]==34:
        st.write ( "rain,snow,ice pellets" )
    elif op[0]==35:
        pst.write ( "snow" )
    elif op[0]==36:
        st.write ( "snowpellets" )
    elif op[0]==37:
        st.write ( "snowshower" )
    elif op[0]==38:
        st.write ( "snowshower,fog" )
    elif op[0]==39:
        st.write ( "snow,blowing snow" )
    elif op[0]==40:
        st.write ( "snow,fog" )
    elif op[0]==41:
        st.write ( "snow,haze" )
    elif op[0]==42:
        st.write ( "snow,icepellets" )
    elif op[0]==43:
        st.write ( "thunderstroms" )
    elif op[0]==44:
        st.write ( "thunderstrom,heavyrainshower" )
    elif op[0]==45:
        st.write (  "thunderstroms,moderate")
    elif op[0]==46:
        st.write (  "thunderstroms,rain" )
    elif op[0]==47:
        st.write (  "thunderstroms,rainshower" )
    elif op[0]==48:
        st.write (  "thunderstroms,rain shower,fog" )
    elif op[0]==49:
        print (  "thunderstroms,rain,fog" )
card( 
    title="Dataset used!", 
    text="Click this card to redirect to Dataset website", 
    image="D:\Goutham\ML internship\weather forecast\cartoon-weather-prediction-for-today-are-vector-21580189.jpg", 
    url="https://www.kaggle.com/datasets/sujaykapadnis/weather-forecast-accuracy", 
) 
    