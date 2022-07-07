# -*- coding: utf-8 -*-
import click
import logging
import requests
import pandas as pd
import json
import os
from pathlib import Path
from dotenv import find_dotenv, load_dotenv


def get_token(api_email, api_password):
    """
    Gets Onemap token using Onemap API email address & password
    """
    url = "https://developers.onemap.sg/privateapi/auth/post/getToken"
    response = requests.post(url, data={"email": api_email, "password": api_password})

    access_token = response.json().get("access_token")
    return access_token


def get_planning_areas(access_token, planning_year=2014):
    """
    Get URA planning area from Onemap API for selected URA Planning Year
    """
    url = "https://developers.onemap.sg/privateapi/popapi/getAllPlanningarea"
    payload = {"token": access_token, "year": planning_year}
    response = requests.get(url, params=payload)

    # Parse json response and normalise into a df
    df = pd.json_normalize(response.json()).fillna("{}")

    # 'geojson' df column is nested. Apply json.loads to the column to convert type from object to string
    geojson = pd.DataFrame(df["geojson"].apply(json.loads).values.tolist())

    # Join unnested geojson columns back to original df
    df2 = df.join(geojson).drop(columns={"geojson"})
    return df2


@click.command()
def main():
    """
    Authenticate Onemap API using API email & password from .env file in root folder
    Get planning area and save as a csv file
    """
    logger = logging.getLogger(__name__)
    logger.info("Starting script")
    onemap_email = os.getenv("ONEMAP_ACCOUNT_EMAIL")
    onemap_password = os.getenv("ONEMAP_ACCOUNT_PASSWORD")

    access_token = get_token(onemap_email, onemap_password)
    logger.info("Access token granted")

    df = get_planning_areas(access_token, 2014)

    df.to_csv("data/raw/planning_areas.csv")
    logger.info("Planning area csv saved")


if __name__ == "__main__":
    log_fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()
