import numpy as np
import pandas as pd
import mysql.connector as c
from flask import Flask, request, render_template


class Drone:
    drone_name = 'Not Selected'
    flight_radius = 'Not Selected'
    flight_altitude = 'Not Selected'
    operations_per_head = 'Not Selected'
    flight_time = 'Not Selected'
    payload_capacity = 'Not Selected'
    flight_range = 'Not Selected'
    camera_quality = 'Not Selected'
    wind_resistance = 'Not Selected'
    noise_level = 'Not Selected'
    cost = 'Not Selected'
    data_storage = 'Not Selected'
    durability = 'Not Selected'
    weather_resistance = 'Not Selected'
    speed = 'Not Selected'


app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def get_requirements():
    # connecting the database and fetching the data:
    con = c.connect(host='localhost', user='root',
                    password='manas', database='drones')
    print('the database is conncted')
    cur = con.cursor()

    query = "SELECT * FROM tableName;"
    cur.execute(query)
    column_names = [column[0] for column in cur.description]
    rows = cur.fetchall()
    df = pd.DataFrame(rows, columns=column_names)
    cur.close()
    con.close()

    a1 = Drone()
    print(df)
    # taking input data from webpage
    if request.method == "POST":
        flight_radius = int(request.form["flightRadius"])
        print('flight radius')
        flight_altitude = int(request.form["flightAltitude"])
        print('flight altitude')
        operations_per_head = int(request.form["operationsPerHead"])
        print('operations per head')
        flight_time = int(request.form["flightTime"])
        print('flight time')
        payload_capacity = round(float(request.form["payloadCapacity"]), 2)
        print('payload capacity')
        flight_range = int(request.form["flightRange"])
        print('flight range')
        camera_quality = int(request.form["cameraQuality"])
        print('camera quality')
        wind_resistance = int(request.form["windResistance"])
        print('wind resistance')
        noise_level = int(request.form["noiseLevel"])
        print('noise level')
        cost = int(request.form["cost"])
        print('cost')
        data_storage = int(request.form["dataStorage"])
        print('data storage')
        durability = int(request.form["durability"])
        print('flight durability')
        weather_resistance = int(request.form["weatherResistance"])
        print('weather resistance')
        speed = int(request.form["speed"])
        print('speed')

        importanceLevel = [(request.form["importanceLevel1"]), (request.form["importanceLevel2"]), (request.form["importanceLevel3"]), (request.form["importanceLevel4"]), (request.form["importanceLevel5"]), (request.form["importanceLevel6"]), (request.form["importanceLevel7"]),
                           (request.form["importanceLevel8"]), (request.form["importanceLevel9"]), (request.form["importanceLevel10"]), (request.form["importanceLevel11"]), (request.form["importanceLevel12"]), (request.form["importanceLevel13"]), (request.form["importanceLevel14"])]

        inputs = {
            'Flight_Radius': flight_radius,
            'Flight_Altitude': flight_altitude,
            'Operations_Per_Head': operations_per_head,
            'Flight_Time': flight_time,
            'Payload_Capacity': payload_capacity,
            'flight_range': flight_range,
            'Camera_Quality': camera_quality,
            'Wind_Resistance': wind_resistance,
            'Noise_Level': noise_level,
            'Cost': cost,
            'Data_Storage': data_storage,
            'Durability': durability,
            'Weather_Resistance': weather_resistance,
            'Speed': speed,
        }

        # Define attribute weights
        attribute_weights = [0]*14
        # normalizing all the attribute values of each drone:
        # finding the min and max values:
        # min1=df['Flight Radius'].min()
        # max1=df['Flight Radius'].max()
        # # Normalizing value:
        # df.at[0,'Normalized Flight Radius']=((df['Flight Radius'].iloc[0]-min1)/max1-min1)*10

        df['Normalized Flight Radius'] = 0
        df['Normalized Flight Altitude'] = 0
        df['Normalized Operations per Head'] = 0
        df['Normalized Flight Time'] = 0
        df['Normalized Payload Capacity'] = 0
        df['Normalized Flight Range'] = 0
        df['Normalized Camera Quality'] = 0
        df['Normalized Wind Resistance'] = 0
        df['Normalized Noise Level'] = 0
        df['Normalized Cost'] = 0
        df['Normalized Data Storage'] = 0
        df['Normalized Durability'] = 0
        df['Normalized Weather Resistance'] = 0
        df['Normalized Speed'] = 0

        l = len(df)
        for x in range(0, l):
            # normalizing flight radius:
            min1 = df['flight_radius'].min()
            max1 = df['flight_radius'].max()
            # Normalizing value:
            df.at[x, 'Normalized Flight Radius'] = (
                (df['flight_radius'].iloc[x]-min1)/max1-min1)*10
            # if df['Normalized Flight Radius'].iloc[x] < 0:
            #     df.at[x, 'Normalized Flight Radius'] *= (-1)

            # normalizing flight altitude:
            min1 = df['flight_altitude'].min()
            max1 = df['flight_altitude'].max()
            # Normalizing value:
            df.at[x, 'Normalized Flight Altitude'] = (
                (df['flight_altitude'].iloc[x]-min1)/max1-min1)*10
            # if df['Normalized Flight Altitude'].iloc[x] < 0:
            #     df.at[x, 'Normalized Flight Altitude'] *= (-1)

            # normalizing operations per head:
            min1 = df['operations_per_head'].min()
            max1 = df['operations_per_head'].max()
            # Normalizing value:
            df.at[x, 'Normalized Operations per Head'] = (
                (df['operations_per_head'].iloc[x]-min1)/max1-min1)*10
            # if df['Normalized Operations per Head'].iloc[x] < 0:
            #     df.at[x, 'Normalized Operations per Head'] *= (-1)

            # normalizing flight time:
            min1 = df['flight_time'].min()
            max1 = df['flight_time'].max()
            # Normalizing value:
            df.at[x, 'Normalized Flight Time'] = (
                (df['flight_time'].iloc[x]-min1)/max1-min1)*10
            # if df['Normalized Flight Time'].iloc[x] < 0:
            #     df.at[x, 'Normalized Flight Time'] *= (-1)

            # normalizing payload capacity:
            min1 = df['payload_capacity'].min()
            max1 = df['payload_capacity'].max()
            # Normalizing value:
            df.at[x, 'Normalized Payload Capacity'] = (
                (df['payload_capacity'].iloc[x]-min1)/max1-min1)*10
            # if df['Normalized Payload Capacity'].iloc[x] < 0:
            #     df.at[x, 'Normalized Payload Capacity'] *= (-1)

            # normalizing flight_range:
            min1 = df['flight_range'].min()
            max1 = df['flight_range'].max()
            # Normalizing value:
            df.at[x, 'Normalized Flight Range'] = (
                (df['flight_range'].iloc[x]-min1)/max1-min1)*10
            # if df['Normalized Flight Range'].iloc[x] < 0:
            #     df.at[x, 'Normalized Flight Range'] *= (-1)

            # normalizing camera quality:
            min1 = df['camera_quality'].min()
            max1 = df['camera_quality'].max()
            # Normalizing value:
            df.at[x, 'Normalized Camera Quality'] = (
                (df['camera_quality'].iloc[x]-min1)/max1-min1)*10
            # if df['Normalized Camera Quality'].iloc[x] < 0:
            #     df.at[x, 'Normalized Camera Quality'] *= (-1)

            # normalizing Wind Resistance:
            min1 = df['wind_resistance'].min()
            max1 = df['wind_resistance'].max()
            # Normalizing value:
            df.at[x, 'Normalized Wind Resistance'] = (
                (df['wind_resistance'].iloc[x]-min1)/max1-min1)*10
            # if df['Normalized Wind Resistance'].iloc[x] < 0:
            #     df.at[x, 'Normalized Wind Resistance'] *= (-1)

            # normalizing Noise Level:
            min1 = df['noise_level'].min()
            max1 = df['noise_level'].max()
            # Normalizing value:
            df.at[x, 'Normalized Noise Level'] = (
                (df['noise_level'].iloc[x]-min1)/max1-min1)*10
            # if df['Normalized Noise Level'].iloc[x] < 0:
            #     df.at[x, 'Normalized Noise Level'] *= (-1)

            # normalizing Cost:
            min1 = df['cost'].min()
            max1 = df['cost'].max()
            # Normalizing value:
            df.at[x, 'Normalized Cost'] = (
                (df['cost'].iloc[x]-min1)/max1-min1)*10
            # if df['Normalized Cost'].iloc[x] < 0:
            #     df.at[x, 'Normalized Cost'] *= (-1)

            # normalizing Data flight_range:
            min1 = df['data_storage'].min()
            max1 = df['data_storage'].max()
            # Normalizing value:
            df.at[x, 'Normalized Data Storage'] = (
                (df['data_storage'].iloc[x]-min1)/max1-min1)*10
            # if df['Normalized Data Storage'].iloc[x] < 0:
            #     df.at[x, 'Normalized Data Storage'] *= (-1)

            # normalizing Cost:
            min1 = df['durability'].min()
            max1 = df['durability'].max()
            # Normalizing value:
            df.at[x, 'Normalized Durability'] = (
                (df['durability'].iloc[x]-min1)/max1-min1)*10
            # if df['Normalized Durability'].iloc[x] < 0:
            #     df.at[x, 'Normalized Durability'] *= (-1)

            # normalizing Weather Resistance:
            min1 = df['weather_resistance'].min()
            max1 = df['weather_resistance'].max()
            # Normalizing value:
            df.at[x, 'Normalized Weather Resistance'] = (
                (df['weather_resistance'].iloc[x]-min1)/max1-min1)*10
            # if df['Normalized Weather Resistance'].iloc[x] < 0:
            #     df.at[x, 'Normalized Weather Resistance'] *= (-1)

            # normalizing Speed:
            min1 = df['speed'].min()
            max1 = df['speed'].max()
            # Normalizing value:
            df.at[x, 'Normalized Speed'] = (
                (df['speed'].iloc[x]-min1)/max1-min1)*10
            # if df['Normalized Speed'].iloc[x] < 0:
            #     df.at[x, 'Normalized Speed'] *= (-1)

        print(df)

        # normalizing input values:
        # normalizing flight radius:
        min1 = df['flight_radius'].min()
        max1 = df['flight_radius'].max()
        # Normalizing value:
        flight_radius_n = ((flight_radius-min1)/max1-min1)*10

        # normalizing flight altitude:
        min1 = df['flight_altitude'].min()
        max1 = df['flight_altitude'].max()
        # Normalizing value:
        flight_altitude_n = ((flight_altitude-min1)/max1-min1)*10

        # normalizing operations per head:
        min1 = df['operations_per_head'].min()
        max1 = df['operations_per_head'].max()
        # Normalizing value:
        operations_per_head_n = ((operations_per_head-min1)/max1-min1)*10

        # normalizing flight time:
        min1 = df['flight_time'].min()
        max1 = df['flight_time'].max()
        # Normalizing value:
        flight_time_n = ((flight_time-min1)/max1-min1)*10

        # normalizing payload capacity:
        min1 = df['payload_capacity'].min()
        max1 = df['payload_capacity'].max()
        # Normalizing value:
        payload_capacity_n = ((payload_capacity-min1)/max1-min1)*10

        # normalizing flight_range:
        min1 = df['flight_range'].min()
        max1 = df['flight_range'].max()
        # Normalizing value:
        flight_range_n = ((flight_range-min1)/max1-min1)*10

        # normalizing camera quality:
        min1 = df['camera_quality'].min()
        max1 = df['camera_quality'].max()
        # Normalizing value:
        camera_quality_n = ((camera_quality-min1)/max1-min1)*10

        # normalizing Wind Resistance:
        min1 = df['wind_resistance'].min()
        max1 = df['wind_resistance'].max()
        # Normalizing value:
        wind_resistance_n = ((wind_resistance-min1)/max1-min1)*10

        # normalizing Noise Level:
        min1 = df['noise_level'].min()
        max1 = df['noise_level'].max()
        # Normalizing value:
        noise_level_n = ((noise_level-min1)/max1-min1)*10

        # normalizing Cost:
        min1 = df['cost'].min()
        max1 = df['cost'].max()
        # Normalizing value:
        cost_n = ((cost-min1)/max1-min1)*10

        # normalizing Data flight_range:
        min1 = df['data_storage'].min()
        max1 = df['data_storage'].max()
        # Normalizing value:
        data_storage_n = ((data_storage-min1)/max1-min1)*10

        # normalizing Cost:
        min1 = df['durability'].min()
        max1 = df['durability'].max()
        # Normalizing value:
        durability_n = ((durability-min1)/max1-min1)*10

        # normalizing Weather Resistance:
        min1 = df['weather_resistance'].min()
        max1 = df['weather_resistance'].max()
        # Normalizing value:
        weather_resistance_n = ((weather_resistance-min1)/max1-min1)*10

        # normalizing Speed:
        min1 = df['speed'].min()
        max1 = df['speed'].max()
        # Normalizing value:
        speed_n = ((speed-min1)/max1-min1)*10

        for i in range(0, 14):
            if (importanceLevel[i] == "very important"):
                importanceLevel[i] = 0.1
            elif (importanceLevel[i] == "important"):
                importanceLevel[i] = 0.5
            else:
                importanceLevel[i] = 0.9

        df['score'] = 0
        for x in range(0, l):
            # calculating the flight radius:
            y = (flight_radius_n-df['Normalized Flight Radius'].iloc[x])**2
            y = y**(1/2)
            if y < 0:
                y *= (-1)
            df.at[x, 'score'] += (y*importanceLevel[0])
            # calculating the flight altitude:
            y = (flight_altitude_n-df['Normalized Flight Altitude'].iloc[x])**2
            y = y**(1/2)
            if y < 0:
                y *= (-1)
            df.at[x, 'score'] += (y*importanceLevel[1])
            # calculating the flight altitude:
            y = (operations_per_head_n -
                 df['Normalized Operations per Head'].iloc[x])**2
            y = y**(1/2)
            if y < 0:
                y *= (-1)
            df.at[x, 'score'] += (y*importanceLevel[2])
            # calculating the flight time:
            y = (flight_time_n-df['Normalized Flight Time'].iloc[x])**2
            y = y**(1/2)
            if y < 0:
                y *= (-1)
            df.at[x, 'score'] += (y*importanceLevel[3])
            # calculating the payload capacity:
            y = (payload_capacity_n -
                 df['Normalized Payload Capacity'].iloc[x])**2
            y = y**(1/2)
            if y < 0:
                y *= (-1)
            df.at[x, 'score'] += (y*importanceLevel[4])
            # calculating the flight_range:
            y = (flight_range_n-df['Normalized Flight Range'].iloc[x])**2
            y = y**(1/2)
            if y < 0:
                y *= (-1)
            df.at[x, 'score'] += (y*importanceLevel[5])
            # calculating the camera quality:
            y = (camera_quality_n-df['Normalized Camera Quality'].iloc[x])**2
            y = y**(1/2)
            if y < 0:
                y *= (-1)
            df.at[x, 'score'] += (y*importanceLevel[6])
            # calculating the wind resistance:
            y = (wind_resistance_n-df['Normalized Wind Resistance'].iloc[x])**2
            y = y**(1/2)
            if y < 0:
                y *= (-1)
            df.at[x, 'score'] += (y*importanceLevel[7])
            # calculating the Noise Level:
            y = (noise_level_n-df['Normalized Noise Level'].iloc[x])**2
            y = y**(1/2)
            if y < 0:
                y *= (-1)
            df.at[x, 'score'] += (y*importanceLevel[8])
            # calculating the cost:
            y = (cost_n-df['Normalized Cost'].iloc[x])**2
            y = y**(1/2)
            if y < 0:
                y *= (-1)
            df.at[x, 'score'] += (y*importanceLevel[9])
            # calculating the data storage:
            y = (data_storage_n-df['Normalized Data Storage'].iloc[x])**2
            y = y**(1/2)
            if y < 0:
                y *= (-1)
            df.at[x, 'score'] += (y*importanceLevel[10])
            # calculating the durability:
            y = (durability_n-df['Normalized Durability'].iloc[x])**2
            y = y**(1/2)
            if y < 0:
                y *= (-1)
            df.at[x, 'score'] += (y*importanceLevel[11])
            # calculating the weather resistance:
            y = (weather_resistance_n -
                 df['Normalized Weather Resistance'].iloc[x])**2
            y = y**(1/2)
            if y < 0:
                y *= (-1)
            df.at[x, 'score'] += (y*importanceLevel[12])
            # calculating the Speed:
            y = (speed_n-df['Normalized Speed'].iloc[x])**2
            y = y**(1/2)
            if y < 0:
                y *= (-1)
            df.at[x, 'score'] += (y*importanceLevel[13])

        min_score = df['score'].min()
        selected_drone = df[df['score'] == min_score].iloc[0]

        print(selected_drone)

        a1.drone_name = selected_drone['Drone_Name']
        a1.flight_radius = selected_drone["flight_radius"]
        a1.flight_altitude = selected_drone["flight_altitude"]
        a1.operations_per_head = selected_drone["operations_per_head"]
        a1.flight_time = selected_drone["flight_time"]
        a1.payload_capacity = selected_drone["payload_capacity"]
        a1.flight_range = selected_drone["flight_range"]
        a1.camera_quality = selected_drone["camera_quality"]
        a1.wind_resistance = selected_drone["wind_resistance"]
        a1.noise_level = selected_drone["noise_level"]
        a1.cost = selected_drone["cost"]
        a1.data_storage = selected_drone["data_storage"]
        a1.durability = selected_drone["durability"]
        a1.weather_resistance = selected_drone["weather_resistance"]
        a1.speed = selected_drone["speed"]
        print(selected_drone)

    return render_template('index.html', a1=a1)


if __name__ == "__main__":
    app.run()
