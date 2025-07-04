import json
import random

# Example beaches & nature spots in Southern Leyte
topics = [
    "limasawa_island", "san_juan_beach", "hinunangan_islands", "pintuyan_whale_sharks",
    "maasin_city_waterfalls", "sogod_bay", "padre_burgos_beach", "himokilan_island",
    "cagnituan_lagoon", "tangkaan_beach", "silago_beach", "pacific_resort_area",
    "kabutongan_falls", "malitbog_marine_sanctuary", "st_bernard_coral_reefs"
]

# Greetings & farewells
greetings = ["greetings"]
farewells = ["farewell"]

fallback_label = "fallback"

# Response samples generator
def generate_response(label):
    if label == "greetings":
        return [
            "Hi there! How can I help you explore Southern Leyte today?",
            "Hello! Ready to discover the stunning nature and beaches of Southern Leyte?"
        ]
    if label == "farewell":
        return [
            "Goodbye! Enjoy your trip to Southern Leyte!",
            "See you soon! Have a wonderful time exploring the beaches!"
        ]
    # Beaches & nature spots
    return [
        f"{label.replace('_', ' ').title()} is one of the hidden gems of Southern Leyte. "
        f"Visitors love its crystal-clear waters, white sand, and peaceful atmosphere. "
        f"It's perfect for swimming, relaxing, and enjoying nature with friends and family."
    ]

# Create data
data = []
responses = []

# Greetings & farewells examples
for _ in range(100):
    data.append({"text": random.choice(["Hi!", "Hello!", "Hey there!", "Good morning!"]), "label": "greetings"})
    data.append({"text": random.choice(["Goodbye!", "See you!", "Bye!", "See you later!"]), "label": "farewell"})

# Beaches / nature questions
for i in range(700):
    topic = random.choice(topics)
    question = random.choice([
        f"Can you tell me about {topic.replace('_', ' ')}?",
        f"Give me info on {topic.replace('_', ' ')}.",
        f"What can I do at {topic.replace('_', ' ')}?",
        f"Is {topic.replace('_', ' ')} good for swimming?",
        f"Describe {topic.replace('_', ' ')} please."
    ])
    data.append({"text": question, "label": topic})

# Add fallback training examples — now 200
for i in range(200):
    nonsense = f"random gibberish text {i} ajskdjh qweqwe"
    data.append({"text": nonsense, "label": fallback_label})

# Prepare non-fallback responses
for label in topics + greetings + farewells:
    responses.append({"label": label, "response": generate_response(label)})

# Add fallback responses with multiple variations (50)
fallback_responses = [
    f"I'm not sure how to answer that right now. Maybe ask about a beach or island instead. ({i})"
    for i in range(1, 51)
]
responses.append({"label": fallback_label, "response": fallback_responses})

# Write to JSON
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

with open("responses.json", "w", encoding="utf-8") as f:
    json.dump(responses, f, indent=2)

print(f"✅ Done! Created {len(data)} data items and {len(responses)} response labels.")
