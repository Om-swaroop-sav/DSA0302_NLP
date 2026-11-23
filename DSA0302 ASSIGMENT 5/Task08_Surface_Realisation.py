"""Task 8: template/grammar-inspired surface realiser with audience variants."""
def realise(facts,audience="public"):
    loc=facts.get("location","the affected area")
    typ=facts.get("type","incident").replace("_"," ")
    severity=facts.get("severity","unknown")
    status=facts.get("status","under review")
    action=facts.get("action","Follow official updates.")
    if audience=="field_officer":
        return f"{typ.title()} at {loc}: severity={severity}; status={status}. Action: {action}."
    return f"{severity.title()} {typ} has been reported at {loc}. The incident is {status}. {action}."
def main():
    print("TASK 8 - SURFACE REALISATION")
    samples=[
      {"location":"Old Bridge","type":"flooding","severity":"high","status":"active","action":"Use Market Road."},
      {"location":"Lake Road","type":"road_block","severity":"high","status":"active","action":"Avoid Lake Road."},
      {"location":"Ward 4","type":"power failure","severity":"medium","status":"investigating","action":"Keep clear of the transformer."},
      {"location":"Central School","type":"relief camp","severity":"low","status":"open","action":"Bring identification if available."},
      {"location":"North Road","type":"road closure","severity":"medium","status":"active","action":"Use the bypass."},
      {"location":"West Zone","type":"waterlogging","severity":"low","status":"monitoring","action":"Drive slowly."},
    ]
    for x in samples: print("\nPublic:",realise(x),"\nField:",realise(x,"field_officer"))
    print("\nReference policy: full noun phrase on first mention; repeat the noun when a pronoun could be ambiguous.")
if __name__=="__main__": main()
