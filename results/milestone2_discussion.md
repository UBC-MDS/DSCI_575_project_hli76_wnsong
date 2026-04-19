# 1.2. Describe Pipeline and Model Choice

We chose to implement Groq because we don't have a GPU and we wanted to try different tool other than HuggingFace. For the model choice, we chose the "llama-3.3-70b-versatile" model because it is recommended by Groq. With few test runs, we found it worked fine so we stick to keep using it.

# 2.1. Test Different Top-K Retrievals

We tested k = 5, k = 10, and initially the processes and returning results worked fine. We expected higher k would take longer time to run, but in practice it was hard to differentiate. However, maybe due to Groq API limitation, it quickly sent me limitation reached errors so we had to stop testing.

# 2.3. Prompt Template Design

With the test query = "Best container for my food that needs to be cold"
We tried 3 prompts from simple to improved to best as following:

### Simple prompt:
```
DEFAULT_SYSTEM_PROMPT = """
Instructions:
- You are a helpful Amazon shopping assistant.
- You must answer the question using ONLY the following context (real product reviews with helpful votes and the metadata for the products).
"""
```

The results:
Based on the reviews, I would recommend the "KRIB BLING Compact Refrigerator 2 Door Mini Fridge with Freezer" (parent_asin: B08T682VX8) for keeping your food cold. It has a 3.4-star rating and many reviewers have mentioned that it works well for storing food and drinks at a cold temperature. One reviewer even mentioned that it "keeps drinks super cold and my ice cream frozen." Alternatively, you could consider the "GiTenvy 15 Quarts 24 Cans Portable Car Cooler" (parent_asin: B0B3937GVL) which is a portable electric cooler that can be used to keep food and drinks cold on-the-go. It has a 3.0-star rating and some reviewers have mentioned that it works well for keeping items cool, although some have noted that the quality could be improved. If you're looking for a more specific solution, such as a container for eggs, the "Plastic Refrigerator Egg Storage Container with Flip-top Lid" (parent_asin: B08P4J57J7) or the "Set of 3 Covered Egg Container for Refrigerator" (parent_asin: B08P797NTS) may be a good option. Both of these products have high ratings and are designed specifically for storing eggs in the refrigerator.

### Improved prompt:
```
DEFAULT_SYSTEM_PROMPT = """
Instructions:
- You are a helpful Amazon shopping assistant.
- You must answer the question using ONLY the following context (real product reviews with helpful votes and the metadata for the products).
- Always cite the product ASIN when possible.
"""
```

The results:
Based on the reviews, I would recommend the "2-Tier Deviled Egg Container" (ASIN: B0855Q8MZR) for storing food that needs to be cold. It has a 4.3 average rating and many reviewers have praised its ability to keep food fresh and cold. One reviewer mentioned that it's "great for carrying or storage" and that it "keeps eggs fresher longer". Another reviewer said that it's "perfect for holding deviled eggs" and that it's "easy to use". However, if you're looking for a container that can store a larger quantity of food, you might want to consider the "Set of 3 Covered Egg Container" (ASIN: B08P797NTS) which can hold up to 34 eggs. It has a 4.3 average rating and reviewers have praised its durability and ability to keep food organized in the fridge. It's also worth considering the "Plastic Refrigerator Egg Storage Container" (ASIN: B08P4J57J7) which has a 4.6 average rating and is designed to store eggs in the fridge. One reviewer mentioned that it's "very convenient to store milk, drinks, popsicles and other snacks" and that it "looks nice" in the fridge.

### Best prompt:
```
DEFAULT_SYSTEM_PROMPT = """
Instructions:
- You are a helpful Amazon shopping assistant.
- You must answer the question using ONLY the following context (real product reviews with helpful votes and the metadata for the products).
- Always cite the product ASIN when possible.
- If the answer is present, extract and summarize it clearly.
- Do NOT say "I don't know" if the answer exists in the context.
- Only say "I don't know" if the context truly does not contain the answer.
"""
```

The results:
The best container for your food that needs to be cold seems to be the IceeNOW Freezer Pak (ASIN: B08JCZ4WNP) with a 4.6 average rating. A reviewer mentioned that it "keeps my ice packs cold for a minimum of five/six hours" and is "great for shipping perishables and chilling drinks". Alternatively, you could also consider the GiTenvy 15 Quarts 24 Cans Portable Car Cooler (ASIN: B0B3937GVL) with a 3.0 average rating, which is an electric mini fridge that can keep your food and drinks cold for quite some time. Additionally, the Friomex Dry Ice Packs (ASIN: B09Q8T47SM) with a 4.2 average rating can also be a good option for keeping your food cold, especially when shipping or storing perishables. However, if you are looking for a more specific container for eggs, the Plastic Refrigerator Egg Storage Container (ASIN: B08P4J57J7) with a 4.6 average rating or the Whirlpool Egg Container (ASIN: B002ZNNQMO) with a 3.9 average rating might be a better fit. It ultimately depends on your specific needs and preferences. 

### Conclusion
Overall, the results from simple, improved, and best prompt versions were all returning proper results. However, when we tested on unrelated category items, the best prompt would provde more concise answer. On top of that, the best prompt we set could potentially avoid LLM hallucination results by giving it more restrict prompt.


# 5.1. Manual / Qualitative Evaluation for Hybrid RAG Workflow

### Query 1
Query="quiet fast-boiling kettle for small apartment that keeps water warm"

Result:
The Gevi Milk Frothing Pitcher 12oz/350ml (ASIN: B08KGB9563) and Gevi Milk Frothing Pitcher 12oz/350ml (ASIN: B08KGF4Q3H) are both electric kettles that boil water quickly. However, reviews for these products do not specifically mention keeping water warm. One reviewer for the Gevi Milk Frothing Pitcher 12oz/350ml (ASIN: B08KGB9563) mentioned that it "heats up water fast" and another reviewer for the same product mentioned it has "automatic shut-off". Another product, the Danby DKT17C2SSDB 1.7L Kettle (ASIN: B01GV52L4U), has a review stating it "works very well" but does not mention keeping water warm or being particularly quiet. Considering the criteria of being quiet and keeping water warm, none of these products perfectly match, but the Gevi Milk Frothing Pitcher 12oz/350ml (ASIN: B08KGB9563) has some relevant features.

Accuracy: Yes; 
Completeness: Yes; 
Fluency: Yes


### Query 2
Query="high-power blender for nut butter and ice under $200"

Result:
I don’t know.

Accuracy: No; 
Completeness: No; 
Fluency: Yes


### Query 3
Query="countertop oven that fits a 9x13 pan and has air fry mode"


Result:
The B08PN448L7 and B08B3DK2C6 products are wall ovens and the B095YNXNDW is an air fryer toaster oven, but none of them are countertop ovens that fit a 9x13 pan. However, the B095YNXNDW product has a 13.5 Quart capacity which might fit a 9x13 pan. It is also worth noting that the B07YZTGYXS and B08DLKXX22 products do not have air fry mode. The B08NVBYTZV product has air fry mode, but it is an induction range, not a countertop oven. The B086V54184 product is an electric range with air fry mode, but it is not a countertop oven. Therefore, the B095YNXNDW product is the closest match to the requirements, but it is an air fryer toaster oven, not a traditional countertop oven. It is recommended to check the product dimensions and features to confirm if it fits your needs. The ASIN of the product is B095YNXNDW.

Accuracy: Yes; 
Completeness: Yes; 
Fluency: Yes


### Query 4
Query="lightweight cordless vacuum for hardwood, pet hair, and stairs under 5 kg"


Result:
The acum Cordless Stick Vacuum (ASIN: B009A6OTU2) is a lightweight option that fits your requirements, weighing under 5 kg and suitable for hardwood, pet hair, and stairs. It has a 6-in-1 handheld cleaner and a 30-minute lasting runtime.

Accuracy: Yes; 
Completeness: Yes; 
Fluency: Yes


### Query 5
Query="convection toaster oven for baking small batches"

Result:
For baking small batches, you may want to consider the Air Fryer Toaster Oven 13.5 Quart Large Air Fryer Oven 10in1 Convection Oven (ASIN: B095YNXNDW). It has a 13.5 quart capacity and features a convection oven setting, making it suitable for baking small batches. One reviewer mentioned using it to make French fries and stated that it was “very easy to use” (180 votes). Another reviewer used it to cook chicken wings and found it to be “easy” and produced “juicy and tender” results (122 votes).

Accuracy: Yes; 
Completeness: Yes;  
Fluency: Yes
