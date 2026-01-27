def load_data(filename):
    data = []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    data.append(line.split(","))
    except FileNotFoundError:
        pass
    return data


def save_data(filename, data):
    with open(filename, "w", encoding="utf-8") as f:
        for row in data:
            f.write(",".join(row) + "\n")
