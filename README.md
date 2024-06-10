# Authentication-System

# Feature List
1. SignUp
   - Username
   - Password
     - Check Password Strength
   - Take user details
     - Name
     - phone number
       - Check length of phone number
     - Email
       - Check valid Email
     - 2 Security Question
    - Generate backup code
2. SignIn
   - Username
     - Check Username Already SignUp or nor
   - Password
     - Forget Password
     - Update Password
   - Signin Using Backup code
   - Signin Through Security Question
     - Update Security Question's Answer

# SignUp Process
1. Username and Password
   -Input fields for Username and Password.
   -Check password strength (e.g., at least 8 characters, includes uppercase, lowercase, numbers, and special characters).

2. User Details
   -Input fields for Name, Phone Number, and Email.
   -Validate the length of the phone number (usually 10 digits for many countries).
   -Validate email format using regex (e.g., ^[\w\.-]+@[\w\.-]+\.\w{2,4}$).

3. Security Questions
   -Provide two security questions and input fields for their answers.
   -Optionally, choose from a set of predefined security questions.

4. Backup Code
   -Generate a backup code (e.g., a random string of characters) for account recovery.

5. Store User Details
   -Save the user details, including hashed password, security question answers, and backup code in a secure database.

# SignIn
1. Username and Password
   -Input fields for Username and Password.
   -Check if the username is already signed up.
   -Validate the password against the stored hashed password.
2. Forgot Password
   -Option to reset the password by verifying the user through:
      -Security questions.
      -Backup code.
      -Sending a reset link to the registered email.
3. SignIn Using Backup Code
   -Input field for backup code to authenticate the user.
4. Update Security Question’s Answer
   -Allow users to update their security questions and answers after logging in.

# What is authentication & how does it work?
authentication means confirming that a user is who they say they are. This ensures only those with authorized credentials gain access to secure systems. When a user attempts to access information on a network, they must provide secret credentials to prove their identity.
