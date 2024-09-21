# The Kopi / Latte Ratio - Understanding Coffee Preference Across Singapore 
### _Querying Locations via Google Maps API | Review Text Classification with Hugging Face | Geospatial Data Visualization with GeoPandas_

## Introduction & Motivation
Singapore's coffee culture is rich and diverse, with two main types of coffee being served: **kopi**, a traditional blend made from dark-roasted Robusta beans and sweetened with condensed milk, and **latte** (or cappuccino, mocha, etc.), a more delicate drink featuring an espresso from Arabica beans and creamy steamed milk.

As a coffee enthusiast, I’ve always been curious about the coffee preferences across Singapore. Does kopi reign supreme across the entire island? Are there hidden café hotspots beyond the Central region? These questions inspired me to delve into the data and uncover the answers.

I also wanted to refine my skills in API usage, deepen my understanding of NLP models with Hugging Face, elevate my geospatial data visualization capabilities, and present my insights clearly and visually.

## Results & Key Insights
![Infographic on coffee preferences across Singapore](img/kopi_latte_infographic.png? "Coffee preferences across Singapore")

_Infographic on coffee preferences across Singapore_

- **Kopi is king**: There are about 2.4 kopitiams for every 1 café in Singapore. The top areas with the most kopitiams are Jurong West (171), Sengkang (146), and Yishun (143).
- **Central café hotspots**: As expected, the areas with the highest café-to-kopitiam ratios are in Central Singapore, such as the Marina South, Singapore River and Tanglin. Noteworthy café clusters outside the central region include Seletar (e.g. Wheeler's Yard) and Changi (e.g. Changi Village and Jewel at Changi Airport).
- **East vs. West**: The East has more cafés per kopitiam compared to the West, primarily because the West has twice as many kopitiams.
- **Heartland highlights**: Serangoon, Kallang, and Queenstown stand out with the highest cafe-to-kopitiam ratios, while Sembawang, Bukit Batok, and Woodlands have the most concentration of kopitiams.

## Project Structure
The primary notebooks for this project are located in the `notebooks` folder, guiding you through the five key stages of the project. 

## Methodology
Classifying over 4,800 locations and 21,000 reviews from Google Maps as either a café or kopitiam at scale was a core challenge. To tackle this efficiently, I developed a three-layer classification system to minimize manual effort:
  
1. **Heuristic Classification**: This initial layer uses well-known coffee franchises and keywords in names to classify the majority of locations with minimal effort.
2. **Review Text** Classification: Using Hugging Face, I finetuned a model to classify locations based on review content, automating a significant portion of the process.
3. **Manual Classification**: For locations that remain ambiguous, I performed manual classification, which is the most labor-intensive step and was reserved for a manageable number of locations.

Further details on each stage of the project are provided below.

### 1. Data Collection
Using the OneMap API, I retrieved GeoJSON data for planning areas in Singapore and queried the Google Maps API for locations and reviews of cafes and kopitiams in the planning areas.

### 2. Data Preparation
The collected location and review data were cleaned and prepared to create a dataset suitable for finetuning the review text classification model.

### 3. Model Training
I finetuned a DistilBERT model using the Hugging Face toolkit to determine whether a review was written for a café or kopitiam. The model achieved 90% accuracy on the test dataset.

### 4. Model Inference
The finetuned model was then used to classify the remaining unlabelled locations. Prediction scores were aggregated for each location, and a threshold was set to flag locations requiring manual review.

### 5. Data Visualisation
In conclusion, this project was enjoyable and enabled me to discover many interesting cafés to visit in Singapore through my data exploration. I was also impressed by the performance and ease of use of the Hugging Face library, which significantly accelerated the project’s progress. Overall, I successfully achieved my goals of enhancing my data science and analytics skills across various areas.

# Conclusion & Reflections
In conclusion, this project was enjoyable and allowed me to discover many interesting cafés to visit in Singapore through my data exploration. I was also impressed by the performance and ease of use of the Hugging Face library, which significantly accelerated the project’s progress. Overall, I successfully achieved my goals of developing my data science and analytics skills in various areas.

# Acknowledgements
I would like to express my gratitude to the following resources that were instrumental in this project:

- [Google Maps Platform]([url](https://mapsplatform.google.com/)): For providing essential location and reviews data.
- [OneMap API]([url](https://www.onemap.gov.sg/apidocs/)) : For offering GeoJSON data on planning areas in Singapore.
- [Hugging Face]([url](https://huggingface.co/)): For their user-friendly NLP library that facilitated model fine-tuning.
- [GeoPandas]([url](https://geopandas.org/en/stable/)): For enabling efficient geospatial data visualization and analysis.
- [Canva]([url](https://www.canva.com/)): For assisting in the creation of the infographic to present my findings.
