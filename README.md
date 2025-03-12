# Elevator Script
## Summary
This script models a simple elevator. It takes two arguments, start and floors, which indicate the starting floor and the floors we want the elevator to visit. The script is designed to output the time it takes in seconds to travel between all of the floors we want to visit. The script will also output the floors we visited in order, including the starting floor.

## Constants
- Single floor travel time: 10 seconds


## Usage
One can run this script if they have python 3 installed using the command below:
```
python elevator.py start=<int> floors=<int1,int2,int3...>
```
**Note:** **start** and **floors** arguments must be **integers** greater than or equal to 1

Here is an example with valid arguments:
```
python elevator.py start=40 floors=39,3,44,1,4,5,33,22
```


## Assumptions
This script was written with the following assumptions in mind:
- All buttons are pressed at the beginning, meaning elevator will continue its direction and stop at each floor along the way
- Each floor will only be visited once, even if it appears multiple times in the list
  - This acts as one elevator ride starting when someone gets in at the starting floor, then presses all buttons in the floors list
- Direction of elevator is always down first if there are any floors pressed that are lower than the starting floor

## Potential Enhancements
- Adding functionality for elevator direction
  - Could add an argument to specify direction, which would then mandate which order we start traversing the floors
- Adding functionality to traverse list in order (first come, first serve)
  - Would allow for duplicate floors, as the elevator would simply visit each floor in the order it was provided in the list
- Adding functionality to minimize overall time the elevator spends traversing the floors
  - For example, with the inputs start=40 and floors=5,9,1,41 this script will output: 790 40,9,5,1,41
  - The above could theoretically be optimized so that the output would look like this: 410 40,41,9,5,1
