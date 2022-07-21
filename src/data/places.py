# -*- coding: utf-8 -*-
import click
import logging
import googlemaps
import time
import jsonlines
import pandas as pd
import os
from pathlib import Path
from dotenv import find_dotenv, load_dotenv


def prepare_queries(query_list, location_list):
    """
    Prepare a list of queries for Place Search

    Parameters:
        query_list (list): A list of queries to search for. Eg ["coffee", "coffee shops", "kopi"]
        location_list (list): A list of locations to search in for each query in query_list. Eg ["bishan", "orchard", "ang mo kio"]

    Returns:
        prepared_query_list (list): A list of queries that cross-joins elements in query_list & location_list. Eg ["coffee in bishan", "coffee in orchard", ...]
    """

    prepared_query_list = [i + " in " + j for i in query_list for j in location_list]

    return prepared_query_list


def get_all_query_results(query, gmaps_client):
    """
    Returns the maximum number of results (60) for a Google Place API Text Search request
    """
    json_list = []

    # Search for places using query and save value of next_page_token
    logging.info("Requesting results for %s", query)
    response = gmaps_client.places(query=query)
    json_list.append(response.get("results"))

    next_page_token = response.get("next_page_token")

    while next_page_token is not None:
        time.sleep(2)
        response = gmaps_client.places(page_token=next_page_token)
        json_list.append(response.get("results"))
        next_page_token = response.get("next_page_token")
    else:
        logging.info("next_page_token not found. Returning list of jsons for %s", query)

    return json_list


@click.command()
@click.option(
    "--input_filepath",
    prompt=True,
    default="data/input/input.csv",
    help="Please enter the filepath of the input file",
)
def main(input_filepath):
    """
    Authenticate Onemap API using API email & password from .env file in root folder
    Get planning area and save as a csv file
    """
    logger = logging.getLogger(__name__)
    logger.info("Starting script")

    # Define variables & filepaths
    places_filepath = "data/raw/places.csv"
    places_backup_filepath = "data/raw/places_backup.jsonl"
    reviews_filepath = "data/raw/reviews.csv"
    reviews_backup_filepath = "data/raw/reviews_backup.jsonl"
    places_api_key = os.getenv("PLACES_API_KEY")

    gmaps = googlemaps.Client(key=places_api_key)
    logger.info("Gmaps client initiated")

    input_df = pd.read_csv(input_filepath, skiprows=1)

    query_list = input_df["queries"].dropna().to_list()
    location_list = input_df["locations"].dropna().to_list()

    prepared_query_list = prepare_queries(query_list, location_list)

    json_list = []
    i = 0

    # Loop through queries in prepared_query_list and save all results in df
    for query in prepared_query_list:
        json_list2 = get_all_query_results(query, gmaps_client=gmaps)
        json_list.extend(json_list2)
        i += 1

        if i % 10 == 0:
            with jsonlines.open(places_backup_filepath, "w") as writer:
                writer.write_all(json_list)
            logger.info(
                f"Places backup for query 0 - {i} saved in {places_backup_filepath}"
            )

    df_list = [pd.json_normalize(json) for json in json_list]
    df = pd.concat(df_list, axis=0, ignore_index=True)

    # Save df as a csv
    df.to_csv(places_filepath)
    logger.info("Places data saved in %s", places_filepath)

    # Get a deduplicated list of place IDs for all places with at least one review in df
    place_id_list = (
        df.loc[df["user_ratings_total"] > 0, "place_id"].drop_duplicates().tolist()
    )

    json_list = []
    df_list = []
    i = 0

    # Loop through requests for place_ids in place_id_list and save reviews in df2
    logger.info("Requesting for reviews data")
    for place_id in place_id_list:
        try:
            response = gmaps.place(place_id)
            json_list.append(response)
            i += 1

            if i % 10 == 0:
                with jsonlines.open(reviews_backup_filepath, "w") as writer:
                    writer.write_all(json_list)
                logger.info(
                    f"Reviews backup for place ID 0 - {i} saved in {reviews_backup_filepath}"
                )

            reviews_df = pd.json_normalize(response.get("result").get("reviews"))
            reviews_df["place_id"] = response.get("result").get("place_id")
            df_list.append(reviews_df)
        except NotImplementedError:
            pass

    df2 = pd.concat(df_list, axis=0, ignore_index=True)

    # Save df2 as a csv
    df2.to_csv(reviews_filepath)
    logger.info("Reviews data saved in %s", reviews_filepath)


if __name__ == "__main__":
    log_fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()
