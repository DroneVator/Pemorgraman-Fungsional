expenses = [
    {'tanggal': '2023-07-25', 'deskripsi': 'Makan Siang', 'jumlah': 50000},
    {'tanggal': '2023-07-25', 'deskripsi': 'Transportasi', 'jumlah': 25000},
    {'tanggal': '2023-07-26', 'deskripsi': 'Belanja', 'jumlah': 100000},
]

# TODO 1


def add_expense(expenses_list, expense):
    return expenses_list + [expense]


# TODO 2
def calculate_total_expenses(expenses_list): return sum(
    expense['jumlah'] for expense in expenses_list)

# TODO 3


def get_expenses_by_date(expenses_list, date): return [
    expense for expense in expenses_list if expense['tanggal'] == date]

# TODO 4


def generate_expenses_report(expenses_list):
    for expense in expenses_list:
        yield f"Date: {expense['tanggal']}, Description: {expense['deskripsi']}, Amount: Rp {expense['jumlah']}"

# Function to add expense interactively


def add_expense_interactively(expenses_list):
    date = input("Masukkan tanggal pengeluaran (YYYY-MM-DD): ")
    description = input("Masukkan deskripsi pengeluaran: ")
    amount = int(input("Masukkan jumlah pengeluaran: "))
    new_expense = {
        'tanggal': date,
        'deskripsi': description,
        'jumlah': amount
    }
    new_expenses = add_expense(expenses_list, new_expense)
    print("Pengeluaran berhasil ditambahkan.")
    return new_expenses


def view_expenses_by_date(expenses_list):
    date = input("Masukkan tanggal (YYYY-MM-DD): ")
    expenses_on_date = get_expenses_by_date(expenses_list, date)
    print(f"\nPengeluaran pada tanggal {date}:")
    for expense in expenses_on_date:
        print(f"{expense['deskripsi']} - Rp {expense['jumlah']}")


def view_expenses_report(expenses_list):
    print("\nLaporan Pengeluaran Harian:")
    expenses_report = generate_expenses_report(expenses_list)
    for entry in expenses_report:
        print(entry)


def display_menu():
    print("\n===== Aplikasi Pencatat Pengeluaran Harian =====")
    print("1. Tambah Pengeluaran")
    print("2. Total Pengeluaran Harian")
    print("3. Lihat Pengeluaran berdasarkan Tanggal")
    print("4. Lihat Laporan Pengeluaran Harian")
    print("5. Keluar")


# TODO 6
def get_user_input(command): return int(input(command))


def main():
    global expenses
    while True:
        display_menu()
        choice = get_user_input("Pilih menu (1/2/3/4/5): ")
        if choice == 1:
            expenses = add_expense_interactively(expenses)
        elif choice == 2:
            total_expenses = calculate_total_expenses(expenses)
            print(f"\nTotal Pengeluaran Harian: Rp {total_expenses}")
        elif choice == 3:
            view_expenses_by_date(expenses)
        elif choice == 4:
            view_expenses_report(expenses)
        elif choice == 5:
            print("Terima kasih telah menggunakan aplikasi kami.")
            break
        else:
            print("Pilihan tidak valid. Silahkan pilih menu yang benar.")


if __name__ == "__main__":
    main()
