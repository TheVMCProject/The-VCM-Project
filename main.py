import smtplib


# Prompt the user to choose software
print("Choose software (separate choices with commas):")
print("1. Microsoft 365")
print("2. Unity")
print("3. Roblox Studio")
print("4. Visual Studio Code")
print("Github Desktop)
print("Adobe Creative Cloud")
print("Blender")           
print("Adobe Premiere Pro")
print("Adobe After Effects")
# Get the user's choices
choices = input("Enter your choices (e.g., 1,2,3): ").split(",")

# Map the user's choices to the corresponding software
software = []
for choice in choices:
    if choice == "1":
        software.append("Microsoft 365")
    elif choice == "2":
        software.append("Unity")
    elif choice == "3":
        software.append("Roblox Studio")
    elif choice == "4":
        software.append("Visual Studio Code")
    else:
        print(f"Invalid choice: {choice}")

# Prompt the user to enter their username and password
username = input("Enter your username: ")
password = input("Enter your password: ")

# Email details
sender_email = "VCM@TheVCMProject.com"
receiver_email = "thecodeProject@outlook.com"
subject = "VM Details"
message = f"Software: {', '.join(software)}\nUsername: {username}\nPassword: {password}"

# Connect to the SMTP server
with smtplib.SMTP("smtp.office365.com", 587) as server:
    server.starttls()
    server.login(sender_email, "Seth1365")  # Replace "your_password" with the actual password

    # Send the email
    server.sendmail(sender_email, receiver_email, f"Subject: {subject}\n\n{message}")

print(" Thank you we will have it ready within 2-4 buisness days.")
