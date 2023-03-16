from prettytable import PrettyTable

table = PrettyTable()

table.field_names = ["s.no","company_name","status"]

table.add_row(["1","Oracle","Cleared"])
table.add_row(["2","Cemanti","Not Declared"])
table.add_row(["3","HCL App Scan","Not Declared"])


print(table)

