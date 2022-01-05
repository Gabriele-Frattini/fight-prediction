# Can we create a beting edge with data-driven fight predictions?
![bet_boxing](https://user-images.githubusercontent.com/88820508/148267698-31d5748e-9434-4acc-a99e-efe87a966498.jpg)


### Introduction
Data analytics is a science that involves analyzing raw data to come up with useful insights.
In this article, I’m going to present a data analytics project and how I used the derived insights from EDA to create an app for fight predictions.
I love the sport of boxing, I also make a bet once in a while but I was curious if It’s possible to create a tool that could make data-driven predictions for me. I was inspired by the dataset provided from this github. Before we begin I just want to say that I dont encourage anyone to bet with money and that this app was just made for fun.


### Project Summary
- Created an app that predicts the result of a fight (accuracy ~85%) to help users make data-driven bets for fights
- Quantified fighter attributes in terms of importance so users know what contributes to the fight outcome
- Defined fights that a user might be interest to watch based on preferences
- Constructed a fighter profile that emperically has had the most success in fights

### Data cleaning
The data was structured in such a way that we had about 180 000 rows for all fights but we only had attributes for one of the fighters. Because of the scope of this project I needed the attrubutes from both fighters for every row.
Luckily we had unique ID’s for the two fighters for every row so I decided to split them up as our fighter and the opponent. This led to a bit of relational algebra, where I used the opponents ID as a primary key and inner joined our dataframe with itself to get all the fights where we had data on both fighters.

![innerjoin](https://user-images.githubusercontent.com/88820508/148267987-9ca0b3df-fac5-4b4c-9648-9b61c428aa9b.png)

After some cleaning I was left with about 8000 fights to analyze, thats about 5% of the original data which says quite a bit of how much cleaning had to be done.

### Exploratory Data Analysis

There where mainly five questions I where interested in.


**Firstly,** there are two stances in boxing, left-handed and right-handed. In boxing terms, the former is called southpaw and the latter is called orthodox. Since I’am a southpaw I was interested in the win/loss distribution for these two stances

**Secondly,** I wanted to know which countries are doing best in the sport. USA is known for Las Vegas “the mekka of boxing” but how are they compared to other countries in terms of winned fights?

**Thirdly,** what does an optimal fighter profile look like based on the data?

**Fourth,** there are mainly two ways to end a fight, either on points or knockout. Which weight-classes would be most interesting for a viewer to watch, based on preference?

**Fifth,** what quantifiable attributes between two fighters are most importants for predicting the result?


**Question one**
Southpaws had a 5.7% higher winning rate than orthodox fighters but because this difference was so marginal I analyzed it further and bootstrapped the data to see if the difference is statistically significant. Bootstrapping works by resampling a sample n of the data x number of times to get a predictible confidence intervall for our sample statistic (the win-rate). By comparing the confidence intervals for both stances I concluded that they overlaped to much for me to be able to draw any conclusions.

![stances 1](https://user-images.githubusercontent.com/88820508/148268241-65517395-2f5b-44d8-a79d-2af8b18dd800.png)

![conf_int_stances](https://user-images.githubusercontent.com/88820508/148268280-eb841c70-964b-478a-ae54-0c6033d9494d.png)


**Question two**
The first four countries are the biggest in boxing but to my suprise, Philippines had more wins under their belt than USA. This made question why, so i analyzed this further.
I found that over time Phillippines where actually superior in terms of yearly wins until 2018. Phillippines had a bad previous year and since then USA is on the way to reedeming their first place in the boxing world.

![top_countries](https://user-images.githubusercontent.com/88820508/148268395-5c8e5dcd-49cc-40ca-b24d-7a67125cb9df.png)
![nations_time](https://user-images.githubusercontent.com/88820508/148268404-3da1b90d-2845-42fa-bb2b-059d8bb0be4a.png)






# [App](https://share.streamlit.io/gabriele-frattini/fight-prediction/main/app.py)
