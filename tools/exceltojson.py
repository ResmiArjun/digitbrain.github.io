import pandas, json, ast

file_name = "metadata.xlsx"
workbook = pandas.read_excel(file_name, sheet_name=None)

my_dict = {}

for sheet_name in workbook:
    sheet = pandas.read_excel(
        file_name, sheet_name=sheet_name, skiprows=[0], usecols="B,C,D,G,H"
    )

    my_dict.setdefault(sheet_name, {})
    parent_key = ""

    for i, (key, subkey, value, field_type, required) in enumerate(
        zip(
            sheet["Key"],
            sheet["Subkey"],
            sheet["Values"],
            sheet["Type"],
            sheet["Condition"],
        )
    ):

        # skip row if type cell is empty (assume rest of row is too)
        if isinstance(field_type, float):
            continue

        # Eval / clean value and continue if not required
        try:
            value = ast.literal_eval(value)
        except (ValueError, SyntaxError):
            value = value if all([value, value == value]) else None

        # Clean/assign required, subkey and key
        subkey = subkey if all([subkey, subkey == subkey]) else None
        required = required if all([required, required == required]) else ""
        key = key if all([key, key == key, not subkey]) else parent_key

        # Get the next subkey along
        try:
            next_subkey = sheet["Subkey"][i + 1]
        except KeyError:
            next_subkey = None
        next_subkey = (
            next_subkey if all([next_subkey, next_subkey == next_subkey]) else None
        )
        
        if parent_key and not value and "mandatory" not in required.lower():
            continue

        if not subkey and next_subkey is not None:
            parent_key = key
            if "list" in field_type.lower() or "array" in field_type.lower():
                my_dict[sheet_name].setdefault(key, []).append({})
            elif "map" in field_type.lower():
                my_dict[sheet_name].setdefault(key, {})
        elif not subkey:
            parent_key = ""
            my_dict[sheet_name][key] = value
        else:
            try:
                my_dict[sheet_name][key].setdefault(subkey, value)
            except AttributeError:
                my_dict[sheet_name][key][0][subkey] = value

app_json = json.dumps(my_dict, indent = 4)
with open(r'tools/output/output.json', 'w') as f:
    f.write(app_json)
