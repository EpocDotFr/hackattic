# hackattic

<img src="https://hackattic.com/static/core/h%5E.png" align="right">

Source code of my solutions to the [hackattic](https://hackattic.com/) challenges.

## Prerequisites

Python >= 3.7.

## Installation

Clone this repo, and then the usual `pip install -r requirements.txt`.

## Configuration

Copy the `.env.example` file to `.env` and fill in the configuration parameters:

| Name           | Type | Required?  | Default | Description                                                                                            |
|----------------|------|------------|---------|--------------------------------------------------------------------------------------------------------|
| `ACCESS_TOKEN` | str  | Yes        |         | Access token used to get problem data / give solution. See on problem's pages on the hackattic website |
| `PUBLIC_IP`    | str  | Yes and no |         | Your public IP, required for some problems                                                             |

## Usage

Simply execute one of the scripts named after the corresponding problem (e.g `python help_me_unpack.py`).