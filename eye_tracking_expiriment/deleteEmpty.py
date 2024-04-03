import pandas as pd
gaze = pd.read_csv("eye_tracking_expiriment\data\gaze_data_Alexander_2.csv")

gaze = gaze.dropna()

gaze.to_csv("test.csv")