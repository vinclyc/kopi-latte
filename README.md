# The Kopi / Latte Ratio - Understanding Coffee Preference Across Singapore 
### _Data Extraction via Google Maps API | Review Text Classification with Hugging Face | Geospatial Data Visualization with GeoPandas_

## Introduction & Motivation
Singapore's coffee culture is rich and diverse, with two main types of coffee being served: **kopi**, a traditional blend made from dark-roasted Robusta beans and sweetened with condensed milk, and **latte** (or cappuccino, mocha, etc.), a more delicate drink featuring an espresso shot from Arabica beans and creamy steamed milk.

As a coffee enthusiast, I’ve always been curious about the coffee preferences across Singapore. Does kopi reign supreme across the entire island? Are there hidden café hotspots beyond the Central region? These questions inspired me to delve into the data and uncover the answers.

## Results & Key Insights
![_Map depicting the density of cafes across Singapore](plots/kopi_latte_map.jpg?raw=true "Density of cafes across Singapore")
_Map depicting the density of cafes across Singapore. Dark brown areas indicate higher concentrations of cafes compared to kopitiams._

- **Kopi is king**: There are about 3 kopitiams for every 1 café in Singapore. The top areas with the most kopitiams are Jurong West (171), Sengkang (146), and Yishun (143).
- **Central café hotspots**: As expected, the areas with the highest café-to-kopitiam ratios are in Central Singapore, such as the Downtown Core, Orchard, and Singapore River. Noteworthy café clusters outside the central region include Seletar (e.g. Wheeler's Yard) and Changi (e.g. Changi Village and Jewel at Changi Airport).
- **East vs. West**: The East has more cafés per kopitiam compared to the West, primarily because the West has twice as many kopitiams.
- **Heartland highlights**: Among the heartlands, Kallang has the highest café-to-kopitiam ratio, with 1 café for every 2 kopitiams. Following closely are Serangoon, Bedok, and Pasir Ris.

## Project Structure
The primary notebooks for this project are located in the `notebooks` folder, guiding you through the five key stages of the project. More details on each stage are provided in the 'Methodology' section below.

Scripts for data collection will be made available in the `src` folder, and sample data in the `data` folder where applicable.

## Methodology
Classifying over 4,800 locations and 21,000 reviews from Google Maps as either a café or kopitiam at scale was a core challenge. To tackle this efficiently, I developed a three-layer classification system to minimize manual effort:

1. Heuristic Classification: This initial layer uses well-known coffee franchises and keywords in names to classify the majority of locations with minimal effort.
2. Review Text Classification: Using Hugging Face, I finetuned a model to classify locations based on review content, automating a significant portion of the process.
3. Manual Classification: For locations that remain ambiguous, I performed manual classification, which is the most labor-intensive step and was reserved for a manageable number of locations.

Further details on each stage of the project are provided below.

### 1. Data Collection
Using the OneMap API, I retrieved GeoJSON data for planning areas in Singapore and queried the Google Maps API to gather location and review data for both cafes and kopitiams.

### 2. Data Preparation
The collected location and review data were cleaned and prepared to create a dataset suitable for finetuning the review text classification model.

### 3. Model Training
I finetuned a DistilBERT model using the Hugging Face toolkit to determine whether a review was written for a café or kopitiam. The model achieved 90% accuracy on the test dataset.

### 4. Model Inference
The finetuned model was then used to classify the remaining unlabelled locations. Prediction scores were aggregated for each location, and a threshold was set to flag locations requiring manual review.

### 5. Data Visualisation
After completing the manual review, I consolidated the labels from the three classification layers. Using GeoPandas, I performed a spatial join of the Google Maps locations with the GeoJSON data to calculate the coffee-to-kopitiam ratio for each area, yielding insights that were then visualized.

# Conclusion & Reflections
Work in progress

