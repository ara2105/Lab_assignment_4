class FlightTable:
    def __init__(self):
        self.entries = []

    def add_entry(self, p_id, process, start_time, priority):
        self.entries.append((p_id, process, start_time, priority))

    def sort_table(self, sort_key):
        if sort_key == 1:
            self.entries.sort(key=lambda entry: entry[0])
        elif sort_key == 2:
            self.entries.sort(key=lambda entry: entry[2])
        elif sort_key == 3:
            self.entries.sort(key=lambda entry: entry[3], reverse=True)

    def display_table(self):
        print("{:<5} {:<10} {:<15} {}".format("P_ID", "Process", "Start Time (ms)", "Priority"))
        print("=" * 45)
        for entry in self.entries:
            print("{:<5} {:<10} {:<15} {}".format(entry[0], entry[1], entry[2], entry[3]))
        print("=" * 45)


def main():
    flight_table = FlightTable()

    flight_table.add_entry("P1", "VSCode", 100, "MID")
    flight_table.add_entry("P23", "Eclipse", 234, "MID")
    flight_table.add_entry("P93", "Chrome", 189, "High")
    flight_table.add_entry("P42", "JDK", 9, "High")
    flight_table.add_entry("P9", "CMD", 7, "High")
    flight_table.add_entry("P87", "NotePad", 23, "Low")

    while True:
        print("\nSort Options:")
        print("1. Sort by P_ID\n2. Sort by Start Time\n3. Sort by Priority")
        choice = int(input("Enter your choice (1/2/3): "))

        if choice in [1, 2, 3]:
            flight_table.sort_table(choice)
            flight_table.display_table()
        else:
            print("Invalid choice. Exiting.")
            break


if __name__ == "__main__":
    main()
