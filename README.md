<a name="readme-top"></a>
  <h1 align="center">Solomining Probability Calculator, by citb0in</h1>
<div align="center">
  <p align="center">
    <br />
    <a href="https://github.com/citb0in/solomining_probability_calc/issues">Report Bug</a>
    ·
    <a href="https://github.com/citb0in/solomining_probability_calc/issues">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This small tool was created as a result of [this discussion on bitcointalk.org](https://bitcointalk.org/index.php?topic=5437062.0).

The "Solomining Probability Calculator" is a tool designed to assist solo miners in understanding their chances of successfully mining a block on the Bitcoin network. The program takes the user's hash rate as input, supporting various formats for ease of use. It also retrieves the current Bitcoin network difficulty which is then used to calculate a range of important mining metrics. These include the ratio of all hashes over the valid hashes, the probability of each single hash attempt, expected time to mine a block and the probability of successfully mining a block for various time frames. Additionally, the program offers helpful analogy and phrases to provide a better human-understanding of the probabilities, making it easier for users to interpret the results. With this tool, solo miners can gain valuable insights into their mining operations and make more informed decisions. Overall, the solomining probability calculator is a valuable tool for any solo miner looking to increase their chances of success in the competitive world of cryptocurrency mining.

If you found this project useful and helpful, please consider making a donation to my bitcoin address bc1qycq57rtc2rjgslqk8kehjequ9z5egane**thanks** to support its continued development and maintenance. Your support is greatly appreciated and will go a long way in ensuring that this project continues to be a valuable resource for others. Thank you for your generosity!

<p align="right">(<a href="#readme-top">back to top</a>)</p>


### Built With

Python3 on GNU/Linux

[![Python3][Python3.com]][Python3-url]


<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

Note: Python2 is not supported.

* Python3 libs
```requests, re```

### Installation

1. Ensure you are running Python3
   ```sh
   python3 -V
   ```

2. Clone this repository
   ```sh
   git clone https://github.com/citb0in/solomining_probability_calc.git
   ```
   
3. Either make the python program executable
   ```sh
   chmod +x ./solomining_probability_calc.py
   ```
   and run it by
   ```sh
   ./solomining_probability_calc.py
   ```
   
   or just execute it by
   ```sh
   python3 solomining_probability_calc.py
   ```
<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Usage

The program is started without parameters, after which the user is prompted to enter the solomining hashrate. Various formats are supported, the input is case-insensitive. The input requires an integer or floating number. You can provide one of the following available letters representing the corresponding units: (K)ilo, (M)ega, (G)iga, (T)era, (P)eta, (E)xa, (Z)etta, (Y)otta. You can add the letter 'h' or 'H' for hashes, you can add the slash character '/' and you can add the the letter 's' or 'S' or 'sec' or 'sEc' for seconds. You can use whitespaces and any combinations of those. If the unit is omitted then the input is evaluated as hashes/sec. After program start, both the hash rate entered by the user and the hash rate evaluated by the program are displayed for checking.

Examples:

Value followed by the unit as a single letter
  ```sh
  350g
  ```
  
Value followed by the unit as a single uppercase letter
  ```sh
  73M
  ```

Value followed by a space followed by the unit as a single uppercase letter
  ```sh
  10 T
  ```

Value followed by the lowercase unit-hashes abbreviation
  ```sh
  50ph
  ```

Float value followed by the unit-hashes-second abbreviation
  ```sh
  5.78phs
  ```

Float value followed by the unit-hashes per second abbreviation
  ```sh
  12.77Eh/s
  ```

Whitespace followed by a number followed by an uppercase unit letter followed by the uppercase S
  ```sh
   2.558 p H S
  ```

Or some weird input styles
  ```sh
         1234.56     T   h          /   sec
	    1234.56 p     / s  
  ```

... you get the idea, right?



## Output example for 140 TH/s @2023/Jan/28
```
Enter the hashrate/sec of your solo miner: 140t
Executing API query to retrieve some Bitcoin network information ...

Current Bitcoin difficulty is: 37,590,453,655,497.094 (37.59 T)
Current Bitcoin overall network hashrate is: 281,754,256,197,767,004,160.00 (281.75 EH/s)

Ratio of all hashes over the valid hashes means that:
1 hash in 161,452,232,657,725,468,704,768 results in a valid block.
Or each single hash attempt has a chance of 0.000000000000000000000006193782 %
==================================================================================================
Entered hash rate of 140.0 TH/sec equals to: 140,000,000,000,000.00 hashes/sec
The ratio of the solo mining hash rate related to the total network hash rate is: 0.000050 %

==================================================================================================
Probability per 10min: 0.000000520 (0.000052028 %) or 1 in 1,922,050

In words: The chance of mining a block with the given hashrate within a 10min period is similar
to the probability of picking a red winning ball from a jar containing 1,922,050 white balls.
Or: The probability of such an event happening is virtually impossible - it's like the likelihood
of getting a specific combination of five numbers on a slot machine.
==================================================================================================
Probability per hour: 0.000003122 (0.00 %) or 1 in 320,342

In words: The chance of mining a block with the given hashrate within an hour is similar to the
probability of picking a red winning ball from a jar containing 320,342 white balls. Or:
The probability of such an event happening is virtually impossible - it's like the likelihood of
winning a prize in a sweepstakes with 1 in 10 million chances.
==================================================================================================
Probability per day: 0.000074920 (0.01 %) or 1 in 13,348

In words: The chance of mining a block with the given hashrate within a day is similar to the
probability of picking a red winning ball from a jar containing 13,348 white balls.
Or: The probability of such an event happening is virtually impossible - it's more likely to
get hit by lightning in a lifetime.
==================================================================================================
Probability per week: 0.000524440 (0.05 %) or 1 in 1,907

In words: The chance of mining a block with the given hashrate within a week is similar to the
probability of picking a red winning ball from a jar containing 1,907 white balls. Or: The
probability of such an event happening is virtually impossible - it's more likely to be struck by
lightning twice in the same place or being dealt a royal flush in poker on the first hand.
==================================================================================================
Probability per month: 0.002247600 (0.22 %) or 1 in 445

In words: The chance of mining a block with the given hashrate within a month is similar to the
probability of picking a red winning ball from a jar containing 445 white balls. Or:
The probability of such an event happening is virtually impossible - it's like flipping a coin and
getting heads 100 times in a row.
==================================================================================================
Probability per half-year: 0.013672899 (1.37 %) or 1 in 73

In words: The chance of mining a block with the given hashrate within a half-year is similar to the
probability of picking a red winning ball from a jar containing 73 white balls. Or:
The probability of such an event happening is extremely unlikely - it's like flipping a coin and
getting heads 10 times in a row.
==================================================================================================
Probability per year: 0.027345797 (2.73 %) or 1 in 37

In words: The chance of mining a block with the given hashrate within a year is similar to the
probability of picking a red winning ball from a jar containing 37 white balls. Or:
The probability of such an event happening is extremely unlikely - it's like flipping a coin and
getting heads 10 times in a row.
==================================================================================================
Expected average time to hit a block:
1,153,230,233.3 sec = 19,220,503.9 min = 320,341.7 h = 13,347.6 days = 1,906.8 weeks = 439.4 months = 36.6 years

Expected average time (relative to overall network):
1,207,518,240.8 sec = 20,125,304.0 min = 335,421.7 h = 13,975.9 days = 1,996.6 weeks = 460.0 months = 38.3 years
==================================================================================================
```


## Output example for 50 PH/s @2023/Jan/28
```
Enter the hashrate/sec of your solo miner: 50 PH
Executing API query to retrieve some Bitcoin network information ...

Current Bitcoin difficulty is: 37,590,453,655,497.094 (37.59 T)
Current Bitcoin overall network hashrate is: 281,754,256,197,767,004,160.00 (281.75 EH/s)

Ratio of all hashes over the valid hashes means that:
1 hash in 161,452,232,657,725,468,704,768 results in a valid block.
Or each single hash attempt has a chance of 0.000000000000000000000006193782 %
==================================================================================================
Entered hash rate of 50.0 PH/sec equals to: 50,000,000,000,000,000.00 hashes/sec
The ratio of the solo mining hash rate related to the total network hash rate is: 0.018 %

==================================================================================================
Probability per 10min: 0.000 (0.019 %) or 1 in 5,382

In words: The chance of mining a block with the given hashrate within a 10min period is similar to
the probability of picking a red winning ball from a jar containing 5,382 white balls. Or:
The probability of such an event happening is virtually impossible - it's more likely to be struck
by lightning twice in the same place or being dealt a royal flush in poker on the first hand.
==================================================================================================
Probability per hour: 0.001 (0.11 %) or 1 in 897

In words: The chance of mining a block with the given hashrate within an hour is similar to the
probability of picking a red winning ball from a jar containing 897 white balls. Or:
The probability of such an event happening is virtually impossible - it's like flipping a coin and
getting heads 100 times in a row.
==================================================================================================
Probability per day: 0.027 (2.68 %) or 1 in 37

In words: The chance of mining a block with the given hashrate within a day is similar to the
probability of picking a red winning ball from a jar containing 37 white balls. Or:
The probability of such an event happening is extremely unlikely - it's like flipping a coin and
getting heads 10 times in a row.
==================================================================================================
Probability per week: 0.187 (18.73 %) or 1 in 5

In words: The chance of mining a block with the given hashrate within a week is similar to the
probability of picking a red winning ball from a jar containing 5 white balls. Or:
The probability of such an event happening is very unlikely, highly improbable - it's like the
likelihood of getting a specific number when rolling a fair die.
==================================================================================================
Probability per month: 0.803 (80.27 %) or 1 in 1

In words: The chance of mining a block with the given hashrate within a month is similar to the
probability of picking a red winning ball from a jar containing 1 white balls. Or:
The probability of such an event happening is more likely than not - it's similar to the
probability of a basketball team making a free throw.
==================================================================================================
Probability per half-year: 4.883 (488.32 %) or 1 in 0

In words: The chance of mining a block with the given hashrate within a half-year is similar to the
probability of picking a red winning ball from a jar containing 0 white balls. Or: The probability
of such an event happening is a guarantee, a 100% sure thing - you can bet your last dollar on it.
It's gonna happen soon YEAH!!!
==================================================================================================
Probability per year: 9.766 (976.64 %) or 1 in 0

In words: The chance of mining a block with the given hashrate within a year is similar to the
probability of picking a red winning ball from a jar containing 0 white balls. Or: The probability
of such an event happening is a guarantee, a 100% sure thing - you can bet your last dollar on it.
It's gonna happen soon YEAH!!!
==================================================================================================
Expected average time to hit a block:
3,229,044.7 sec = 53,817.4 min = 897.0 h = 37.4 days = 5.3 weeks = 1.2 months = 0.1 years

Expected average time (relative to overall network):
3,381,051.1 sec = 56,350.9 min = 939.2 h = 39.1 days = 5.6 weeks = 1.3 months = 0.1 years
==================================================================================================
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ROADMAP -->
## Roadmap

- [x] Add Changelog
- [x] Add back to top links
- [x] Implement input validation
- [ ] Fix some analogy phrases
- [ ] Fix the resulting text on jar example for high probability cases
- [ ] Make the lumpy output code in the last part more compact
- [ ] Improve output formatting for enhanced readability
- [ ] Multi-language Support
    - [ ] Spanish
    - [ ] French
    - [ ] German
    - [ ] Chinese

See the [open issues](https://github.com/citb0in/solomining_probability_calc/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the GPLv3 License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

[@citb0in](https://bitcointalk.org)

Project Link: [https://github.com/citb0in/solomining_probability_calc](https://github.com/citb0in/solomining_probability_calc)


<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Acknowledgments

Helpful ressources and credits to:

* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Img Shields](https://shields.io)
* [GitHub Pages](https://pages.github.com)
* [Best Best-README-Template](https://github.com/othneildrew/Best-README-Template)
* [Font Awesome](https://fontawesome.com)


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/citb0in/solomining_probability_calc.svg?style=for-the-badge
[contributors-url]: https://github.com/citb0in/solomining_probability_calc/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/citb0in/solomining_probability_calc.svg?style=for-the-badge
[forks-url]: https://github.com/citb0in/solomining_probability_calc/network/members
[stars-shield]: https://img.shields.io/github/stars/citb0in/solomining_probability_calc.svg?style=for-the-badge
[stars-url]: https://github.com/citb0in/solomining_probability_calc/stargazers
[issues-shield]: https://img.shields.io/github/issues/citb0in/solomining_probability_calc.svg?style=for-the-badge
[issues-url]: https://github.com/citb0in/solomining_probability_calc/issues
[license-shield]: https://img.shields.io/github/license/citb0in/solomining_probability_calc.svg?style=for-the-badge
[license-url]: https://github.com/citb0in/solomining_probability_calc/blob/master/LICENSE.txt
[Python3.com]: https://www.python.org/static/img/python-logo@2x.png
[Python3-url]: https://www.python.org/download/releases/3.0
