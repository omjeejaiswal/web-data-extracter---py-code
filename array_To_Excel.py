import pandas as pd

# # Data with prices added
data = {
#     # "Category": [
#     #     " Spices"
#     #     ],
    "Product Name": [
        "Pushp Brand Kashmiri Red Chilli Powder (Pouch Pack of 1)", 
        "Pushp Brand Chilli Powder Spicy Red Chilli Powder (Tikha Tadka)", 
        "Pushp Brand Turmeric Powder Pouch", 
        "Pushp Brand Natural Coriander (Dhaniya) Powder Pouch", 
        "Pushp Brand Combo Pack 200g Each (Chilli Powder, Turmeric Powder, Coriander Powder)", 
        "Pushp Brand Combo Pack 500g Each (Kashmiri Chilli Powder, Turmeric Powder, Coriander Powder)", 
        "Pushp Brand Combo Pack (Chilli Powder 500g, Turmeric Powder 500g, Coriander Powder 500g, Hing 50g)", 
        "Pushp Brand Black Pepper Powder (50g)", 
        "Pushp White Pepper Powder (50g)", 
        "Pushp Brand Black Pepper Powder (100g Pack of 1)", 
        "Pushp White Pepper Powder (100g Pack of 1)", 
        "Pushp Brand Mango Powder Amchur Powder (100g Pack of 1)", 
        "Pushp Brand Kasuri Methi Pouch (100g Pack of 1)", 
        "Pushp Dry Ginger (Adrak) Powder (100g Pack of 1)", 
        "Pushp Brand Dhana Jeera Powder Pouch (500g Pack of 1)", 
        "Pushp Brand Dhana Jeera Powder Pouch (200g Pack of 1)", 
        "Pushp Brand Kashmiri Red Chilli Powder (Pouch Pack of 10, 200g each)", 
        "Pushp Brand Coarse Ground Red Chilli Powder (500g Pack of 10)", 
        "Pushp Brand Chilli Powder (100g Pack of 10)"
    ],
    "Weight": [
        "500 g", 
        "1 kg", 
        "1 kg", 
        "1 kg", 
        "200 g each", 
        "500 g each", 
        "Chilli Powder 500g, Turmeric Powder 500g, Coriander Powder 500g, Hing 50g", 
        "50 g", 
        "50 g", 
        "100 g", 
        "100 g", 
        "100 g", 
        "100 g", 
        "100 g", 
        "500 g", 
        "200 g", 
        "200 g each", 
        "500 g each", 
        "100 g each"
    ],
    "Original Price (₹)": [
        540, 
        564, 
        428, 
        311, 
        270, 
        913, 
        1047, 
        103, 
        153, 
        200, 
        300, 
        59, 
        81, 
        120, 
        244, 
        98, 
        2170, 
        2790, 
        570
    ]

}


# Check the length of each array in the data dictionary
for key, value in data.items():
    print(f"Length of {key}: {len(value)}")

# Creating the DataFrame
df = pd.DataFrame(data)

# Saving to an Excel file
file_path = "MTR_Full_Spices_Product_List.xlsx"
df.to_excel(file_path, index=False)

print(f"Data saved to {file_path}")


