## UK WAGE CALCULATOR

The UK WAGE CALCULATOR program enables the user to work out their monthly take home pay using by entering their annual gross earnings and tax code.
The income tax and National Insurance rates used are only relevant to 2022/23 tax year. This program does not calculate student loan and pension deductions.

Users will be able to see the income tax breakdown as well as national insurance breakdown.

The live version of this project can be found here [UK WAGE CALCULATOR]:https://uk-wage-calculator.herokuapp.com/

![UK WAGE CALCULATOR PROGRAM](https://user-images.githubusercontent.com/106548101/224796092-bae7ec2e-b429-4572-bd0d-b11eef6170a6.png)

### How to use the UK WAGE CALCULATOR

* Upon running the program, the user can choose to proceed using the calculator by pressing 1 or quit by pressing 2
* If option 2 is selected, the program ends and this message ['See you another time. Goodbye!'] is presented to the user 

![Screenshot 2023-03-13 at 20 06 50](https://user-images.githubusercontent.com/106548101/224820144-66c9335a-df8f-4189-a8e7-fe726077399e.png)

* However if the user chooses option 1, then the program proceeds to ask the user to enter their tax code and gross earnings

![Screenshot 2023-03-13 at 20 08 23](https://user-images.githubusercontent.com/106548101/224820434-0ec1408c-227e-4c16-b0fd-33a769fba02c.png)

### Features

* Input validation and error checking
* You can only choose option 1 or 2 to proceed
* A wrong option is detected and message with instructions of what to do is presenrted to the user as show below

![Screenshot 2023-03-13 at 20 11 30](https://user-images.githubusercontent.com/106548101/224821297-21df8dd8-b0ec-4906-b8ee-1974d116fc6e.png)

* 


## Testing

#### General test required

* To confirm whether this website works in Chrome and Firefox (mobile and desktop versions).
* To confirm the responsiveness of this website on all screen sizes using chrome dev tools.
* To confirm that other users [other than myself] can read and understand the text throughout the website
* To confirm that the enquiry form works, indicates required text and the submit button works.

#### Tests carried out

##### Functional Testing

* Tested all links ensuring they are working as expected and make sure there are no broken links. 
* This included the navigation links [Home, Services, Contact Us]

##### Usability Testing

* Tested the site Navigation to ensure that the buttons or Links to different pages are easily visible and consistent on all webpages
* Tested the Content:
* Tested all content to ensure it is legible and without spelling or grammatical errors.
* Checked all images to ensure they all contain an “alt” text


### Validator Testing

* PEP8 PYTHON VALIDATOR

<img width="1123" alt="Screenshot 2023-03-13 at 19 05 46" src="https://user-images.githubusercontent.com/106548101/224804515-9cf1e7fb-6d8f-4a19-a46b-dfacb8431da6.png">

* Accessibility
 * I have validted that accessibility is good. My accessibility report shows a low perfomance report. This is due to the many font awesome icons i have used in this website.

### Bugs and Errors

#### Solved
* I encountered a few errors in HTML and CSS during the build phase. For example, I had created a button inside the anchor tag. After seeing the error from the validation report, i adjusted my code.

* I encountered issues while building the services section layout. The service types were displaying as "two columns side-by-side and two rows" structure that I needed. I solved this by created an outer container to house all service types plus a container for each service type

#### Unsolved

* No errors outstanding

## Deployment 

The UK WAGE CALCULATOR program was deployed in GitHub.

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
* Code Institute - mentor was very helpful, reassuring and very patient.
* Code Institute - Tutors were very also helpful.
* Reffered to documentation and examples on W3schools website.
* Icons were downloaded free from Font Awesome website.
* Reffered to stackoverflow website for various code query examples.
* All images in this website were downloaded free from Pexels website.
* I used Coolers website to find and learn about color palettes.
* I also referred to Google fonts as well as Chrome Developer tools to text and view responsiveness.