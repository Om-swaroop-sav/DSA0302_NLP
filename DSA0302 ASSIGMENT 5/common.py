"""Shared synthetic disaster-control-room demonstration data and utilities."""
import re, json, time
from pathlib import Path

BASE = Path(__file__).resolve().parent
DATA = BASE / "data"
OUT = BASE / "outputs"
OUT.mkdir(exist_ok=True)

REPORTS = [
    {"id":"R01","speaker":"citizen_A","text":"Water is rising near the old bridge. It has covered the east lane. Therefore buses should use Market Road."},
    {"id":"R02","speaker":"citizen_B","text":"A tree fell across Lake Road. It blocks both lanes. The road is unsafe for ambulances."},
    {"id":"R03","speaker":"citizen_C","text":"The power failed in Ward 4. The transformer is flooded. Crews are checking it now."},
    {"id":"R04","speaker":"citizen_D","text":"The relief camp at Central School is open. It has drinking water and medical support."},
    {"id":"R05","speaker":"citizen_E","text":"The river crossed the warning mark. As a result, low-lying homes may flood. Residents should move to higher ground."},
    {"id":"R06","speaker":"citizen_F","text":"The north road is closed because a culvert is damaged. The closure will remain until engineers inspect it."},
    {"id":"R07","speaker":"citizen_G","text":"An elderly resident needs medicine. She is waiting near the bus stand. Please send an ambulance."},
    {"id":"R08","speaker":"citizen_H","text":"A shelter opened at ZP High School. The building has separate rooms for families. It closes at 9 PM."},
    {"id":"R09","speaker":"citizen_I","text":"Rain has stopped in the west zone. However, water remains on the service road. Drivers should proceed slowly."},
    {"id":"R10","speaker":"citizen_J","text":"A power line is hanging over the street. It is dangerous. Keep away until the electricity team arrives."},
    {"id":"R11","speaker":"citizen_K","text":"The canal overflowed behind the market. This has affected three streets. Officials are placing warning signs."},
    {"id":"R12","speaker":"citizen_L","text":"The bridge inspection is complete. It is now safe for light vehicles. Heavy vehicles must use the bypass."},
]
INCIDENTS = [
    {"incident_id":"I01","type":"flood","location":"Old Bridge","severity":"high","status":"active","road_status":"east lane covered","shelter":"Central School","shelter_status":"open","water_level":"rising","reported_at":"08:30","updated_at":"09:00","source":"control_room","action":"Use Market Road"},
    {"incident_id":"I02","type":"road_block","location":"Lake Road","severity":"high","status":"active","road_status":"both lanes blocked","shelter":"None","shelter_status":"unknown","water_level":"not applicable","reported_at":"08:45","updated_at":"09:05","source":"field_team","action":"Avoid Lake Road"},
    {"incident_id":"I03","type":"power_failure","location":"Ward 4","severity":"medium","status":"investigating","road_status":"open","shelter":"None","shelter_status":"unknown","water_level":"not applicable","reported_at":"08:50","updated_at":"09:10","source":"utility_team","action":"Keep clear of flooded transformer"},
]
DIALOGUES = [
    ("Where is the open relief camp?","QUESTION"),
    ("I am in Ward 4.","INFORM"),
    ("The camp is at Central School.","INFORM"),
    ("Is it open now?","QUESTION"),
    ("Yes, it is open.","CONFIRM"),
    ("Please send an ambulance.","REQUEST_ACTION"),
    ("Thank you.","THANK"),
    ("No, I meant Ward 5.","CORRECT"),
    ("Could you repeat that?","REPEAT_REQUEST"),
    ("I do not know the street name.","CANNOT_ANSWER"),
    ("The road is blocked.","INFORM"),
    ("Are you safe?","CHECK"),
    ("Yes.","CONFIRM"),
    ("Wait there.","INSTRUCT"),
    ("I am sorry.","APOLOGY"),
    ("Good morning.","GREETING"),
    ("Goodbye.","GOODBYE"),
    ("The water is rising.","ALERT"),
    ("Why is the road closed?","WHY_QUESTION"),
    ("The bridge is damaged.","EXPLAIN"),
]
def save_json(name, obj):
    (OUT/name).write_text(json.dumps(obj, indent=2, ensure_ascii=False), encoding="utf-8")
def words(text):
    return re.findall(r"[A-Za-z0-9']+", text.lower())
def timed(fn, *args, **kwargs):
    t=time.perf_counter(); result=fn(*args, **kwargs); return result, time.perf_counter()-t
