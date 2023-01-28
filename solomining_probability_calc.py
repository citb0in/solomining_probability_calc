#!/usr/bin/env python3
##########################################
#         2023/Jan/28 by citb0in         #
#       https://github.com/citb0in       #
#                                        #
#   This project is licensed under the   #
#       terms of the GPLv3 license.      #
##########################################
import requests
import re

####################
# Some global vars #
####################

# Uncomment following line(s) for manually seting the difficulty/netrate to a value of your choice
#diff = 123456789.1234
#netrate = 77889900112233.555

# Number of chars to print as horizontal line separator, on a widescreen you could try 200
sep = 150

###########################
# Definitions (functions) #
###########################

def get_diff_and_netrate(diff_from_api=False,netrate_from_api=False):
    """Function for getting the current Bitcoin difficulty and network hashrate from API"""
    global diff
    global netrate
    if 'diff' not in globals() or 'netrate' not in globals():
        response = requests.get("https://mempool.space/api/v1/mining/hashrate/3d")
        print("Executing API query to retrieve some Bitcoin network information ...\n")
        if response.status_code != 200:
            raise Exception("Failed to retrieve data from API")
        if 'diff' not in globals():
            diff = response.json()["currentDifficulty"]
            diff_from_api = True
        if 'netrate' not in globals():
            netrate = response.json()["currentHashrate"]
            netrate_from_api = True
    return diff, netrate, diff_from_api, netrate_from_api

def get_proportion_of_netrate(hashrate):
    """Function to set the hashrate of the solominer in relation to the total network rate"""
    proportion = hashrate_raw / netrate * 100
    if "e-" in str(proportion):
        precision = 1
        netrate_prec = int(str(proportion).split("e-")[1]) + precision
    else:
        netrate_prec = re.search(r"[1-9]", str(proportion)).start()
    return proportion, netrate_prec

def format_input(hashrate_raw):
    """Function for formatting the input hashrate"""
    hashrate_match = re.match(r'^\s*([0-9]+(?:\.[0-9]+)?)\s*([KMGTPEZY]?)\s*(H)?\s*(\/)?\s*(s|sec)?\s*$', hashrate_raw, flags=re.IGNORECASE)
    if hashrate_match:
        hashrate_nounit = float(hashrate_match.group(1))
        hashrate_unit = hashrate_match.group(2).upper()
        conversions = {'K': 1e3, 'M': 1e6, 'G': 1e9, 'T': 1e12, 'P': 1e15, 'E': 1e18, 'Z': 1e21, 'Y': 1e24}
        if hashrate_unit in conversions:
            hashrate_raw = hashrate_nounit*conversions[hashrate_unit]
        else:
            hashrate_raw = hashrate_nounit
    else:
        return None
    return hashrate_nounit, hashrate_unit, hashrate_raw

def scale_unit(value):
    """Function for scaling to highest possible unit"""
    units = ['', 'K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y']
    value = str(value)
    prefix = ''
    if ' ' in value:
        value, prefix = value.split()
    exponent = 0
    while float(value) >= 1000:
        value = str(float(value) / 1000)
        exponent += 1
    return f"{float(value):.2f} {units[exponent]}{prefix}"

def calculate_probability(hashrate):
    """Function for calculating the probability per block avg. time of 10min for use as a base"""
    expected_blockhit_time = diff * 2**48 / 0xffff / hashrate_raw / 3600
    expected_blockhit_rel_net = netrate / hashrate_raw * 600
    prob_per_10min = hashrate_raw / (diff * 2**48 / 0xffff) * 600
    prob_per_block = prob_per_10min
    if "e-" in str(prob_per_10min):
        # Number of desired additional decimal places
        # beginning from first occurring decimal place not equal to zero
        precision = 2
        prob_prec = int(str(prob_per_10min).split("e-")[1]) + precision
    else:
        prob_prec = 3
    # Define some additional time units
    prob_per_hour = prob_per_block * 6
    prob_per_day = prob_per_hour * 24
    prob_per_week = prob_per_day * 7
    prob_per_month = prob_per_day * 30
    prob_per_halfyear = prob_per_day * 182.5
    prob_per_year = prob_per_day * 365
    return expected_blockhit_time, expected_blockhit_rel_net, prob_per_block, prob_per_hour, prob_per_day, prob_per_week, prob_per_month, prob_per_halfyear, prob_per_year, prob_prec, netrate_prec

def probability_phrase(probability):
    if probability <= 0.00001:
        return "more likely than getting struck by lightning"
    elif probability <= 0.0001:
        return "less likely than winning the lottery"
    elif probability <= 0.45:
        return "the odds are stacked against it"
    elif probability <= 0.55:
        return "about as likely as flipping a coin and getting heads"
    elif probability <= 0.00001:
        return "more likely than finding a needle in a haystack"
    elif probability <= 0.001:
        return "about as likely as getting a hole-in-one in golf"
    elif probability <= 0.000001:
        return "similar likelihood as finding a specific grain of sand on a beach"
    elif probability <= 0.001:
        return "as likely as getting a perfect score in a game of darts"
    elif probability <= 0.5:
        return "unlikely"
    else:
        return "more likely than not"

def describe_probability(prob):
    if prob >1:
        return "a guarantee, a 100% sure thing - you can bet your last dollar on it. It's gonna happen soon YEAH!!!"
    if prob >= 0.99 and prob <= 1:
        return "virtually certain, almost a guarantee - it's similar to the probability of the sun rising tomorrow."
    elif prob >= 0.98 and prob < 0.99:
        return "extremely likely, almost a sure thing - it's similar to the probability of a football team winning a game when they're up by 14 points with 2 minutes left."
    elif prob >= 0.95 and prob < 0.98:
        return "very likely, highly probable - it's similar to the probability of a baseball pitcher throwing a strike with a 3-2 count."
    elif prob >= 0.9 and prob < 0.95:
        return "likely, it's quite probable - it's similar to the probability of a golfer making a 5-foot putt."
    elif prob >= 0.8 and prob < 0.9:
        return "more likely than not - it's similar to the probability of a basketball team making a free throw."
    elif prob >= 0.7 and prob < 0.8:
        return "somewhat likely - it's similar to the probability of a football team scoring a touchdown on a red-zone drive."
    elif prob >= 0.6 and prob < 0.7:
        return "about as likely as not - it's similar to the probability of a weather forecast predicting rain and it actually raining."
    elif prob >= 0.5 and prob < 0.6:
        return "about as likely as not - it's similar to the likelihood of flipping a coin and getting heads on the first try."
    elif prob >= 0.4 and prob < 0.5:
        return "somewhat likely - it's similar to the probability of drawing a red card from a standard deck of playing cards"
    elif prob >= 0.3 and prob < 0.4:
        return "less likely than not - it's similar to the probability of a baseball team winning a game when they're trailing by 4 runs in the bottom of the 9th inning."
    elif prob >= 0.2 and prob < 0.3:
        return "unlikely, quite improbable - it's similar to the probability of guessing the correct combination on a three-digit lock on the first try."
    elif prob >= 0.1 and prob < 0.2:
        return "very unlikely, highly improbable - it's like the likelihood of getting a specific number when rolling a fair die."
    elif prob >= 0.01 and prob < 0.1:
        return "extremely unlikely - it's like flipping a coin and getting heads 10 times in a row."
    elif prob >= 0.001 and prob < 0.01:
        return "virtually impossible - it's like flipping a coin and getting heads 100 times in a row."
    elif prob >= 0.0001 and prob < 0.001:
        return "virtually impossible - it's more likely to be struck by lightning twice in the same place or being dealt a royal flush in poker on the first hand."
    elif prob >= 0.00005 and prob < 0.0001:
        return "virtually impossible - it's more likely to get hit by lightning in a lifetime."
    elif prob >= 0.00001 and prob < 0.00005:
        return "virtually impossible - it's like a specific individual being struck by lightning multiple times in their lifetime."
    elif prob >= 0.000001 and prob < 0.00001:
        return "virtually impossible - it's like the likelihood of winning a prize in a sweepstakes with 1 in 10 million chances."
    elif prob >= 0.0000005 and prob < 0.000001:
        return "virtually impossible - it's like the likelihood of getting a specific combination of five numbers on a slot machine."
    elif prob >= 0.00000005 and prob < 0.0000005:
        return "virtually impossible - it's more likely to win the Powerball lottery jackpot or Mega Millions."
    elif prob < 0.00000005:
        return "infinitesimally small - it's similar to the probability of finding a specific atom among all the atoms in the universe."
    else:
        return "questionable?!"

#######################################
# Program flow / variable assignments #
#######################################

# User input hash rate
hashrate_input = input("Enter the hashrate/sec of your solo miner: ")

# Call the functions and fill the variables
diff, netrate, diff_from_api, netrate_from_api = get_diff_and_netrate()
diff_formatted, netrate_formatted = scale_unit(diff), scale_unit(netrate)+"H/s"
hashrate_nounit, hashrate_unit, hashrate_raw = format_input(hashrate_input)
proportion, netrate_prec = get_proportion_of_netrate(hashrate_raw)
expected_blockhit_time, expected_blockhit_rel_net, prob_per_block, prob_per_hour, prob_per_day, prob_per_week, prob_per_month, prob_per_halfyear, prob_per_year, prob_prec, netrate_prec = calculate_probability(hashrate_raw)


##########
# Output #
##########

print(f"{'Manually set Bitcoin difficulty:' if not diff_from_api else 'Current Bitcoin difficulty is:'} {diff:,.3f} ({diff_formatted})\n{'Manually set Bitcoin network hashrate:' if not netrate_from_api else 'Current Bitcoin overall network hashrate is:'} {netrate:,.2f} ({netrate_formatted})")
print(f'\nEntered hash rate of {hashrate_nounit} {hashrate_unit}H/sec equals to: {hashrate_raw:,.2f} hashes/sec\nThe ratio of the solo mining hash rate related to the total network hash rate is: {proportion:,.{netrate_prec}f} %\n')
print('=' * sep)

# Display probability as decimal value, percentage, "1 in x" format and as description / analogy text
print(f'Probability per 10min: {prob_per_block:,.{prob_prec}f} ({prob_per_block*100:,.{prob_prec}f} %) or 1 in {1/prob_per_block:,.0f}')
print(f'\nIn words: The chance of mining a block with the given hashrate within a 10min period is similar to the probability of picking a red winning ball from a jar containing {int(round(1/prob_per_block,0)):,} white balls. Or: The probability of such an event happening is {str(describe_probability(prob_per_block))}')
print('=' * sep)
print(f'Probability per hour: {prob_per_hour:,.{prob_prec}f} ({prob_per_hour*100:,.2f} %) or 1 in {1/prob_per_hour:,.0f}')
print(f'\nIn words: The chance of mining a block with the given hashrate within an hour is similar to the probability of picking a red winning ball from a jar containing {int(round(1/prob_per_hour,0)):,} white balls. Or: The probability of such an event happening is {str(describe_probability(prob_per_hour))}')
print('=' * sep)
print(f'Probability per day: {prob_per_day:,.{prob_prec}f} ({prob_per_day*100:,.2f} %) or 1 in {1/prob_per_day:,.0f}')
print(f'\nIn words: The chance of mining a block with the given hashrate within a day is similar to the probability of picking a red winning ball from a jar containing {int(round(1/prob_per_day,0)):,} white balls. Or: The probability of such an event happening is {str(describe_probability(prob_per_day))}')
print('=' * sep)
print(f'Probability per week: {prob_per_week:,.{prob_prec}f} ({prob_per_week*100:,.2f} %) or 1 in {1/prob_per_week:,.0f}')
print(f'\nIn words: The chance of mining a block with the given hashrate within a week is similar to the probability of picking a red winning ball from a jar containing {int(round(1/prob_per_week,0)):,} white balls. Or: The probability of such an event happening is {str(describe_probability(prob_per_week))}')
print('=' * sep)
print(f'Probability per month: {prob_per_month:,.{prob_prec}f} ({prob_per_month*100:,.2f} %) or 1 in {1/prob_per_month:,.0f}')
print(f'\nIn words: The chance of mining a block with the given hashrate within a month is similar to the probability of picking a red winning ball from a jar containing {int(round(1/prob_per_month,0)):,} white balls. Or: The probability of such an event happening is {str(describe_probability(prob_per_month))}')
print('=' * sep)
print(f'Probability per half-year: {prob_per_halfyear:,.{prob_prec}f} ({prob_per_halfyear*100:,.2f} %) or 1 in {1/prob_per_halfyear:,.0f}')
print(f'\nIn words: The chance of mining a block with the given hashrate within a half-year is similar to the probability of picking a red winning ball from a jar containing {int(round(1/prob_per_halfyear,0)):,} white balls. Or: The probability of such an event happening is {str(describe_probability(prob_per_halfyear))}')
print('=' * sep)
print(f'Probability per year: {prob_per_year:,.{prob_prec}f} ({prob_per_year*100:,.2f} %) or 1 in {1/prob_per_year:,.0f}')
print(f'\nIn words: The chance of mining a block with the given hashrate within a year is similar to the probability of picking a red winning ball from a jar containing {int(round(1/prob_per_year,0)):,} white balls. Or: The probability of such an event happening is {str(describe_probability(prob_per_year))}')
print('=' * sep)
print(f'Expected average time to hit a block:\n{expected_blockhit_time*3600:,.1f} sec = {expected_blockhit_time*60:,.1f} min = {expected_blockhit_time:,.1f} h = {expected_blockhit_time/24:,.1f} days = {expected_blockhit_time/24/7:,.1f} weeks = {expected_blockhit_time/24/7/4.34:,.1f} months = {expected_blockhit_time/24/7/4.34/12:,.1f} years\n')
print(f'Expected average time (relative to overall network):\n{expected_blockhit_rel_net:,.1f} sec = {expected_blockhit_rel_net/60:,.1f} min = {expected_blockhit_rel_net/60/60:,.1f} h = {expected_blockhit_rel_net/60/60/24:,.1f} days = {expected_blockhit_rel_net/60/60/24/7:,.1f} weeks = {expected_blockhit_rel_net/60/60/24/7/4.34:,.1f} months = {expected_blockhit_rel_net/60/60/24/7/4.34/12:,.1f} years')
print('=' * sep)
