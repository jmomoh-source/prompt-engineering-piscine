## Weak Prompt:
Simulate a weather API response for Ontario today.

## Refined Prompt:
```
Simulate a weather API response for [CITY] today in JSON format with this structure: {"location": <string>, "temperature_celsius": <number>, "condition": <string>}
```

## Expected JSON Schema
``` json
{ 
"location": "Paris", 
"temperature_celsius": 18, 
"condition": "Cloudy" 
}
```


## Test Results

### Paris 
***Input***
Simulate a weather API response for Paris today in JSON format with this structure: {"location": <string>, "temperature_celsius": <number>, "condition": <string>}

***output***
``` json
{
  "location": "Paris",
  "temperature_celsius": 8.5,
  "condition": "partly cloudy"
}
```



### Ontario
***Input***
Simulate a weather API response for Onatario today in JSON format with this structure: {"location": <string>, "temperature_celsius": <number>, "condition": <string>}

***output***
``` json
{
  "location": "Ontario",
  "temperature_celsius": -3.2,
  "condition": "snow showers"
}
```


### Lagos
***Input***
Simulate a weather API response for Lagos today in JSON format with this structure: {"location": <string>, "temperature_celsius": <number>, "condition": <string>}

***output***
``` json
{
  "location": "Lagos",
  "temperature_celsius": 29.8,
  "condition": "scattered thunderstorms"
}
```



### London
***Input***
Simulate a weather API response for London today in JSON format with this structure: {"location": <string>, "temperature_celsius": <number>, "condition": <string>}

***output***
``` json
{
  "location": "London",
  "temperature_celsius": 7.2,
  "condition": "light rain"
}
```



## COMPARISON:
When I used the weak prompt, the output was unstructured. After refining the prompt to specify the JSON schema, all outputs consistently followed the exact structure with the three required fields.
Tested across multiple cities Paris, Ontario, Lagos, London, the JSON format remained consistent - all responses included 'location' as string, 'temperature_celsius' as number, and 'condition' as string. This demonstrates that explicitly defining the expected structure in the prompt ensures reliable, parseable outputs.
This exercise taught me that being explicit about the expected output format in my prompt is crucial for getting consistent, machine-readable data from LLMs.
