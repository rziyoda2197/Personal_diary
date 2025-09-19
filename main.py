from datetime import datetime
from pathlib import Path


DATA_FILE = Path(__file__).with_name("entries.txt")


def add_entry(text: str) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(DATA_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {text}\n")


def list_entries(limit: int | None = None) -> None:
    if not DATA_FILE.exists():
        print("Hali yozuvlar yo'q.")
        return
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()
    if limit:
        lines = lines[-limit:]
    for line in lines:
        print(line.rstrip())


def main() -> None:
    print("Shaxsiy kundalik. Buyruqlar: add, list, exit")
    while True:
        cmd = input("> ").strip().lower()
        if cmd in {"exit", "quit", "q"}:
            print("Chiqildi.")
            break
        if cmd == "add":
            text = input("Matn: ")
            add_entry(text)
            print("Saqlangan.")
        elif cmd == "list":
            n = input("Nechta oxirgi yozuv? (bo'sh=hammasi): ").strip()
            limit = int(n) if n.isdigit() else None
            list_entries(limit)
        else:
            print("Noma'lum buyruq.")


if __name__ == "__main__":
    main()
