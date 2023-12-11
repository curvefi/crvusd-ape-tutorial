import logging
import time
from datetime import datetime

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from ape import Contract, chain

# Configuration
TEST_MODE = True
CONTROLLER_ADDRESS = "0x4e59541306910ad6dc1dac0ac9dfb29bd9f15c67"  # WBTC Controller
USER_ADDRESS = "0xda9550086Cd641F515654a857Dd357E982589CFD"
START_BLOCK = 17557475
TEST_RESOLUTION = 20
PROD_RESOLUTION = 1000
start_time = time.time()

# Set the logging level to CRITICAL to suppress lower-level messages
# XXX

# Initialize contracts
controller = Contract(CONTROLLER_ADDRESS)
amm = Contract(controller.amm())


def main():
    """
    Main function to process user data, save it to a CSV file, and plot the data.
    It processes health, AMM prices, band bounds, and user state values over a range of blocks.
    """

    # Configure scraping window
    end_block = # XXX
    resolution = TEST_RESOLUTION if TEST_MODE else PROD_RESOLUTION

    # Main loop
    data = process_user_data(USER_ADDRESS, START_BLOCK, end_block, resolution)
    save_data_to_csv(data)
    print(f"Runtime: {format_time(time.time() - start_time)} ")

    # Plot results
    plot_data(data)


def process_user_data(user, start, end, resolution):
    """
    Processes and collects data for a given user over a specified range of blocks.

    :param user: User address to process.
    :param start: Start block number.
    :param end: End block number.
    :param resolution: The number of points to sample between start and end.
    :return: Dictionary containing the updated dataframe_data and a dictionary with times, 
            health_values, amm_prices, lower_band, upper_band, and user_state_values.
    """

    print(f"Processing {user}")
    data = {
        "times": [],
        "health_values": [],
        "amm_prices": [],
        "lower_band": [],
        "upper_band": [],
        "user_state": [],
    }

    blocks_processed = 0

    for block in np.linspace(start, end - 1, resolution, dtype=int):
        # Log current progress
        blocks_processed += 1
        percent_complete = (blocks_processed / resolution) * 100
        elapsed_time = time.time() - start_time
        avg_time_per_block = elapsed_time / blocks_processed
        estimated_time_remaining = avg_time_per_block * (resolution - blocks_processed)
        formatted_time_remaining = format_time(estimated_time_remaining)

        print(
            f"\rProcessing block {block} / {end}.\r{percent_complete:.1f}% complete. " +
            f"Estimated time remaining: {formatted_time_remaining}    ",
            end="",
        )
        t, h, n1, n2, amm_price, user_state = process_block(user, block)
        data["times"].append(t)
        data["health_values"].append(h)
        data["amm_prices"].append(amm_price)

        p_current_down = amm.p_oracle_down(n1) / 1e18 if n1 is not None else np.nan
        p_current_up = amm.p_oracle_up(n2) / 1e18 if n2 is not None else np.nan
        data["lower_band"].append(p_current_down)
        data["upper_band"].append(p_current_up)

        if user_state[0] is not None and user_state[1] is not None:
            data["user_state"].append(user_state[1] / (user_state[0] + user_state[1]))
        else:
            data["user_state"].append(None)

    return data


def process_block(user, block):
    """
    Processes data for a given user at a specific block.

    :param user: User address to process.
    :param block: The block number to process.
    :return: Tuple containing health, n1, n2, AMM price, and user state data at the given block.
    """
    block = int(block)
    try:
        h = controller.health(user, True, block_identifier=block) / 1e18 * 100
        n1, n2 = amm.read_user_tick_numbers(user, block_identifier=block)
        amm_price = controller.amm_price(block_identifier=block) / 1e18
        user_state = controller.user_state(user, block_identifier=block)
    except Exception as e:
        h, n1, n2, amm_price, user_state = None, None, None, None, [None] * 4

    return block, h, n1, n2, amm_price, user_state


def plot_data(data):
    """
    Plots and displays multiple charts including health, AMM prices, band bounds, and user state data.

    :param data: Dictionary containing scraped data to be plotted
    """

    # Number of plots (0 for AMM price and bands, 1 for health, 2 for user_state values)
    num_plots = 3
    fig, axs = plt.subplots(
        num_plots, 1, figsize=(15, 10)
    )  # Adjust figure size to fit in one window

    # Plot AMM Price and Band Bounds
    band_color = "#789F8A"  # Greenish-grey
    axs[0].plot(data["times"], data["amm_prices"], label="AMM Price", color="tab:green")
    axs[0].plot(data["times"], data["lower_band"], color=band_color, linestyle="--")
    axs[0].plot(data["times"], data["upper_band"], color=band_color, linestyle="--")
    axs[0].fill_between(
        data["times"],
        data["lower_band"],
        data["upper_band"],
        color=band_color,
        alpha=0.3,
    )
    axs[0].set_title("AMM Price and User Bands")
    axs[0].set_ylabel("Price")

    # Plot Health
    axs[1].plot(data["times"], data["health_values"], color="tab:red")
    axs[1].set_title("Health")
    axs[1].set_ylabel("Health (%)")

    # Plot User State
    axs[2].plot(data["times"], data["user_state"], color="tab:blue")
    axs[2].set_title("Collateral Composition")
    axs[2].set_ylabel("% in Stablecoins")

    # Set x-label for the last subplot
    axs[-1].set_xlabel("Time (blocks)")

    plt.tight_layout()
    plt.show()


def save_data_to_csv(data):
    """
    Saves the provided data into a CSV file.

    :param data: Dictionary containing various time-series data.
    """
    # Prepare DataFrame
    df = pd.DataFrame(data)
    df.insert(0, "User", USER_ADDRESS)  # Add a column for the user address

    # Save to CSV
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"data/data{'_test' if TEST_MODE else '_prod'}/{USER_ADDRESS[0:8]}_{timestamp}.csv"
    df.to_csv(filename, index=False)
    print(f"\rData saved to {filename}")


def format_time(seconds):
    """
    Converts seconds into a more readable format (days, hours, minutes, seconds).

    :param seconds: Time in seconds.
    :return: Formatted time string.
    """
    days, seconds = divmod(seconds, 86400)
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)
    time_format = ""
    if days > 0:
        time_format += f"{int(days)}d "
    if hours > 0:
        time_format += f"{int(hours)}h "
    if minutes > 0:
        time_format += f"{int(minutes)}m "
    time_format += f"{int(seconds)}s"
    return time_format


if __name__ == "__main__":
    main()
