# =============================================================================
# Mail Merge Program - Day 24 Challenge
# Automatically generates personalised invitation letters for multiple recipients
# Reads names from file, replaces placeholder in template, saves individual letters
# =============================================================================

# =============================================================================
# CONSTANTS
# =============================================================================
PLACEHOLDER = "[name]"  # Placeholder text to be replaced with actual names

# =============================================================================
# READ INVITED NAMES FROM FILE
# =============================================================================
# Open the names file and read all lines into a list
# Each line contains one name that will receive an invitation
with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()  # Returns list with \n characters included

# =============================================================================
# READ LETTER TEMPLATE
# =============================================================================
# Open the template letter file and read the entire contents
# This template contains the [name] placeholder to be replaced
with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()  # Read entire file as single string

    # =============================================================================
    # GENERATE PERSONALISED LETTERS
    # =============================================================================
    # Loop through each name and create a personalised letter
    for name in names:
        # Remove whitespace (including \n) from the name
        stripped_name = name.strip()

        # Replace the placeholder with the actual name
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)

        # Create and save the personalised letter
        # File naming convention: letters_for_[Name].docx
        with open(f"./Output/ReadyToSend/letters_for_{stripped_name}.docx", mode="w") as completed_letter:
            completed_letter.write(new_letter)

# =============================================================================
# PROGRAM COMPLETE
# =============================================================================
# All personalised letters have been generated and saved to ReadyToSend folder
# Each recipient now has their own invitation file ready to be sent