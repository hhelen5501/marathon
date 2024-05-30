import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Constants
MARATHON_DISTANCE = 42.195  # Marathon distance in kilometers
MAX_TIME_HOURS = 6.5  # Maximum allowed time in hours

# Sidebar configuration
st.sidebar.header("Marathon Time Calculator")
running_distance = st.sidebar.slider('Running Distance (km)', min_value=0.0, max_value=MARATHON_DISTANCE, value=21.0,
                                     step=0.1)
running_pace = st.sidebar.slider('Running Pace (min/km)', min_value=1.0, max_value=20.0, value=6.0, step=0.1)
walking_speed = st.sidebar.slider('Walking Speed (km/h)', min_value=1.0, max_value=10.0, value=5.0, step=0.1)
target_time_hours = st.sidebar.slider('Target Completion Time (hours)', min_value=2.0, max_value=8.0, value=6.5,
                                      step=0.1)

st.write("## Marathon Completion Time")

# Calculations for time spent running and walking
running_time_hours = (running_distance * running_pace) / 60  # Convert minutes to hours
walking_distance = MARATHON_DISTANCE - running_distance
walking_time_hours = walking_distance / walking_speed
total_time_hours = running_time_hours + walking_time_hours
total_time_minutes = total_time_hours * 60

cols = st.columns(2)
with cols[0]:
    st.metric(label="Total Running Time", value=f"{running_time_hours:.2f} hours")
    st.metric(label="Estimated Total Completion Time", value=f"{total_time_hours:.2f} hours")

with cols[1]:
    st.metric(label="Total Walking Time", value=f"{walking_time_hours:.2f} hours")
    st.metric(label="Estimated Total Completion Time", value=f"{total_time_minutes:.0f} minutes")

# Plotting total distance over time
times = np.linspace(0, total_time_hours, num=500)  # Sample times from start to finish
distance_over_time = np.where(times <= running_time_hours,
                              times * (running_distance / running_time_hours),  # Running distance formula
                              running_distance + (
                                      times - running_time_hours) * walking_speed)  # Walking distance formula

fig2, ax2 = plt.subplots()
ax2.plot(times * 60, distance_over_time)  # Convert hours to minutes for the x-axis
ax2.axvline(x=MAX_TIME_HOURS * 60, color='red', label='Maximum Allowed Time (6.5 hours)',
            linestyle='--')  # Max time line
ax2.set_title("Total Distance Over Time")
ax2.set_xlabel("Time (minutes)")
ax2.set_ylabel("Distance (km)")
ax2.legend()
st.pyplot(fig2)

# Display results
# Display results using st.metri

# Calculations keeping use supplied paces and target time

velocity_running_km_h = 1 / running_pace * 60
velocity_walking_km_h = walking_speed

if velocity_walking_km_h != velocity_running_km_h:
    st.write("## Necessary Running Time")
    st.write(f"At the provided paces {running_pace} min/km for running and walking {velocity_walking_km_h} km/h \nthis is the required time running that you need")
    time_walking = (MARATHON_DISTANCE - velocity_running_km_h * target_time_hours) / (
                velocity_walking_km_h - velocity_running_km_h)
    time_running = target_time_hours - time_walking

    distance_running = time_running * velocity_running_km_h
    distance_walking = time_walking * velocity_walking_km_h

    st.write(f"### To meet the target time of {target_time_hours} hours:")

    cols = st.columns(2)
    with cols[0]:
        st.metric(label="Necessary Running Distance", value=f"{distance_running:.2f} km")
        st.metric(label="Necessary Running Time", value=f"{time_running:.2f} h")

    with cols[1]:
        st.metric(label="Necessary Walking Distance", value=f"{distance_walking:.2f} km")
        st.metric(label="Necessary Walking Time", value=f"{time_walking:.2f} h")
