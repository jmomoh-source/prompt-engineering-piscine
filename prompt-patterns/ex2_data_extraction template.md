### Template Prompt:
"Extract the following fields from the text: Name, Age, Location, Occupation. Return the output in JSON format."

### Test 1:
**Input:** John Mathews, age 39, lives in Pakistan and works as a software engineer.

**Output:** 
```json
{
  "Name": "John Mathews",
  "Age": 39,
  "Location": "Pakistan",
  "Occupation": "software engineer"
}
```

### Test 2:
**Input:** Jezreal Momoh, age 25, lives in Nigeria and works as a Ethical hacker and pentester.

**Output:**
```json
{
  "Name": "Jezreal Momoh",
  "Age": 25,
  "Location": "Nigeria",
  "Occupation": "Ethical hacker and pentester"
}
```

### Test 3:
**Input:** Victoria Ifeoma works as a data scientist. She is 23 years old and currently lives in Japan.

**Output:**
```json
{
  "Name": "Victoria Ifeoma",
  "Age": 23,
  "Location": "Japan",
  "Occupation": "data scientist"
}
```

### Validation.
The template worked consistently across all 3 inputs despite different sentence structures, successfully extracting all four fields in proper JSON format. 

Test 1 and 2 followed similar structures while Test 3 varied the order significantly, yet the template still delivered the result as requested in JSON format. 

This makes the template highly reusable because it focuses on extracting specific data fields regardless of how the information is arranged in the text. The JSON output format improves usability by providing structured, machine readable data that can be easily integrated into databases, applications, or further processing workflows.