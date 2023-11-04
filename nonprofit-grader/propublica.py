import requests
import pandas as pd

baseurl = "https://projects.propublica.org/nonprofits/api/v2"


def get_ein(orgname: str) -> str:
    """
    Get the EIN for an organization.
    """
    url = f"{baseurl}/search.json?q={orgname}"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Error getting EIN for {orgname}.")
    data = response.json()
    if data["total_results"] == 0:
        raise Exception(f"No results for {orgname}.")
    return data["organizations"][0]["ein"]


def get_org_data(ein: str) -> dict:
    """
    Get the data for an organization.
    """
    url = f"{baseurl}/organizations/{ein}.json"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Error getting data for {ein}.")
    return response.json()


def get_org_data_by_name(orgname: str) -> dict:
    """
    Get the data for an organization by name.
    """
    ein = get_ein(orgname)
    return get_org_data(ein)


def latest_pdf(orgname: str) -> str:
    """
    Get the URL for the latest 990 PDF for an organization.
    """
    data = get_org_data_by_name(orgname)
    return (
        pd.DataFrame(data["filings_with_data"])
        .dropna(subset=["pdf_url"])
        .sort_values("tax_prd_yr", ascending=False)
        ["pdf_url"].tolist()[0]
    )
