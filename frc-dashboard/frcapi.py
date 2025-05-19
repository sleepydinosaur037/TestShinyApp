import statbotics
sb = statbotics.Statbotics()
import json
import requests
import base64 as b64
import pandas as pd
from PIL import Image
import operator

import plotly.express as px
import plotly.graph_objects as go
import cv2
import os

tba_key = os.environ.get('TBA_KEY')
tba_headers = {
    'Accept': 'application/json',
    'X-TBA-Auth-Key': tba_key
}

team_list = []
for i in range(22):
    url = f"https://www.thebluealliance.com/api/v3/teams/2025/{i}/keys"
    request = requests.get(url, headers=tba_headers).json()
    team_list += request

url = f"https://www.thebluealliance.com/api/v3/event/2025mdsev/coprs"
data = requests.get(url, headers=tba_headers).json()
copr_stats = list(pd.DataFrame(data).columns)