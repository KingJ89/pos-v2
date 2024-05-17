# report.py
from backend import generate_report

def main():
    report = generate_report()
    print("Report generated successfully.")
    print("Timestamp:", report['timestamp'])
    print("Total value of inventory:", report['total_value'])
    print("Inventory:")
    for product in report['inventory']:
        print(product)

if __name__ == "__main__":
    main()

