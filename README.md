# The Kopi / Latte Ratio

## What is the underlying problem we are trying to solve?
There are two kinds of coffee served by eateries in Singapore - kopi, a rich concoction made with dark-roasted Robusta coffee beans and a hearty serving of condensed milk. And latte (or cuppucino, mocha etc), a more nuanced coffee beverage consisting of an espresso shot pulled from fresh Arabica beans and creamy steamed milk.

As a coffee fan, I'm interested to understand what are the preferences of the local population in Singapore when it comes to coffee. A straightforward way to answer this question would be to conduct surveys to get a general popularity of each drink. But I'm also interested in the landscape of coffee in terms of geography. Which areas in Singapore are kopis or lattes more favoured?

Questions to solve:
- Do Singaporeans prefer kopi or latte? How much more do they prefer one drink over the other?
- Are there differences in preferences across areas in Singapore? 
- If I planning to start a cafe, where should I open my new hipster fourth-wave Nordic-roasted specialty coffee salon? 

## How will success be measured? 
An easy to read visualisation of the insights obtained from the analysis
A public github project that is well-organised following data science best practices

## Are there specific goals?
To build up on the following skills
- Version control with Git & Github
- Data science project planning & processes
- Working with Google Places API for data collection
- Geospatial data visualisation using geopandas

## What should the team not do?
- Spend too much time fussing over details 

## Who are the stakeholders?
Recruiters, people in the data industry

# Deliverables
## Data Visualisation
- A map of Singapore with the kopi/latte ratio calculated by planning areas
- A bar graph showing the 5 highest & lowest kopi latte areas in Singapore
- Dataframe of kopi/latte ratio by planning areas

## Reproducible Analysis
- .py scripts for extracting, transforming & pulling data in a reproducible manner
- Public git repo 

# Approach
We will be using the  CRISP-DM model for the project
- Business understanding – What does the business need?
- Data understanding – What data do we have / need? Is it clean?
- Data preparation – How do we organize the data for modeling?
- Data Visualisation – What data visualisation techniques should we apply?
- Evaluation – Which model best meets the business objectives?
- Deployment – How do stakeholders access the results?

## Business Understanding
- Project planning
- Set up project folder (Cookie cutter)
- Set up credentials for Google Cloud project
- Set up Git repo
- Set up One Map credentials

## Data Understanding
- Learn Google Place API
- Extract data from Google Place API
- Check data structure and validate
- Learn One Map API
- Pull planning area polygons


## Data Preparation
- Clean data by categorising places into cafes or coffee shops
- Clean up geolocation data of row
- Group data by planning area
- Calculate Kopi / Latte ratio by planning area
- Output: Dataframe with Kopi / Latte ratio by planning area

## Data Visualisation
- Plot a visual map of Singapore & Kopi / Latte ratio by planning area
- Bar graph showing the 5 highest & lowest kopi latte areas in Singapore
- Infographic on:
    - Project introduction
    - Overall Kopi / Latte ratio
    - Map visualisation
