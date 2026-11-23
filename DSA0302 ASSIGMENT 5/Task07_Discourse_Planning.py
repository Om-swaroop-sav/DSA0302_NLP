"""Task 7: content selection and discourse planning from structured incidents."""
from common import INCIDENTS
PRIORITY={"high":1,"medium":2,"low":3}
def plan(incident):
    content=["type","location","severity","status","road_status","action","updated_at"]
    if incident["shelter_status"]!="unknown": content += ["shelter","shelter_status"]
    order=sorted(content,key=lambda k: (0 if k in ["type","location","severity"] else 1))
    return {"incident_id":incident["incident_id"],"selected_fields":order,
            "suppressed_fields":[k for k in incident if k not in order],
            "relations":["BACKGROUND","RESULT","ACTION"]}
def main():
    print("TASK 7 - DISCOURSE PLANNING")
    for i in INCIDENTS:
        print("\nPlan:",plan(i))
if __name__=="__main__": main()
