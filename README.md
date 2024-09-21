# The Kopi / Latte Ratio - Understanding Coffee Preference Across Singapore

### _Querying Locations via Google Maps | Text Classification with Hugging Face | Geospatial Visualization with GeoPandas_

## Introduction & Motivation
Singapore's coffee culture is diverse, featuring the **kopi** (traditional dark-roasted Robusta) and the **latte** (espresso from Arabica beans). 

As a coffee enthusiast, I explored questions like:
- How much does kopi dominate in Singapore?
- Are there hidden café hotspots outside the Central region?

This project aimed to:
- Enhance my skills in API usage.
- Familiarize myself with NLP models via Hugging Face.
- Improve capabilities in geospatial data visualization.
- Communicate insights clearly and visually.

## Results & Key Insights
![Infographic on coffee preferences across Singapore](img/kopi_latte_infographic.png?raw=true)

_Infographic on coffee preferences across Singapore_

- **Kopi is king**: 2.4 kopitiams for every café in Singapore. Top areas: Jurong West (171), Sengkang (146), Yishun (143).
- **Central café hotspots**: Highest ratios in Marina South, Singapore River, and Tanglin. Notable non-Central clusters: Seletar (Wheeler's Yard), Changi (Changi Village).
- **East vs. West**: The East has more cafés per kopitiam; the West has twice as many kopitiams.
- **Heartland highlights**: Serangoon, Kallang, and Queenstown have the highest café-to-kopitiam ratios; Sembawang, Bukit Batok, and Woodlands have the most kopitiams.

## Project Structure
Find the main notebooks in the `notebooks` folder, guiding you through the project's five key stages.

## Methodology
To classify over 4,800 locations and 21,000 reviews efficiently, I developed a three-layer classification system:

1. **Heuristic Classification**: This initial step uses coffee franchise names and keywords to classify the majority of locations with minimal manual effort.
2. **Review Text Classification**: I fine-tuned a Hugging Face model to classify locations based on review content, automating a significant portion of the process.
3. **Manual Classification**: For locations that remain ambiguous after the first two layers, I performed manual classification, ensuring accuracy while managing the workload effectively.

This multi-layered approach maximized efficiency and reduced the need for extensive manual review.

### 1. Data Collection
Used the OneMap API for GeoJSON data and Google Maps for café and kopitiam locations.

### 2. Data Preparation
Cleaned and organized the data for model training.

### 3. Model Training
Fine-tuned a DistilBERT model on Hugging Face, achieving 90% accuracy.

### 4. Model Inference
Classified remaining unlabeled locations, aggregating prediction scores.

### 5. Data Visualization
Used GeoPandas to calculate coffee-to-kopitiam ratios and visualize insights.

## Conclusion & Reflections
This project was fun and led me to discovering interesting cafés. The Hugging Face library greatly increased project speed, and I met my goals of enhancing my data science and analytics skills.

## Acknowledgements
Thanks to:
- [**Google Maps**](https://mapsplatform.google.com/): For essential location data.
- [**OneMap API**](https://www.onemap.gov.sg/apidocs/): For GeoJSON data.
- [**Hugging Face**](https://huggingface.co/): For their NLP library.
- [**GeoPandas**](https://geopandas.org/en/stable/): For geospatial visualization.
- [**Canva**](https://www.canva.com/): For infographic creation.
