#!/usr/bin/env python

import argparse
import logging
from PyESMTool import ADF, ILAMB, xesmf_clm_fates_diagnostics

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

def run_adf(config):
    """Run the ADF (Analysis Diagnostics Framework) module."""
    logger.info("Running ADF module...")
    try:
        ADF.run(config)
        logger.info("ADF module completed successfully.")
    except Exception as e:
        logger.error(f"ADF module failed: {e}")


def run_ilamb(config):
    """Run the ILAMB (International Land Model Benchmarking) module."""
    logger.info("Running ILAMB module...")
    try:
        ILAMB.run(config)
        logger.info("ILAMB module completed successfully.")
    except Exception as e:
        logger.error(f"ILAMB module failed: {e}")


def run_xesmf_clm_fates_diagnostics(config):
    """Run the xESMF CLM-FATES diagnostics module."""
    logger.info("Running xESMF CLM-FATES diagnostics module...")
    try:
        xesmf_clm_fates_diagnostics.run(config)
        logger.info("xESMF CLM-FATES diagnostics module completed successfully.")
    except Exception as e:
        logger.error(f"xESMF CLM-FATES diagnostics module failed: {e}")


def main():
    """Main function to parse arguments and run selected submodules."""
    parser = argparse.ArgumentParser(description="A wrapper script for NorESM diagnostic packages.")

    parser.add_argument("--config", type=str, required=True, help="Path to the configuration file for the selected module.")
    parser.add_argument("-m", "--module", type=str, choices=["adf", "ilamb", "xclm", "all"], required=True, help="Specify the diagnostics module (REQUIRED). Valid arguments: adf, xclm, ilamb,..., all.")
    parser.add_argument("-c", "--case", "--case1", type=str, help="Test case simulation (OPTIONAL).")
    parser.add_argument("-s", "--start_yr", "--start_yr1", type=int, help="Start year of test case climatology (OPTIONAL).")
    parser.add_argument("-e", "--end_yr", "--end_yr1", type=int, help="End year of test case climatology (OPTIONAL).")
    parser.add_argument("-i", "--input-dir", "--input-dir1", type=str, help="Specify the directory where the test case history files are located (OPTIONAL). Default is $HISTORY_PATH1.")
    parser.add_argument("-o", "--output-dir", type=str, help="Specify the directory where the climatology and time-series files should be stored (OPTIONAL). Default is $DIAG_PATH.")
    parser.add_argument("-w", "--web-dir", type=str, help="Specify the directory where the HTML should be published (OPTIONAL). Default is $WEB_PATH.")

    args = parser.parse_args()

    # Dispatch to the appropriate module based on the user's choice
    if args.module == "ADF":
        run_adf(args.config)
    elif args.module == "ILAMB":
        run_ilamb(args.config)
    elif args.module == "xesmf":
        run_xesmf_clm_fates_diagnostics(args.config)
    else:
        logger.error("Unknown module selected. Please choose from ADF, ILAMB, or xesmf.")

if __name__ == "__main__":
    main()

