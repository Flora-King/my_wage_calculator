# UK Wage Calculator

The UK Wage Calculator program allows the user to work out their monthly take home pay using input gross annual earnings and UK tax code.

The income tax and National Insurance rates used are only relevant to 2022/23 UK tax year. This program does not calculate student loan or pension deductions.

Users will be able to see the income tax breakdown as well as national insurance breakdown.


The live version of this project can be found here [UK WAGE CALCULATOR]:https://uk-wage-calculator.herokuapp.com/

![UK WAGE CALCULATOR PROGRAM](https://user-images.githubusercontent.com/106548101/224796092-bae7ec2e-b429-4572-bd0d-b11eef6170a6.png)


## How to use the UK Wage Calculator

* Upon running the program, the user can choose to proceed using the calculator by pressing 1 or quit by pressing 2
* If option 2 is selected, the program ends and this message ['See you another time. Goodbye!'] is presented to the user 

![Screenshot 2023-03-13 at 20 06 50](https://user-images.githubusercontent.com/106548101/224820144-66c9335a-df8f-4189-a8e7-fe726077399e.png)

* However if the user chooses option 1, then the program proceeds requesting the user to input their tax code and gross annual earnings

![Screenshot 2023-03-13 at 20 08 23](https://user-images.githubusercontent.com/106548101/224820434-0ec1408c-227e-4c16-b0fd-33a769fba02c.png)

## Features

* Input validation and error checking for the show menu
    * the user can only choose option 1 or 2 to proceed
    * A wrong option input is detected and a warning message is presented to the user as shown below

* Input validation and error checking for the tax code
    * the user can only choose option 1 or 2 to proceed
    * A wrong input is detected and a warning message is presented to the user as shown below

![Screenshot 2023-03-13 at 22 48 10](https://user-images.githubusercontent.com/106548101/224849578-7c7bfa9c-d899-42cb-8c2c-30f20dfefd25.png)

## Results Display

* A breakdown of the user's income tax is displayed 
    * This breakdown details the different amount of income tax deducted in accordance to the income tax rate/band
* A breakdown of the user's National Insurance is also displayed 
  * This contains details the different amount of national insurance deducted per in accordance to the National Insurance rate/band

* Lastly the users take home is also presented
* The totals for the 'Income Tax', 'National Insurance', and 'Take Home' amounts are then displayed in a table.
    * This table also breaks down the results to show a yearly amount and a monthly amount

## Testing

### Tests carried out

* Tested all scenarios and successfully validated that accurate data in input by user and where not, the program dispays a message to user for them to try again
* Tested all scenarios and successfully validated that this program would return accurate figures aligned with the different UK Income tax rates and National insurance bands
* Checked the program sequence to ensure it runs and displays data as expected

### Usability Testing

* Tested the program to ensure that the warning messages and sub headings are displayed in color for easier visibility by the user
* Tested all content to ensure it is legible and without spelling or grammatical errors.

### Validator Testing

* PEP8 PYTHON VALIDATOR

There are no outstanding error after validating my code in PEP8 validator

<img width="1123" alt="Screenshot 2023-03-13 at 19 05 46" src="https://user-images.githubusercontent.com/106548101/224804515-9cf1e7fb-6d8f-4a19-a46b-dfacb8431da6.png">

### Bugs and Errors

#### Solved
* The while loop to validate that entered tax code is of correct format, was running non-stop. I eventually stopped it by applying the correct indent to the code

* I encountered issues while trying to eliminate the 'too long line code' error. i hdecided to skillfully shorten my variable names as well as function names to ensure the code was not too long

#### Unsolved

* No errors outstanding

## Accessibility
 * Due to the uniqueness of this project, it is not possible to test and validate accessibility

## Deployment 

The UK Wage Calculator program was deployed in GitHub.

* I created a github project, and followed provided instructions to apply the Code institute template for portifolio prpject 3
* Once the project finished rendering, i proceeded to write code for my project [my_uk_wage_calculator] in gitpod 
* Due to the unique set up of this project, i made sure to pin the gitpod workspace to ensure no loss of written code

To publish/deploy my project, i followed these steps:
1 Updated the requirements.txt before deployment and pushed changed to github
2 Setup my heroku account
3 Created new app called uk-wage-calculator
4 Added python and nojs buildpacks
5 Connected app to Github successfully
6 Then deloyed app manually 


Once the app was successfully deployed, i started to run the program found here [UK WAGE CALCULATOR]: https://uk-wage-calculator.herokuapp.com/

## Credits
* Code Institute - my Mentor was very helpful, reassuring and very patient.
* Code Institute - Tutors were also very helpful.
* Reffered to documentation and examples on W3schools website.
* Reffered to stackoverflow website for various code query examples and to solve some errors i encountered.
* Utilised other salary calculators to test my and validate the results in my program e.g. https://www.thesalarycalculator.co.uk/
* Referred to https://www.gov.uk/ to understand how Income Tax and National Insurance are worked out
* Watched several youtube tutorials to enahnce my code e.g. @Indently
