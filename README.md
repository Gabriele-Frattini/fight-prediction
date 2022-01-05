# Can we create a beting edge with data-driven fight predictions?
![bet_boxing](https://user-images.githubusercontent.com/88820508/148267698-31d5748e-9434-4acc-a99e-efe87a966498.jpg)
# [App](https://share.streamlit.io/gabriele-frattini/fight-prediction/main/app.py)

***

## Introduction
Data analytics is a science that involves analyzing raw data to come up with useful insights.
In this article, I’m going to present a data analytics project and how I used the derived insights from EDA to create an app for fight predictions.
I love the sport of boxing, I also make a bet once in a while but I was curious if It’s possible to create a tool that could make data-driven predictions for me. I was inspired by the dataset provided from this github. Before we begin I just want to say that I dont encourage anyone to bet with money and that this app was just made for fun.

***

## Project Summary
- Created an app that predicts the result of a fight (accuracy ~85%) to help users make data-driven bets for fights
- Quantified fighter attributes in terms of importance so users know what contributes to the fight outcome
- Defined fights that a user might be interest to watch based on preferences
- Constructed a fighter profile that emperically has had the most success in fights

***

## Data cleaning
The data was structured in such a way that we had about 180 000 rows for all fights but we only had attributes for one of the fighters. Because of the scope of this project I needed the attrubutes from both fighters for every row.
Luckily we had unique ID’s for the two fighters for every row so I decided to split them up as our fighter and the opponent. This led to a bit of relational algebra, where I used the opponents ID as a primary key and inner joined our dataframe with itself to get all the fights where we had data on both fighters. After some cleaning I was left with about 8000 fights to analyze, thats about 5% of the original data which says quite a bit of how much cleaning had to be done.

***

## Exploratory Data Analysis

There where mainly five questions I where interested in.

**Firstly,** there are two stances in boxing, left-handed and right-handed. In boxing terms, the former is called southpaw and the latter is called orthodox. Since I’am a southpaw I was interested in the win/loss distribution for these two stances

**Secondly,** I wanted to know which countries are doing best in the sport. USA is known for Las Vegas “the mekka of boxing” but how are they compared to other countries in terms of winned fights?

**Thirdly,** what does an optimal fighter profile look like based on the data?

**Fourth,** there are mainly two ways to end a fight, either on points or knockout. Which weight-classes would be most interesting for a viewer to watch, based on preference?

**Fifth,** what quantifiable attributes between two fighters are most importants for predicting the result?

***

### Question one
Southpaws had a 5.7% higher winning rate than orthodox fighters but because this difference was so marginal I analyzed it further and bootstrapped the data to see if the difference is statistically significant. Bootstrapping works by resampling a sample n of the data x number of times to get a predictible confidence intervall for our sample statistic (the win-rate). By comparing the confidence intervals for both stances I concluded that they overlaped to much for me to be able to draw any conclusions.

![stances 1](https://user-images.githubusercontent.com/88820508/148268241-65517395-2f5b-44d8-a79d-2af8b18dd800.png)

![conf_int_stances](https://user-images.githubusercontent.com/88820508/148268280-eb841c70-964b-478a-ae54-0c6033d9494d.png)


### Question two
The first four countries are the biggest in boxing but to my suprise, Philippines had more wins under their belt than USA. This made question why, so i analyzed this further.
I found that over time Phillippines where actually superior in terms of yearly wins until 2018. Phillippines had a bad previous year and since then USA is on the way to reedeming their first place in the boxing world.

![top_countries](https://user-images.githubusercontent.com/88820508/148268395-5c8e5dcd-49cc-40ca-b24d-7a67125cb9df.png)
![nations_time](https://user-images.githubusercontent.com/88820508/148268404-3da1b90d-2845-42fa-bb2b-059d8bb0be4a.png)


### Question three
If we wanted to construct an optimal fighter profile from our previous two questions we would preferably have a southpaw who is from the phillipines, (which describes one of my favourite fighter Manny Pacquiao)
I also found that the most successful fighters where in their early/mid twenties, above average in height and had 5–9 years of experience

![results_age](https://user-images.githubusercontent.com/96744665/148268897-24d7bdce-59e0-4375-ae40-c7f55421912c.png)
![results_height](https://user-images.githubusercontent.com/96744665/148268909-f94cdf98-66ac-403b-99eb-f35950b2fa71.png)


### Question four
The fights that ended with KO or TKO are labeled with knockout, and the games that went full time and ended with points are labeled points.
My hypothesis was that the heavy weight-class would have the highest percentage of knockouts but they actually had relatively few. If you want to watch a fight that is most likely to end in a knockout you should watch the light heavy weight-class but the middle weight-class can also be interesting if you are in to knockouts.

![Knockout_or_points](https://user-images.githubusercontent.com/96744665/148268992-16d39b56-d467-4409-8ee1-5f88116be411.png)


### Question five
The importance of our variables was derived from the decreased impurity from a random forest classifier. The alghoritm works by partitioning random subsets of the data with the goal of making the classes in each subdivision as homogeneous as possible. The more mixed a class is, the more impure it is and the bar graph below display how much each variable on average contributed to decreasing the gini impurity. The result is a measure of variable-importance for determining which class (win,loss,draw) a fighter will belong to at the end of a fight.
What I found was that the fighters previous loss records are undoubtedly the most important. Closely followed by their wins, height and experience differences. I was a bit suprised to find that the stance was not of relative importance, but it’s a good counter-argument if an orthodox fighter blames a loss for the different angles.

![feature importance](https://user-images.githubusercontent.com/96744665/148269061-fa3519eb-150f-44f5-a369-5496d073d74f.png)

***

## Model performance
Since the fighters records already explain a lot of the the variability that experience does I decided to remove that variable from the model to decrease the risk of overfitting the data. I also removed the stances since these were not of relative importance and again to prevent the risk of capturing noise that dont contribute to the model.
The final random forest classifier had an overall accuracy of 85% which I’m happy about

![confusion_matrix](https://user-images.githubusercontent.com/96744665/148269142-4a064849-a97f-4e16-8e8d-7515ebeefdbc.png)
