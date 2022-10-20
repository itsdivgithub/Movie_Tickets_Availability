# Movie_Tickets_Availability
Here, we characterize the code which will knock a ticket booking webpage and alert the user as and when tickets are available.

This code works for bookmyshow.com, an India based ticket booking platform. The user has to provide a particular webpage  URL of Bookmyshow which holds the listings of Cinemas for a particular movie on the particular date.

If the code detects that the particular Cinema is NOT listed, it sleeps for 300 seconds(5 minutes) before re-running. If the code detects that the particular Cinema IS listed, it displays a PopUp alerting the user of the same. Clicking on the "Click Here" button on the popup will open the webpage URL in Chrome Browser, where the user can proceed to book the tickets! If a Chrome browser session was already openned, a new tab will be openned in the same session.
