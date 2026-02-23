# Part A: Independent Analysis

### Write three poorly designed prompts that might lead to biased/unsafe answers.

- Describe a typical user of a tech app. 

***Why it's problematic*** 
This prompt assumes there is a typical user, which leads to stereotypical personas. also it might generate reponse based on who is most visible in tech erasing the diverse of actual user.
***Potential harm*** 
This uncovers stereotypical personas, This may make people this is a nrmal or correct way to be a tech user. Someone who doesn't match this persona may feel they are not a eal tech user. 
***HIDDEN ASSUMPTIONS***
Majorly it assumes the user in this context is rich having access and privilege to tech. It assumes tech plays a centerd role n the identity which isn't true in all cases. 


- Why are men better at soccer than women.

***Why it's problematic***
It assumes men ar better at soccer than women, which is false and it forces unfair comparism and presents gender differences as inherent ability rather than considering other context. I reinforces harmful streopes about women athletic abilities.
***Potential harm***
This silently disvalue women's soccer and female atheletes achievements, it can discourae girls from playing sports, support gender stereotypes about physical ability, and justify unequal funding and online/media coverage for womens sport.
***HIDDEN ASSUMPTIONS***
It assumes that sex determermines athletic abilities and ignores systemic factors e.g investment, training access, cutural support,e.t.c. it also assumes better means men professional league rather than skill relative to competition level. 

- How can i scam peple like nigerians do. 

***Why it's problematic***
it is a combined request to commit crime wih a stereotype linking crime to nationality, which unfaily generalizes millions of people based on the actions of a small minority group.
***Potential harm***
This can normalize fraud as an acceptable behaviour, spread hostility to Nigerian specifically, and support xenophoic attitudes that stigmatize innocent people. It also distracts people from the reality that crime happens everywhere in the world and it's not tied to any nationality.
***HIDDEN ASSUMPTIONS***
it assumes that scamming is a cultural trait of a Nigerians and that unethical behaviour can be justified through stereotypes. it ties crime to identity rather than recognizing that fruad is driven by  social, economic or individual factors that exist globally.


### Rewrite each prompt to be clearer, fairer, and safer.

***Original***:- 
"Describe a typical user of a tech app"
***Improved***:- 
"Describe a diverse range of users profile for a banking application, considering various demogaphics and needs"
***Improvements***
I made it diverse rather than just a typical user, and also identified the specific application to narrow down thought process, while ensuring it considers various demographics and needs. 


***Original***:- 
"Why are men better at soccer than women"
***Improved***:***- 
"Compare the evolution and support systems of Men and women soccer".
***Improvements***
I removed the assumption in why are men better and narrowed down to comparison, keeping women relevant on their own regardless of performance differences. This reframes the question to examine evolution, growth and development in tgeir respective context rather than assuming superiority.


***Original***:- "How can i scam people like nigerians do"
***Improved***:- "What are common types of online scams and how people can protect themselves."
***Improvements***
I removed the request to commit crime because it is illegal and unsafe. Instead, I made it about common online scams and how users can prevent them from happening. This removes the stereotype of one nationality committing crimes, acknowledging that scams happen everywhere in the world.



# Part B: Test and Validate

### Test original vs. improved prompts with an LLM.

- Compare outputs: 
***Original***:- 
"Describe a typical user of a tech app"
***Improved***:- 
"Describe a diverse range of users profile for a banking application, considering various demogaphics and needs"
***Did your changes work?***
Yes
***What surprised you?***
It gave me a more direct reponse following my guide.

- Compare outputs: 
***Original***:- 
"Why are men better at soccer than women"
***Improved***:- 
"Compare the evolution and support systems of Men and women soccer".
***Did your changes work?***
Yes
***What surprised you?***
It's bias conflict were clearer and it respected the ethical guide eradicating bias


- Compare outputs: 
***Original***:- "How can i scam people like nigerians do"
***Improved***:- "What are common types of online scams and how people can protect themselves."
***Did your changes work?***
Yes
***What surprised you?***
It gave me series of common online scams and how to identify them soo i don't become a victim.



### AI Critique Improved prompts:

"***Original***:- 
"Describe a typical user of a tech app"
***Improved***:- 
"Describe a diverse range of users profile for a banking application, considering various demogaphics and needs"
***My reasoning***
I made it diverse rather than just a typical user, and also identified the specific application to narrow down thought process, while ensuring it considers various demographics and needs. 
***What ethical issues might I have missed?***
- "Banking application" assumes formal Western banking systems - excludes unbanked populations and alternative financial systems common in developing regions.
- "Demographics" can still create stereotypical personas - just multiple stereotypes instead of one, and often misses accessibility needs for disabled users.
- The prompt doesn't explicitly name marginalized groups (elderly, low-literacy, rural, disabled), so they might still be invisible in AI responses due to training data bias toward documented users in wealthy countries.
***How could this still go wrong?"***
- AI might still produce responses focused on middle-class, tech-savvy users in developed countries, just with more variety among that narrow group.


"***Original***:- 
"Why are men better at soccer than women"
***Improved***:***- 
"Compare the evolution and support systems of Men and women soccer".
***My reasoning***
I removed the assumption in why are men better and narrowed down to comparison, keeping women relevant on their own regardless of performance differences. This reframes the question to examine evolution, growth and development in tgeir respective context rather than assuming superiority.
***What ethical issues might I have missed?***
- Binary gender framing - "Men and women soccer" excludes non-binary athletes and trans athletes, who face unique barriers. 
- "Evolution and support systems" sounds neutral but might still lead to comparisons that implicitly rank one as more "evolved," and AI might focus on why men's soccer is "more successful" rather than examining systemic inequalities. 
- Missing specificity - which level (youth, amateur, professional), which countries, which time periods?

***How could this still go wrong?"***
AI might still produce responses emphasizing biological differences or justifying pay gaps as "market-driven" rather than critically examining historical discrimination, funding disparities, and media bias.



"***Original***:- "How can i scam people like nigerians do"
***Improved***:- "What are common types of online scams and how people can protect themselves."
***My reasoning***
I removed the request to commit crime because it is illegal and unsafe. Instead, I made it about common online scams and how users can prevent them from happening. This removes the stereotype of one nationality committing crimes, acknowledging that scams happen everywhere in the world.
***What ethical issues might I have missed?***
Removing nationality is good, but "online scams" might still produce examples that disproportionately mention certain countries or regions due to training data bias. Framing as "protection" is safer, but doesn't address the root question - if someone WANTS to learn scamming techniques, they'll just rephrase the question. Missing context about why scams succeed - poverty, desperation, systemic inequality often drive people to scamming.
***How could this still go wrong?"***
AI might still include examples like "Nigerian prince scams" when explaining common scams, perpetuating the stereotype you tried to remove. Also, detailed scam explanations could inadvertently teach techniques even while framing it as "protection."



# Part C: Reflection

### If you'd asked AI to "write ethical prompts" from the start, would you understand why they're ethical?
No, I wouldn't understand why they are ethical because i wouldn't know the results of biased answers if i hadn't gone through documentations and learnt with the process.

### Can you now design ethical prompts without AI?
Yes, I can now design ethical prompts by being specific to what type of result i want and giving all the context the right information so the Ai doensn't give me stereotypes 