# What's the real cost of travel?

## Project Overview
When optimizing a method of travel, we often only focus on the cost per time spent on transport. However what are other hidden costs that a customer should consider when choosing the optimized transport? As travellers are becoming more environmentally conscious prefering low-carbon journeys, this project factors in transit time and environmental damage to assess the true costs of travel. Methods of plane, train, and bus were compared. With visualization, 'real cost' optimized transprot is recommended 

## Problem Statement
This story will compare the travel costs of flight, bus, and train over the selected dimensions to destinations on which overnight train and direct flight services exist from Malmö/Copenhagen:

1. Ticket price
2. Travel time
3. Social cost - carbon emission based on load factor (i.e. typical number of passengers on each train/plane), estimated route length, energy source.

## Recommendation and Visualizations
For each city, transport with the lowest colored area is concluded as the method with the lowest 'real cost.'

CPH - Stockholm: Train;
CPH - Oslo: Bus;
CPH - Berlin: Fly;
CPH - Amsterdam: Fly;

![Recommendation](https://github.com/junauh/travel-cost/blob/master/recommendation_viz.png)

## Data source
[Rome2Rio](https://www.rome2rio.com/) a good one-stop-shop for ticket prices and journey times by all possible transporations (including rail, air, bus, boat)

[EcoTransit](https://www.ecotransit.org/) for the simplified estimation, we used the following average to compare CO2 kg/ hr travel for each transport model, and further specification could be taken as the next step.
* Train: 1.9
* Bus: 11.0
* Flight: 42.0

## Motivation
**[DW](https://www.dw.com/en/trains-vs-planes-whats-the-real-cost-of-travel/a-45209552)** Inspired highly by the article, adapted and improved with CPH/Malmö centric data analysis with additional bus option
