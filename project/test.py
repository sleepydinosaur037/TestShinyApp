import statbotics
import json
import requests

sb = statbotics.Statbotics()
data = sb.get_team_matches(449, year=2025)
print(json.dumps(data, indent=4))
