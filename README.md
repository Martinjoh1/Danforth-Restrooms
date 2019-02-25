# Nap Time

**Author(s)**: Jenna Hughes and John Martin

**Google Document**: *https://docs.google.com/document/d/1aFm4vNCpDLIUj03oM7EaXg1spCM_F87eTSmThVaaZSk/edit?usp=sharing*

---
## Purpose

Too often, refusing to nap will simply have you falling asleep at your desk, while napping for the wrong amount of time may make you groggy and disoriented upon awakening. Our product will solve the issue of being able to get the right amount of sleep during a nap. We will do this by looking up appropriate information pertaining to what is the right amount of time a person needs in order to nap, and feel fully rested. Based on this information we will program the device to sound an alarm after the designated amount of time. Once the user selects the amount of time that works for his napping schedule, the Embedded system will then wake them up in the approprate amount of time. The device will act as an alarm set to the right amount of time for a comfortable, efficient, and healthy nap, that works for the user's schedule. 

## Initial Design Plan
For our intitial design plan, we have decided to use five buttons, all as inputs.  Four of the buttons will be used for the user to select the appropriate amount of time.  These times will be 10 minutes, 20 minutes, 60 minutes, and 90 minutes.  For example, if the 10 minute button is pressed, the ten minute timer will begin and the remaining time will be displayed on the digital display (output).  When the timer hits zero, the buzzer (output) will sound until the fifth button, the stop button, is pressed.  The stop button can also be used as a reset button, in case the wrong button is pushed, or the user wakes up earlier than anticipated.

## Outline 
- Hardware 
  - Timer/clock display
  - Buzzer for sound
  - Our Arduino device
  - (4) Buttons for users to select their nap time
  - (1) Button to shut off the alarm
    
- Code 
  - Function for the timer 
  - function for button press 
  - function for the sound 
  - A function to start the timer when the button is pressed
  - A function to start the sound when the timer runs out 
  - A function to stop the sound either when the button is pressed again, or after a certain amount of beeps 


**Sample image**:

![A sample image to show how to add one to a repo](/20190124_111548.jpg "A sample image. This is the text that appears.")

## Files
- Nap_Time_Demo_Code (For the Demo)
- Nap_Time_Final_Code (Final Project)
 
 
## Summary
The design was to include 5 buttons, and each button would have a different set amount of time. There is a 10 minute button, 
20 minute button, 60 minute button, and 90 minute button. There is also a stop button just in case the user wakes up early. We also had 
to try and work with a Liquid Crystal Display (LCD), in order to display the sleep time, and time remaining. 

One of the first problems we encountered was trying to get the LCD to work properly. We later realized that we did not have a 
potentiometer. The buttons would also send a surge to our computers which was resolved by adding resistors to each button. 
The next big challenges came when we wanted to understand how to make the LCD display when we pressed the button. Eventually we resolved most of our issues, and our program displays The time the person has to sleep, and plays a sound after the time 
is up. We probably spent about 14 hours working on this project.

## Instructions
Our product is very simple. Simply press the button that corresponds to the length of time that you have available to nap. The timer will automatically start, and you can begin to nap. You can monitor how much time you have left in your nap with the timer display. Once the alarm rings, press the stop button to shut off the sound.

## Errors and Constraints
-  It does not display the amount of time we have left 

- Stop button doesn't work how we intended, you have to press it in order to choose another button after making an initial section, but it does not just stop the action of the button that has already been pressed.  It also does not stop the buzzer.

## Reflection

This project taught us a lot about trying to understand new topics. We had to learn how to work with buttons, buzzers, and displays
using the Arduino. We discovered more possibilities with GIT, and this was a great experience for working as a team. There was a lot of wiring for the Arduino, which made us have to pay close attention to what was changing and how it was changing. 

It was really hard for us to get the stop button to work because there was no way to change the value like we wanted. Scheduling to meet  with each other was hard, but we overcame that challenge by using GIT effectively. We had tons of fun, because we figured out so much by looking through information. I think this project pushed us to think out side of the  box.

## References

https://github.com/2019-Spring-CSC-386/p00-project-1-martinjoh-hughesje/blob/master/example-README.md The original README file that Scott provided us with as a guide.

https://www.google.com/search?q=dehydration+sensor&client=firefox-bab&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiU4fLuzePfAhWRUt8KHRFaCKIQ_AUIDygC&biw=1366&bih=664 Researching if it was possible to track dehydration through sensors.

https://www.sleep.org/articles/how-long-to-nap/ Looking at articles on healthy napping times.

https://www.sleep.org/topic/age/ Looking at healthy naps for our age group.

https://www.scienceofpeople.com/science-perfect-nap/ Comparing different sites to make sure that appropriate nap times are consistent.

https://www.arduino.cc/en/tutorial/button Code used to help us work the button.


https://www.arduino.cc/en/Tutorial/HelloWorld Code used to help us with the LCD.

https://www.arduino.cc/en/Tutorial/LiquidCrystalDisplay Code used to help us understand the LCD.

https://www.google.com/search?client=firefox-b-ab&biw=1366&bih=664&tbm=isch&sa=1&ei=xUNHXJ7iBJKq_QbZ7I9o&q=pin+out+for+lcd+display+screen+1602zfa&oq=pin+out+for+lcd+display+screen+1602zfa&gs_l=img.3...272949.280381..281327...0.0..0.267.716.7j0j1......1....1..gws-wiz-img.PbAqIN70q18#imgrc=fD4tazEbutPbnM: Code used to help us wire up the LCD.

https://www.arduino.cc/en/Tutorial/HelloWorld

https://www.arduino.cc/en/tutorial/pushbutton

https://arduino.stackexchange.com/questions/34817/multiple-push-buttons

https://www.arduino.cc/reference/en/language/functions/digital-io/digitalread/

- Autoscroll.ino : This will help us to understand how to make autoscroll work on Arduino. 

- Button.ino : This file will help us to understand how to use the button on Arduino. 

- TimerHelp.ino: this file will help us to understand exactly how to work with time on the Arduino. 

- codestart.ion: This file is a start to our code that took influence for helper code we found.


## Final Self-Evaluations

### Ideation, Brainstorming, Design:

*Partner 1 (Jenna Hughes): 5

*Partner 2 (John Martin ): 5

### Code creation: 

*Partner 1 (Jenna Hughes): 5

*Partner 2 (John Martin ): 5

### Documentation creation:

*Partner 1 (Jenna Hughes): 5

*Partner 2 (John Martin ): 5

### Teamwork & Participation:

*Partner 1 (Jenna Hughes): 5

*Partner 2 (John Martin ): 5
