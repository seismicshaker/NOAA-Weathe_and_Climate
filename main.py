#!/usr/bin/env python3
"""


"""
import argparse
import cmd

from formatting import date_fromisoformat


def make_parser():
    """Create an ArgumentParser for this script.

    :return: A tuple of the top-level, event, and bibliography parsers.
    """
    parser = argparse.ArgumentParser(
        description="Define search criterion for ISC Bulletin."
    )
    subparsers = parser.add_subparsers(dest="cmd")

    # Add the 'hypo' subcommand parser.
    fetch = subparsers.add_parser(
        "fetch",
        description="Fetch NOAA data.",
    )
    fetch.add_argument(
        "-d",
        "--date",
        type=date_fromisoformat,
        help="Event origin date search parameter, "
        "in YYYY-MM-DD format (e.g. 2020-12-31).",
    )
    fetch.add_argument(
        "-s",
        "--start_date",
        type=date_fromisoformat,
        help="Event origin start date search parameter, "
        "in YYYY-MM-DD format (e.g. 2020-12-31).",
    )
    fetch.add_argument(
        "-e",
        "--end_date",
        type=date_fromisoformat,
        help="Event origin end date search parameter, "
        "in YYYY-MM-DD format (e.g. 2020-12-31).",
    )
    fetch.add_argument(
        "-gsoy",
        "--global_summary-year",
        action="store_true",
        help="The Global Summary of the Year (GSOY) dataset includes climate"
        + " data for several thousand locations worldwide. Data files contain"
        + " 58 climatological variables computed from the summary of the day"
        + " observations of the Global Historical Climatology Network Daily"
        + " dataset (GHCN-D).",
    )

    repl = subparsers.add_parser(
        "interactive",
        description="Start an interactive command session "
        "to repeatedly run `interact` and `query` commands.",
    )
    repl.add_argument(
        "-a",
        "--aggressive",
        action="store_true",
        help="If specified, kill the session whenever a search is modified.",
    )
    return parser, fetch, repl


class SearchShell(cmd.Cmd):
    """
    interactive search
    """

    def __init__(self):
        self.status = "working on it"


if __name__ == "__main__":
    """Run the main script."""
    parser, fetch_parser, interact_parser = make_parser()
    args = parser.parse_args()

    # Run the chosen subcommand.
    if args.cmd == "fetch":
        print("fetching")
    elif args.cmd == "interactive":
        SearchShell()
