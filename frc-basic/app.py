import seaborn as sns

# Import data from shared.py
from shared import df, copr_stats, team_list, event_keys

from shiny.express import input, render, ui
from shiny import reactive
from shinywidgets import render_plotly

import os
import requests
import statbotics
import pandas as pd
import plotly.express as px
sb = statbotics.Statbotics()

tba_key = os.environ.get('TBA_KEY')
tba_headers = {
    'Accept': 'application/json',
    'X-TBA-Auth-Key': tba_key
}

ui.page_opts(title="FRC Graphs?")

with ui.sidebar():
    ui.input_dark_mode()
    ui.input_select("x_var", "Select x variable", choices=copr_stats)
    ui.input_select("y_var", "Select y variable", choices=copr_stats)
    ui.input_select("event", "Event", choices=event_keys, selected="2025new")
    ui.input_selectize("teams", "Teams", choices=team_list, multiple=True)
    #ui.input_switch("species", "Group by species", value=True)
    #ui.input_switch("show_rug", "Show Rug", value=True)


with ui.card(full_screen=True):
    @render_plotly
    def copr():
        return px.scatter(copr_data(), x=input.x_var(), y=input.y_var(), 
                          text="index",
                          labels={"index": "Team", 
                                  input.x_var(): str(input.x_var()), 
                                  input.y_var(): str(input.y_var())},
                          template="plotly_dark")
    

@reactive.calc
def copr_data():
    url = f"https://www.thebluealliance.com/api/v3/event/{input.event()}/coprs"
    teams = pd.DataFrame(requests.get(url, headers=tba_headers).json())
    teams = teams.reset_index()
    teams['index'] = teams['index'].str[3:]
    return teams