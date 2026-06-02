error_count = 0
info_count = 0
warning_count = 0

with open("sample_log.txt", "r") as file:
    for line in file:

        if line.startswith("ERROR"):
            error_count += 1
            print(line.strip())

        elif line.startswith("INFO"):
            info_count += 1

        elif line.startswith("WARNING"):
            warning_count += 1

print(f"ERROR: {error_count}")
print(f"INFO: {info_count}")
print(f"WARNING: {warning_count}")
