# Preface here
#
import Licenses.licensefile as licensefile
license_file = licensefile.license_file
filename = 'eye_tracking_expiriment\data\\'+'gaze_data80.csv'# "data/gaze_data3.csv" # you have to create the csv file beforehand.

# from psychopy import prefs, visual, core, event, monitors, tools, logging
import numpy as np
import tobii_research as tr
import time
import random
import os
import pylsl as lsl
import sys
import csv
import pandas as pd
import tkinter as tk
def read_text(filen):
    with open(filen, 'r') as file:
        return file.read()

Sequence = ['eye_tracking_expiriment\start.txt',
'eye_tracking_expiriment\Ai_HC_P01_text.txt','eye_tracking_expiriment\Ai_HC_P01_MCQ.txt','eye_tracking_expiriment\Ai_HC_P01_FIBQ.txt',
'eye_tracking_expiriment\Ai_HC_P02_text.txt','eye_tracking_expiriment\Ai_HC_P02_MCQ.txt','eye_tracking_expiriment\Ai_HC_P02_FIBQ.txt',
'eye_tracking_expiriment\Ai_HC_P03_text.txt','eye_tracking_expiriment\Ai_HC_P03_MCQ.txt','eye_tracking_expiriment\Ai_HC_P03_FIBQ.txt',
'eye_tracking_expiriment\Ai_HC_P04_text.txt','eye_tracking_expiriment\Ai_HC_P04_MCQ.txt','eye_tracking_expiriment\Ai_HC_P04_FIBQ.txt',
'eye_tracking_expiriment\Ai_HC_P05_text.txt','eye_tracking_expiriment\Ai_HC_P05_MCQ.txt','eye_tracking_expiriment\Ai_HC_P05_FIBQ.txt',
'eye_tracking_expiriment\Ai_HC_P06_text.txt','eye_tracking_expiriment\Ai_HC_P06_MCQ.txt','eye_tracking_expiriment\Ai_HC_P06_FIBQ.txt',
]
texts=[]

for file in Sequence:
    texts.append(read_text(file))

# Setting the font and size
font_size=[20]
font_family=['Arial']

current_text_index = 0


root = tk.Tk()
root.title('Text display')
#root.geometry('1600x1200')
root.attributes('-fullscreen', True)
root.resizable(width=False, height=False)

def close_window(event=None):
    global current_text_index
    current_text_index = 999 #pga shutdown
    root.destroy()

# Create the text widget

canvas = tk.Canvas(root, width=1600, height=1200)
canvas.pack()


# Start position for the text

x_position = 50
y_position = 100

def draw_text():
    global current_text_index
    canvas.delete('all')
    canvas.create_text(x_position, y_position, text=texts[current_text_index], font=(font_family[0], font_size[0]), anchor='nw')
    canvas.update()


draw_text()

def navigate_text(event):
    global current_text_index
    if event.keysym == 'Right':
        if current_text_index < len(texts) - 1:
            current_text_index += 1
            draw_text()
    elif event.keysym == 'Left':
        if current_text_index > 1:
            current_text_index -= 1
            draw_text()



def save_gaze_data_to_csv(gaze_data, filename):
    #print(gaze_data[0])
    print("GD LEN:",len(gaze_data))
    try:
        with open(filename, mode='w', newline='') as csv_file:
            fieldnames = [
                'device_time_stamp',
                'left_gaze_origin_validity',
                'right_gaze_origin_validity',
                'left_gaze_origin_in_user_x',
                'left_gaze_origin_in_user_y',
                'left_gaze_origin_in_user_z',
                'right_gaze_origin_in_user_x',
                'right_gaze_origin_in_user_y',
                'right_gaze_origin_in_user_z',
                'left_gaze_origin_in_trackbox_x',
                'left_gaze_origin_in_trackbox_y',
                'left_gaze_origin_in_trackbox_z',
                'right_gaze_origin_in_trackbox_x',
                'right_gaze_origin_in_trackbox_y',
                'right_gaze_origin_in_trackbox_z',
                'left_gaze_point_validity',
                'right_gaze_point_validity',
                'left_gaze_point_in_user_x',
                'left_gaze_point_in_user_y',
                'left_gaze_point_in_user_z',
                'right_gaze_point_in_user_x',
                'right_gaze_point_in_user_y',
                'right_gaze_point_in_user_z',
                'left_gaze_point_on_display_area_x',
                'left_gaze_point_on_display_area_y',
                'right_gaze_point_on_display_area_x',
                'right_gaze_point_on_display_area_y',
                'left_pupil_validity',
                'right_pupil_validity',
                'left_pupil_diameter',
                'right_pupil_diameter',

            ]

            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()

            for data in gaze_data:
                row = {
                    'device_time_stamp': data[0],
                    'left_gaze_origin_validity': data[1],
                    'right_gaze_origin_validity': data[2],
                    'left_gaze_origin_in_user_x': data[3],
                    'left_gaze_origin_in_user_y': data[4],
                    'left_gaze_origin_in_user_z': data[5],
                    'right_gaze_origin_in_user_x': data[6],
                    'right_gaze_origin_in_user_y': data[7],
                    'right_gaze_origin_in_user_z': data[8],
                    'left_gaze_origin_in_trackbox_x': data[9],
                    'left_gaze_origin_in_trackbox_y': data[10],
                    'left_gaze_origin_in_trackbox_z': data[11],
                    'right_gaze_origin_in_trackbox_x': data[12],
                    'right_gaze_origin_in_trackbox_y': data[13],
                    'right_gaze_origin_in_trackbox_z': data[14],
                    'left_gaze_point_validity': data[15],
                    'right_gaze_point_validity': data[16],
                    'left_gaze_point_in_user_x': data[17],
                    'left_gaze_point_in_user_y': data[18],
                    'left_gaze_point_in_user_z': data[19],
                    'right_gaze_point_in_user_x': data[20],
                    'right_gaze_point_in_user_y': data[21],
                    'right_gaze_point_in_user_z': data[22],
                    'left_gaze_point_on_display_area_x': data[23],
                    'left_gaze_point_on_display_area_y': data[24],
                    'right_gaze_point_on_display_area_x': data[25],
                    'right_gaze_point_on_display_area_y': data[26],
                    'left_pupil_validity': data[27],
                    'right_pupil_validity': data[28],
                    'left_pupil_diameter': data[29],
                    'right_pupil_diameter': data[30],
            
                    

                }
                writer.writerow(row)
                

        print(f"Gaze data saved to {filename} successfully.")
    except Exception as e:
        print(f"Error saving gaze data to {filename}: {e}")


# Find Eye Tracker and Apply License (edit to suit actual tracker serial no)
ft = tr.find_all_eyetrackers()
if len(ft) == 0:
    print("No Eye Trackers found!?")
    exit(1)

# Pick first tracker
mt = ft[0]
print("Found Tobii Tracker at '%s'" % (mt.address))


# Apply license
if license_file != "":
    with open(license_file, "rb") as f:
        license = f.read()

        res = mt.apply_licenses(license)
        if len(res) == 0:
            print("Successfully applied license from single key")
        else:
            print("Failed to apply license from single key. Validation result: %s." % (res[0].validation_result))
            exit
else:
    print("No license file installed")

channels = 31 # count of the below channels, incl. those that are 3 or 2 long
gaze_stuff = [
    ('device_time_stamp', 1),

    ('left_gaze_origin_validity',  1),
    ('right_gaze_origin_validity',  1),

    ('left_gaze_origin_in_user_coordinate_system',  3),
    ('right_gaze_origin_in_user_coordinate_system',  3),

    ('left_gaze_origin_in_trackbox_coordinate_system',  3),
    ('right_gaze_origin_in_trackbox_coordinate_system',  3),

    ('left_gaze_point_validity',  1),
    ('right_gaze_point_validity',  1),

    ('left_gaze_point_in_user_coordinate_system',  3),
    ('right_gaze_point_in_user_coordinate_system',  3),

    ('left_gaze_point_on_display_area',  2),
    ('right_gaze_point_on_display_area',  2),

    ('left_pupil_validity',  1),
    ('right_pupil_validity',  1),

    ('left_pupil_diameter',  1),
    ('right_pupil_diameter',  1)
]


def fetch_text_file():
    return current_text_index

def fetch_font_size():
    return font_size[0]

def fetch_font():
    return font_family[0]


def unpack_gaze_data(gaze_data):
    x = []
    for s in gaze_stuff:
        d = gaze_data[s[0]]
        
        if isinstance(d, tuple):
            x = x + list(d)
        else:
            x.append(d)
    return x

last_report = 0
N = 0

gaze_data_list = []
#i=0

additional_features = []

def gaze_data_callback(gaze_data): # Pretty much the main loop:
    '''send gaze data'''

    '''
    This is what we get from the tracker:

    device_time_stamp

    left_gaze_origin_in_trackbox_coordinate_system (3)
    left_gaze_origin_in_user_coordinate_system (3)
    left_gaze_origin_validity
    left_gaze_point_in_user_coordinate_system (3)
    left_gaze_point_on_display_area (2)
    left_gaze_point_validity
    left_pupil_diameter
    left_pupil_validity

    right_gaze_origin_in_trackbox_coordinate_system (3)
    right_gaze_origin_in_user_coordinate_system (3)
    right_gaze_origin_validity
    right_gaze_point_in_user_coordinate_system (3)
    right_gaze_point_on_display_area (2)
    right_gaze_point_validity
    right_pupil_diameter
    right_pupil_validity

    system_time_stamp
    '''

    #for k in sorted(gaze_data.keys()):
    #    print(' ' + k + ': ' +  str(gaze_data[k]))

    # Pretty much the main loop:
    #for column_name in gaze_data.keys():
     #   print(column_name)
    try:
        global last_report
        global outlet
        global N
        global halted
        #global i

        sts = gaze_data['system_time_stamp'] / 1000000.

        outlet.push_sample(unpack_gaze_data(gaze_data), sts)
        stamp = time.time() - start_time
        # Append the received gaze data to the list
        gaze_data['device_time_stamp'] = stamp
        #print(gaze_data['text_file'])
        additional_features.append([stamp,fetch_text_file(),fetch_font_size(),fetch_font()])
        #print(additional_features)
        
        gaze_data_list.append(unpack_gaze_data(gaze_data))
       # gaze_data_list.append(1) # dataen for size sample 
    
        #i+=1
       
        if sts > last_report + 5:
            sys.stdout.write("%14.3f: %10d packets\r" % (sts, N))
            last_report = sts
        N += 1

        # print(unpack_gaze_data(gaze_data))
    except:
        print("Error in callback: ")
        print(sys.exc_info())

        halted = True

def import_additional_features(features):
    csv_file_path = filename
    df_csv = pd.read_csv(csv_file_path)
    matched_data = []
    for index, row in df_csv.iterrows():
        timestamp = round(row[0])  # Assuming timestamps are in the first column and rounding for matching
        matching_row = next((x for x in features if round(x[0]) == timestamp), None)
        if matching_row:
            matched_data.append(matching_row[1:])  # Excluding the timestamp column
    print("features: ",features)
    print("df:",df_csv)
    # Convert matched data to dataframe
    df_matched_data = pd.DataFrame(matched_data, columns=["text_file","font_size","font_name"])

    # Append matched data to the original dataframe
    df_combined = pd.concat([df_csv, df_matched_data], axis=1)

    # Save the combined dataframe back to CSV
    df_combined.to_csv(filename, index=False)

def start_gaze_tracking():
    global start_time
    start_time = time.time()
    mt.subscribe_to(tr.EYETRACKER_GAZE_DATA, gaze_data_callback, as_dictionary=True)
    return True

def end_gaze_tracking():
    print("End gaze")
    if gaze_data_list:
        
        save_gaze_data_to_csv(gaze_data_list, filename)
        print("Importing additional features...")
        time.sleep(3)
        import_additional_features(additional_features)
        print("Complete. Ready for shutdown")

        
    mt.unsubscribe_from(tr.EYETRACKER_GAZE_DATA, gaze_data_callback)
   
    return True

halted = False


# Set up lsl stream
def setup_lsl():
    global channels
    global gaze_stuff

    info = lsl.StreamInfo('Tobii', 'ET', channels, 90, 'float32', mt.address)
    info.desc().append_child_value("manufacturer", "Tobii")
    channels = info.desc().append_child("channels")
    cnt = 0
    for s in gaze_stuff:
        if s[1]==1:
            cnt += 1
            channels.append_child("channel") \
                    .append_child_value("label", s[0]) \
                    .append_child_value("unit", "device") \
                    .append_child_value("type", 'ET')
        else:
            for i in range(s[1]):
                cnt += 1
                channels.append_child("channel") \
                        .append_child_value("label", "%s_%d" % (s[0], i)) \
                        .append_child_value("unit", "device") \
                        .append_child_value("type", 'ET')

    outlet = lsl.StreamOutlet(info)
    
    return outlet

outlet = setup_lsl()
# Bind arrow keys to the navigate_text function
root.bind('<Left>', navigate_text)
root.bind('<Right>', navigate_text)

root.bind('<Escape>', close_window)

# Start the GUI event loop

# Main loop; run until escape is pressed
print("%14.3f: LSL Running; press CTRL-C repeatedly to stop" % lsl.local_clock())
start_gaze_tracking()
try:
    while not halted:
        time.sleep(1)
        keys = ()  # event.getKeys()
        if len(keys) != 0:
            if keys[0]=='escape':
                halted = True
        root.mainloop()
        if halted:
            break

        # print(lsl.local_clock())

except:
    print("Halting...")

print("terminating tracking now")
end_gaze_tracking()
