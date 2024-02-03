# Similar calendar
In the calendar we usually use, called the Gregorian calendar, there are some repeating patterns. One pattern repeats every 28 years, where the days of the week match up with the same dates again. Another important pattern repeats every 400 years. In this 400-year cycle, the arrangement of leap years (years with an extra day) and common years (years without an extra day) repeats itself.

So, every 28 years, the calendar looks the same, and every 400 years, it repeats exactly. For example, the calendar in the year 2000 was the same as the one in 2400 because both fit into this 400-year cycle. These repeating patterns help us keep track of time consistently over long periods.

One common method to find years with repeating calendar patterns is as follows:
- Let $y$ be the year you want to find the repeated calendar for.<br/>
- For non-leap years: calculate the $\text{remainder}$ when dividing $y$ by 4: $\text{remainder} = y \mod 4$<br/>
- Determine the number of years to add based on the $\text{remainder}$:<br/>
   - If $\text{remainder} = 0$, add 28 years: $y_{\text{repeat}} = y + 28$<br/>
   - If $\text{remainder} = 1$, add 6 years: $y_{\text{repeat}} = y + 6$<br/>
   - If $\text{remainder} = 2$ or $\text{remainder} = 3$, add 11 years: $y_{\text{repeat}} = y + 11$<br/>


So, I've written a simple Python script that does just that: it takes a year as input and identifies all the years from that year up to 2100 that have the same calendar configuration.

```
Enter the base year: 2024
The years similar to 2024 are: 2052, 2080
```


## Languages and Tools
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 

## Requirements
```
Just Python 3.11.2
```

## Test Coverage
TODO

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

<hr>

## Connect with me
<p align="left">
<a href="https://www.linkedin.com/in/francescopl/" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="francescopaololezza" height="20" width="30" /></a>
<a href="https://www.kaggle.com/francescopaolol" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/kaggle.svg" alt="francescopaololezza" height="20" width="30" /></a>
</p>

