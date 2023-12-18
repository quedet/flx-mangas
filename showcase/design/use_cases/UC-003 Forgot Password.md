## UC-003: Password Reset
### Description
The use case outlines the process by which a registered user forgot their password and want to reset it.

### Actors
* Registered User
* Password Reset System

### Preconditions
* The user already have an account on the platform
* The user is on the platform's reset password
* The user is on their password reset settings

### Triggers
* The user clicks on "Forgot Password" button on the platform's login page.
* The user clicks on "Reset Password" button on the platform's profile settings page.

### Basic Flow
* The system displays a password reset form with email address to the user.
* The user enters the email address they registered while creating their account and submit the form.
* The system sends a reset link to the entered email address.
* The user clicks on the reset link and redirected to the platform's password reset page.
* The system displays a password reset form with fields for the user to create new robust password as well as repeat that password for confirmation.
* The user enters these information.
* The user validates the password
* If the password is valid, the system resets the user's previous password to the newly created one.
* The system records the user's password reset activity.
* The user is then redirected to the login page.

### Alternative Flows
* If the entered email address is not registered:
  * The system displays an error message an prompts the user to enter a vali email or register for a new account.
* If the password reset link token is invalid or has expired:
  * The system displays an error message and prompts the user to request a new password reset.

### Exception Flows
* If there are technical issues preventing the password reset process:
  * The system displays a generic error message an prompts the user to try agin later.

### Post Conditions
* The user's password is successfully reset.
* The user can log in using their new password.

### Assumptions
* The user has access to the email account associated with their platform registration.
* The user's email service does not mark password reset emails as spam.

### Dependencies
* The system relies on a secure password reset mechanism and email service for sharing password reset emails.