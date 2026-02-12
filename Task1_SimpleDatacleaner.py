names = [" Alice ", "bob", " CHARLIE "]

cleaned_names = []

for name in names:
    print("Original Name:", repr(name))

    # Condition 1: Check for leading/trailing spaces
    if name != name.strip():
        print(" --> Has extra spaces")

    # Remove spaces first
    name = name.strip()

    # Condition 2: Check if empty after stripping
    if name == "":
        print(" --> Empty name, skipping...")
        continue

    # Condition 3: Check if all uppercase
    if name.isupper():
        print(" --> Name is in uppercase")

    # Condition 4: Check if all lowercase
    elif name.islower():
        print(" --> Name is in lowercase")

    else:
        print(" --> Name has mixed case")

    # Final Cleaning Step
    cleaned_name = name.lower()   # Store in a new variable
    cleaned_names.append(cleaned_name)

    print(" --> Cleaned Name:", cleaned_name)
    print() # goes to next line

print("Final Cleaned List:", cleaned_names)
