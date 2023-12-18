## UC-002: User Authentication
#### Description
The use case describes the process by which a registered user log into their account.
#### Actors
* Registered User
* Authentication System

#### Preconditions
* The user is on the platform's login page.
* The user has successfully registered an account on the platform.

#### Triggers
* The user just created their account and has been redirected to the login page
* The user clicked on the "Log in" button.

#### Basi Flows
* The system displays the login form with fields for the user to enter their identifier (email address or username) and password.
* The user enters their details into the login form.
* The system validates the entered information against the stored user credentials.
* If the information is valid, the system grants access to the user and logs them into the platform.
* The system records the user's login activity, updating login timestamp.
* The user is redirected to the platform's home or dashboard page depending on their role.

