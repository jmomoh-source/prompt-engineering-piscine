# Step 1: Extract User Intent
### Prompt:

```
Given the following user query: "What's the temperature in Paris?"
Extract the following information in JSON format:
- city: the city name mentioned
- intent: what the user wants to know
Return as: {"city": <string>, "intent": <string>}
```

Output:
``` json
{"city": "Paris", "intent": "current temperature"}
```

**Purpose:** This step parses the user's natural language question and extracts structured information needed for the next step.



### Step 2: Simulate Weather API Call

**Prompt:**
```
Simulate a weather API response for Paris today in JSON format with this structure: {"location": <string>, "temperature_celsius": <number>, "condition": <string>}
```

Output:
``` json
{"location": "Paris", "temperature_celsius": 8.5, "condition": "partly cloudy"}
```

**Purpose:** Using the city extracted from Step 1, this step retrieves weather data in a structured format.



# Step 3: Format Natural Language Response

**Prompt:**
```
Given the weather data: {"location": "Paris", "temperature_celsius": 8.5, "condition": "partly cloudy"}
And user query: "What's the temperature in Paris?"
Write a natural response to the user.
```

**Output:**

``` json
The temperature in Paris is currently 8.5°C with partly cloudy conditions. It's a typical mild winter day there.
```

**Purpose:** This step converts the structured data back into a natural, user-friendly response.



# Complete Chain Flow Diagram

```
User Query → [Step 1: Parse] → [Step 2: Get Data] → [Step 3: Format] → Final Response
```

``` json
"What's the temperature in Paris?" 
    ↓
{"city": "Paris", "intent": "current temperature"}
    ↓
{"location": "Paris", "temperature_celsius": 8.5, "condition": "partly cloudy"}
    ↓
"The temperature in Paris is currently 8.5°C with partly cloudy conditions."
```


# My Analysis:
I created a three step prompt chain that simulates how an AI agent processes requests: 
Step 1 extracts the city and intent from the user's question, 
Step 2 calls the weather API with that city, 
Step 3 formats the data into a natural response. 

If any step fails to produce the expected JSON structure, the entire chain breaks down, which taught me the importance of designing precise prompts with clear output specifications. Breaking complex tasks into smaller, focused steps makes the workflow more reliable and easier to debug.

