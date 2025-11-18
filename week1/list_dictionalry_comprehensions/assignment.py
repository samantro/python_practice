raw_scores = [
    {"name": " vishal ", "score": " 83"},
    {"name": "   RAHUL", "score": "91 "},
    {"name": "priya", "score": "  77 "},
    {"name": "amit", "score": "not available"},
    {"name": "SONIA ", "score": "88"}
]

name_to_score = [{entry["name"].strip().title():int(entry["score"].strip()) if entry["score"].strip().isdigit() else None} for entry in raw_scores ]
names = [list(d.keys())[0] for d in name_to_score]
scores = [list(d.values())[0] for d in name_to_score]
print(name_to_score)
print(names)
print(scores)