   ##  Meaning and function of (loading_progress_bar) ##


1. This code defines a function called "progressload" that takes in one argument, "value". The function uses the Tkinter "progress" widget and sets its value to the input argument.

2. The function also defines a global variable called "counter", initially set to 0. The function then enters a loop that runs as long as the counter is less than or equal to 10.

3. Inside the loop, the function creates a variable called "test" which is a string that concatenates the text "Please Wait.... " with the result of 10 multiplied by the counter variable, followed by the string " %". This string will be used to update the text of the "progress_label" widget.

4. Then, it uses the Tkinter "after" method to schedule the function to run again after 1000 milliseconds, with an incremented value for the progress bar, and the counter variable is incremented by 1.

5. Finally, when the counter variable is greater than 10, the function calls another function called "user_login()".

6. This code is used to display a loading bar with a percentage and a message that shows the user that the system is working on something and is not stuck.

7. It's important to note that the above code is just a fragment of a larger program, and it may have dependencies on other functions, widgets or modules that should be defined and imported before running this function.


### this script is responsible for either expanding the window to the fullest
2. root.attributes ("alpha": must be -alpha, -topmost, -zoomed, -fullscreen, or -type)