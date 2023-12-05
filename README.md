# hackattic

<img src="/logo.png?raw=true" align="right">

Source code of my solutions to the [hackattic](https://hackattic.com/) challenges.

## Prerequisites

Python >= 3.8.

## Installation

Clone this repo, and then the usual `pip install -r requirements.txt`.

## Configuration

Either set the following environment variables or copy the `.env.example` file to `.env`:

| Name           | Type | Required?  | Default | Description                                                                                            |
|----------------|------|------------|---------|--------------------------------------------------------------------------------------------------------|
| `ACCESS_TOKEN` | str  | Yes        |         | Access token used to get problem data / give solution. See on problem's pages on the hackattic website |
| `PUBLIC_IP`    | str  | Yes and no |         | Your public IP, required for some problems                                                             |

## Usage

Simply execute one of the scripts named after the corresponding problem (e.g `python help_me_unpack.py`).
