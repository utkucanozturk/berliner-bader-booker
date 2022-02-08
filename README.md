## Booking Alerts for Berliner Bäder

Script that automaticly checks the available tickets for the swimming halls in Berlin.

### Swimming Halls

It can be used for the swimming halls listed in [this website](https://pretix.eu/Baeder/).

### Input Values

4 input values are required for program to run:

* Swimming hall id. It can be found using [this website}(https://pretix.eu/Baeder/). When you clicked on the swimming hall you are interested in, you will be redirected to the URL for that pool. If you check the URL address you will see that it ends with a number such as `49` for Stadtbad Neukölln. That number should be inputted as hall id in the application.

* Date you want to make a search. It should be in the format of `YYYY-MM-DD`.

* Time you want to make a search. It should be in the `HH:MM` 24h format.

* Search duration in minutes.

### How it works?

The program checks the specified swimming hall's ticket website every minute whether if there are any empty tickets for the inputted date and time or not. If there are empty spots, you will hear a victory sound and program will stop running.