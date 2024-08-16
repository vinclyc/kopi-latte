# The Kopi / Latte Ratio - Understanding Coffee Preference Across Singapore | Location & Review Data Extraction via Google Maps API | Review Text Classification with Hugging Face | Geospatial Data Visualisation using GeoPandas

## Introduction & Motivation
There are two main types of coffee served in Singapore - kopi, a rich concoction made with dark-roasted Robusta coffee beans and a hearty serving of condensed milk. And latte (or cuppucino, mocha etc), a more nuanced coffee beverage consisting of an espresso shot pulled from fresh Arabica beans and creamy steamed milk.

As a coffee fan, I am curious about the coffee preferences of the people in Singapore. Does kopi reign supreme across the whole of Singapore? Are there cafe hotspots outside of Singapore's central region? These questions sparked my interest to investigate further using data.

## Results & Key Insights


Map showing the concentration of cafes across areas in Singapore. Dark brown areas have a higher concentration of cafes vs kopitiams.

1. Kopi is king in Singapore, with about 3 kopitiams for every 1 cafe in Singapore. The top 3 areas with the most kopitiams are Jurong West (171), Seng Kang (146) and Yishun (143)
2. It's no surprise that areas with the most cafes to kopitiam are located in Central Singapore - such as the Downtown Core, Orchard and Singapore River areas. Two areas to highlight outside the Central region are Seletar (Wheeler's Yard etc) and Changi (Changi Village and Changi Airport Jewel)
3. East vs West - The East has more cafes per kopitiam compared to the West, but that's mainly due to the fact that the West has 2x more kopitiams in the region.
4. Among the heartlands, Kallang is the one with the highest cafe-to-kopitiam ratio with 1 cafe for every 2 kopitiams. Serangoon, Bedok and Pasir Ris are the next in line.

## Project Structure
The main notebooks for the project are located in the `notebooks` folder. Each notebook will run through the five key stages of the project, with more details explained below in the 'Methodology' section.

Scripts for data collection will be eventually made available in the `src` folder. Where applicable, sample data will be stored in the `data` folder.

## Methodology 
A key aspect of the project is to classify the location data from Google Maps as a cafe or kopitiam at scale, with over 4,800 locations and over 21,000 reviews to categorise. I came up with a system to efficiently classify the locations as a cafe or kopitiam. using 3 layers of classification to minimise the manual effort required:
1. Heuristic classification - Classify the locations based on popular coffee franchises and keywords in names. This requires the least effort and can classify the greatest number of locations accurately. It will also enable
2. Review text classification - Finetune a model to classify the location based on its reviews. This will automate bulk of the classification process.
3. Manual human classification - For locations that are still ambiguous, I will manually classify them. This requires the most effort and should be limited to a reasonable number of location

The sections below goes into further detail on each stage of the project

### 1. Data Collection
Retrieve GeoJSON data on planning areas in Singapore using the OneMap API, query Google Maps API for the locations as well as reviews of cafes and kopitiams in these planning areas.

### 2. Data Preparation
Clean up the location & reviews data collected from Google Maps, and prepare a dataset that can be used to finetune a review text classification model.

### 3. Model Training
Finetune a DistilBERT model using the Hugging Face toolkit to determine if a review is written for a cafe or kopitiam. The finetuned model was able to achieve a 90% accuracy on the test dataset.

### 4. Model Inference
Use the finetuned model to make predictions for the rest of the unlabelled locations. Aggregate the prediction scores for each location and determine a threshold to flag locations for manual review

### 5. Data Visualisation
After manual review, consolidate labels from the three layers of classification. Do a spatial join of the Google Maps locations and the planning areas' GeoJSON data using GeoPandas to determine the coffee-to-kopitiam ratio of each area. Gather insights and visualise the aggregated data.

# Conclusion & Reflections
Work in progress

