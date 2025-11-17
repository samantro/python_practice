raw_data = [
    {"name": "vishal ", "score": " 83"},
    {"name": "   RAHUL", "score": "91 "},
    {"name": "priya", "score": "  77 "},
    {"name": "amit", "score": "not available"},
    {"name": "SONIA ", "score": "88"}
]

cleaned_data = []
valid_scores = []
for entry in raw_data:
    name = entry["name"].strip().title()
    score_str = entry["score"].strip()
    if score_str.isdigit():
        score = int(score_str)
        valid_scores.append(score)
    else:
        score = None
    cleaned_data.append({"name": name, "score": score})



print("cleaned_data = ", cleaned_data)
print("Average Score:", sum(valid_scores) / len(valid_scores))