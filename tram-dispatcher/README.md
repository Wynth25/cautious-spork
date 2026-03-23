# The Tram Dispatcher

## The Scenario

You are writing the scheduling logic for a major transit hub. Trams arrive and depart constantly throughout the day. To avoid traffic jams and delays, you need to calculate the absolute maximum number of trams that will be in the station at the exact same time. This tells the city exactly how many physical platforms must be built and kept open.

## The Input
Your Python function will receive a list of tram schedules. Each tram is represented by a list of two integers: ```[arrival_time, departure_time]```. The times are represented in minutes from midnight (for example, 9:00 AM is 540).
```schedule = [[540, 570], [550, 600], [560, 580], [610, 630], [570, 590]]```

## The Rules of the System

1. Occupancy: A tram occupies exactly 1 platform from the exact minute it arrives until the exact minute it departs.

2. The "Just in Time" Rule: If Tram A departs at the exact same minute Tram B arrives, they can share the same platform. Tram A is considered gone just in time for Tram B to pull in. They do not overlap. (e.g., ```[540, 570]``` and ```[570, 590]``` do not overlap).

3. Chaos: The schedule list you receive is completely unsorted.

## Your Objective
Write a Python function ```def calculate_platforms(schedule):``` that evaluates the daily tram traffic and returns two things:

1. An integer representing the minimum number of platforms required to handle all trams without any of them waiting.

2. The exact minute the station first hits this maximum capacity.

Example Test Case

```
Python
Input: [[540, 570], [550, 600], [560, 580], [610, 630], [570, 590]]

Expected Output:
Platforms Required: 3
Peak Minute: 560

# Breakdown:
# Minute 540: 1 tram
# Minute 550: 2 trams
# Minute 560: 3 trams (Peak)
# Minute 570: One leaves, another arrives. Still 3 trams.
```
