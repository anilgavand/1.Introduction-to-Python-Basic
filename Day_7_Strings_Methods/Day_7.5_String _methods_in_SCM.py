
# Python String Methods – Practical Examples in SAP MM & Procurement


# Example 1. Removing Spaces from Leading and Trailing

Material = "     RAW MATERIAL STEEL     "

print("Original Material Description :", Material)
print("Remove Spaces Output:", Material.strip())

# Example 2. Convert Material Description into Uppercase

Material = "     stainless steel sheet     "

print("Original Material Description :", Material)
print("Upper Letter Output :", Material.strip().upper())

# Without strip()

Material = "     stainless steel sheet     "

print("Original Material Description :", Material)
print("Upper Letter Output            :", Material.upper())

# Example 3. Convert Supplier Name into Title Case

Supplier = "     abc engineering industries pvt ltd     "

print("Original Supplier Name :", Supplier)
print("Proper Letter Output   :", Supplier.title().strip())

# Example 4. Convert Supplier Email into Lowercase

Email = "     PURCHASE@ROVEMA.COM     "

print("Original Email :", Email)
print("Lower Letter Output :", Email.lower().strip())

# Example 5. Replace Material Description

Material = "     SAP MM Procurement Data     "

print("Original Material Description :", Material)

print("Replace SAP MM with SAP S4HANA :",
         Material.replace("SAP MM", "SAP S4HANA").strip())


# Example 6. Count Occurrence of Character

Material = "     Stainless Steel Material     "

print("Original Material Description :", Material)

print("Count of 'a' is :", Material.count("a"))
print("Count of 't' is :", Material.count("t"))

# Example 7. Check Supplier Name Starts with Some Word

Supplier = "     ROVEMA GMBH     "

print("Original Supplier Name :", Supplier)

print("Start with ROVEMA ? :",
      Supplier.strip().startswith("ROVEMA"))

# Example 8. Check Whether Material Number is Numeric

Material_Number = "5001234567"

print("Material Number is Numeric ? :", Material_Number.isnumeric())

# Supplier Name

Supplier = "ROVEMA123"

print("Supplier Name is Numeric ? :", Supplier.isnumeric())

# Purchase Order Number

PO_Number = "4500012345"

print("Purchase Order Number is Numeric ? :", PO_Number.isnumeric())


# Example 9. Split Material Description

Material = "Stainless Steel Sheet 2MM"

print("Original Material Description :", Material)

print("Split Material Description :", Material.split())


# Example 10. Join Material Description with Hyphen

Material = "Stainless Steel Sheet 2MM"

Split_Material = Material.split()

Joined_Text = "-".join(Split_Material)

print("Original Material Description :", Material)
print("Joined Material Description   :", Joined_Text)


# Example 11. Find Position of Character in Supplier Name

Supplier = "ROVEMA GMBH"

print("Supplier Name :", Supplier)

print("Find Position of 'G' :", Supplier.find("G"))

# Example 12. Extract Domain from Supplier Email

Email = "purchase@rovema.com"

Domain = Email[Email.find("@") + 1:]

print("Supplier Email :", Email)
print("Domain Name    :", Domain)


# Example 13. Extract Material Number from Reference

PO_Reference = "PO-4500012345-MAT-500123"

Material_Number = PO_Reference.split("-")[-1]

print("Purchase Order Reference :", PO_Reference)
print("Extracted Material Number :", Material_Number)


# Example 14. lstrip(), rstrip() and strip()

Supplier = "     Rovema Gmbh     "

print("Original Supplier Name :", Supplier)
print("Remove Left Spaces     :", Supplier.lstrip())
print("Remove Right Spaces    :", Supplier.rstrip())
print("Remove Both Side Spaces:", Supplier.strip())

