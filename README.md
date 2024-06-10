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
1. Username and Password:
   -Input fields for Username and Password.
   -Check password strength (e.g., at least 8 characters, includes uppercase, lowercase, numbers, and special characters).

2. User Details:
   -Input fields for Name, Phone Number, and Email.
   -Validate the length of the phone number (usually 10 digits for many countries).
   -Validate email format using regex (e.g., ^[\w\.-]+@[\w\.-]+\.\w{2,4}$).

3. Security Questions:
   -Provide two security questions and input fields for their answers.
   -Optionally, choose from a set of predefined security questions.

# What is authentication & how does it work?
authentication means confirming that a user is who they say they are. This ensures only those with authorized credentials gain access to secure systems. When a user attempts to access information on a network, they must provide secret credentials to prove their identity.
