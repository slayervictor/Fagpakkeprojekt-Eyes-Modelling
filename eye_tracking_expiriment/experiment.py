# Preface heretk
#
import os
import Licenses.licensefile as licensefile
license_file = licensefile.license_file
existing_files = sum(1 for file in os.listdir('eye_tracking_expiriment\data') if file.startswith('gaze_data'))
filename = f'eye_tracking_expiriment\data\gaze_data{existing_files}.csv'

# from psychopy import prefs, visual, core, event, monitors, tools, logging
import numpy as np
import tobii_research as tr
import time
import random
import pylsl as lsl
import sys
import csv
import pandas as pd
import tkinter as tk
def read_text(filen):
    with open(filen, 'r', encoding='utf-8') as file:
        return file.read()
testPerson = 1
Sequence = ['eye_tracking_expiriment\start.txt',
            
            
f'eye_tracking_expiriment\\files\Files_txt\AI_HC_P0{testPerson}_text.txt',f'eye_tracking_expiriment\\files\Files_txt\AI_HC_P0{testPerson}_MCQ.txt',f'eye_tracking_expiriment\\files\Files_txt\AI_HC_P0{testPerson}_FIBQ.txt',
f'eye_tracking_expiriment\\files\Files_txt\OR_HC_P0{testPerson}_text.txt',f'eye_tracking_expiriment\\files\Files_txt\OR_HC_P0{testPerson}_MCQ.txt',f'eye_tracking_expiriment\\files\Files_txt\OR_HC_P0{testPerson}_FIBQ.txt',

f'eye_tracking_expiriment\\files\Files_txt\AI_SK_P0{testPerson}_text.txt',f'eye_tracking_expiriment\\files\Files_txt\AI_SK_P0{testPerson}_MCQ.txt',f'eye_tracking_expiriment\\files\Files_txt\AI_SK_P0{testPerson}_FIBQ.txt',
f'eye_tracking_expiriment\\files\Files_txt\OR_SK_P0{testPerson}_text.txt',f'eye_tracking_expiriment\\files\Files_txt\OR_SK_P0{testPerson}_MCQ.txt',f'eye_tracking_expiriment\\files\Files_txt\OR_SK_P0{testPerson}_FIBQ.txt',

f'eye_tracking_expiriment\\files\Files_txt\AI_KB_P0{testPerson}_text.txt',f'eye_tracking_expiriment\\files\Files_txt\AI_KB_P0{testPerson}_MCQ.txt',f'eye_tracking_expiriment\\files\Files_txt\AI_KB_P0{testPerson}_FIBQ.txt',
f'eye_tracking_expiriment\\files\Files_txt\OR_KB_P0{testPerson}_text.txt',f'eye_tracking_expiriment\\files\Files_txt\OR_KB_P0{testPerson}_MCQ.txt',f'eye_tracking_expiriment\\files\Files_txt\OR_KB_P0{testPerson}_FIBQ.txt'

]
texts=[]

for file in Sequence:
    texts.append(read_text(file))

# Setting the font and size
font_family=['Arial','Times New Roman']
font_size=[20,16]
fontIndex = 0
# Ændre til [1,1,passagetal], når vi kører anden omgang af eksperimenter

def modStuff(tp,fontBool):
    if fontBool:
        if tp%4 == 0:
            return 0
        elif tp%4 == 1: 
            return 0
        elif tp%4 == 2:
            return 1
        elif tp%4 == 3:
            return 1
    else:
        return tp%2
    

            
fontDetails = [[modStuff(testPerson,False),modStuff(testPerson,True),1]] # Hvilken passage der skal have hvilken font, eks [[font_family_index , font_size_index , passage],[...]]  -  default (index 0) er Arial
font_sizeIndex = 0


current_text_index = 0
max_current_text_index = 0


root = tk.Tk()
root.title('Text display')
#root.geometry('1600x1200')
root.attributes('-fullscreen', True)
root.resizable(width=False, height=False)

def changeFontDetails():
    global fontIndex
    global font_sizeIndex
    currentPassage = fetch_passage_number()
    changed = False
    for i in range(0,len(fontDetails)):
        if (fontDetails[i][2]) == currentPassage:
            fontIndex = fontDetails[i][0]
            font_sizeIndex = fontDetails[i][1]
            changed = True

    if not changed: 
        fontIndex = 0
        font_sizeIndex = 0
        

def close_window(event=None):
    global current_text_index
    current_text_index = 999 #pga shutdown
    global halted
    halted = True
    root.destroy()

# Create the text widget

canvas = tk.Canvas(root, width=1600, height=1200)
canvas.pack()

# Start position for the text

x_position = 250
y_position = 150

# Function to draw text with uniform appearance
def draw_text():
    global current_text_index
    canvas.delete('all')
    text = texts[current_text_index]
    canvas.create_text(x_position, y_position, text=text, font=(font_family[fontIndex], font_size[font_sizeIndex]), anchor='nw', justify='left', width=1200)
    canvas.update()


draw_text()

def navigate_text(event):
    global current_text_index
    global max_current_text_index
    if event.keysym == 'Right':
        if current_text_index < len(texts) - 1:
            current_text_index += 1
            changeFontDetails()
            draw_text()
            if current_text_index > max_current_text_index:
                max_current_text_index +=1
            #print(fetch_passage_number())
    elif event.keysym == 'Left':
        if current_text_index > 1:
            current_text_index -= 1
            changeFontDetails()
            draw_text()
            if current_text_index > max_current_text_index:
                max_current_text_index +=1
            #print(fetch_passage_number())

    



def save_gaze_data_to_csv(gaze_data, filename):
    #print(gaze_data[0])
    
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


def fetch_text_file(): # navn på filen. 
    tempSeq = Sequence[current_text_index].replace("eye_tracking_expiriment\\","")
    return tempSeq

def fetch_passage_number(): # index på hvilken fil det er.
    seq = Sequence[current_text_index].replace("eye_tracking_expiriment\\","")
    if seq == "start.txt":
        return 0
    else:
        return int(seq.replace(seq[:7],"").replace(".txt","")[:2])

def fetch_label():
    if max_current_text_index > current_text_index:
        return "Skimming"
    else:
        return "Immersive"

def fetch_font_size(): # Skriftstørrelse
    
    return font_size[font_sizeIndex]

def fetch_font(): # Skrifttype
    return font_family[fontIndex]

def fetch_author():
    #eye_tracking_expiriment\Ai_HC_P01_text.txt  Ai_
    tempSeq = Sequence[current_text_index].replace("eye_tracking_expiriment\\","")
    tempSeq = tempSeq.replace(tempSeq[:3],"")
    if tempSeq == "rt":
        return "Start"
    else:
        return tempSeq[:2].replace("rt","Start Page")


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
        global Sequence

        sts = gaze_data['system_time_stamp'] / 1000000.

        outlet.push_sample(unpack_gaze_data(gaze_data), sts)
        stamp = time.time() - start_time
        # Append the received gaze data to the list

            
        gaze_data['device_time_stamp'] = stamp
        
        try:
            additional_features.append([stamp,Sequence[current_text_index].find("_text") >= 0,fetch_text_file(),fetch_passage_number(),fetch_font_size(),fetch_font(),fetch_author(),Sequence[current_text_index].replace("eye_tracking_expiriment\\","")[:2]=="Ai",fetch_label()])
        except:
            pass
        
        
        gaze_data_list.append(unpack_gaze_data(gaze_data))
       
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
        timestamp = round(row[0]) 
        matching_row = next((x for x in features if round(x[0]) == timestamp), None)
        if matching_row:
            matched_data.append(matching_row[1:])  

    df_matched_data = pd.DataFrame(matched_data, columns=["Reading","text_file","passage_index","font_size","font_name","Author","AI","Label"])
    df_combined = pd.concat([df_csv, df_matched_data], axis=1)

    df_combined.to_csv(filename, index=False)

def start_gaze_tracking():
    global start_time
    start_time = time.time()
    mt.subscribe_to(tr.EYETRACKER_GAZE_DATA, gaze_data_callback, as_dictionary=True)
    return True

def end_gaze_tracking():
    
    if gaze_data_list:
        save_gaze_data_to_csv(gaze_data_list, filename)
        
        print("Importing additional features...")
        import_additional_features(additional_features)
        print("Additional features imported.")
    else:
        print("No gaze data collected.")

    mt.unsubscribe_from(tr.EYETRACKER_GAZE_DATA, gaze_data_callback)
    print("Unsubscribed from gaze data stream.")
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

print("Terminating...")
end_gaze_tracking()
sys.exit()
