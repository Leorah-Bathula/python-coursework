import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import random
import calendar

# ----------------- 1. Generate Sample Sales Data -----------------
def generate_sales_data(start_date, end_date, n_transactions=2000):
    product_categories = ["Electronics", "Clothing", "Groceries", "Home", "Books", "Sports"]
    data = []
    current_date = start_date
    date_range = (end_date - start_date).days

    for _ in range(n_transactions):
        # random date in range
        rand_days = random.randint(0, date_range)
        date = start_date + timedelta(days=rand_days)

        category = random.choice(product_categories)
        units_sold = random.randint(1, 100)
        price_per_unit = round(random.uniform(5, 500), 2)
        total_sales = round(units_sold * price_per_unit, 2)

        data.append({
            "date": date,
            "category": category,
            "units": units_sold,
            "price": price_per_unit,
            "total": total_sales
        })
    return data

# ----------------- 2. Analysis Functions -----------------
def total_revenue_per_month(data):
    revenue = {}
    for d in data:
        month = d["date"].strftime("%B")
        revenue[month] = revenue.get(month, 0) + d["total"]
    return revenue

def best_selling_category(data):
    category_sales = {}
    for d in data:
        category_sales[d["category"]] = category_sales.get(d["category"], 0) + d["total"]
    return max(category_sales, key=category_sales.get), category_sales

def peak_sales_month(revenue_by_month):
    return max(revenue_by_month, key=revenue_by_month.get)

def average_sales_per_day(data):
    # Use NumPy for mean
    totals = np.array([d["total"] for d in data])
    return np.mean(totals)

def day_with_highest_sales(data):
    daily_sales = {}
    for d in data:
        day = d["date"].date()
        daily_sales[day] = daily_sales.get(day, 0) + d["total"]
    return max(daily_sales, key=daily_sales.get), daily_sales[max(daily_sales, key=daily_sales.get)]

# ----------------- 3. Visualization -----------------
def plot_sales_trends(data):
    # Aggregate daily sales
    daily_totals = {}
    for d in data:
        daily_totals[d["date"].date()] = daily_totals.get(d["date"].date(), 0) + d["total"]
    dates = sorted(daily_totals.keys())
    totals = [daily_totals[day] for day in dates]

    plt.figure(figsize=(10,5))
    plt.plot(dates, totals, marker='o')
    plt.title("Daily Sales Trend")
    plt.xlabel("Date")
    plt.ylabel("Total Sales ($)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_category_bar(category_sales):
    plt.figure(figsize=(7,5))
    plt.bar(category_sales.keys(), category_sales.values(), color="teal")
    plt.title("Total Sales per Product Category")
    plt.xlabel("Category")
    plt.ylabel("Total Sales ($)")
    plt.tight_layout()
    plt.show()

def plot_category_pie(category_sales):
    plt.figure(figsize=(6,6))
    plt.pie(category_sales.values(), labels=category_sales.keys(), autopct="%1.1f%%", startangle=140)
    plt.title("Sales Distribution by Category")
    plt.show()

def plot_sales_histogram(data):
    totals = [d["total"] for d in data]
    plt.figure(figsize=(7,5))
    plt.hist(totals, bins=20, color="orange", edgecolor="black")
    plt.title("Distribution of Sales Amounts")
    plt.xlabel("Sales Amount ($)")
    plt.ylabel("Frequency")
    plt.show()

# ----------------- 4. User Interaction -----------------
def monthly_report(data, month_name):
    month_data = [d for d in data if d["date"].strftime("%B").lower() == month_name.lower()]
    if not month_data:
        print(f"No transactions found for {month_name}.")
        return

    total = sum(d["total"] for d in month_data)
    best_cat, cat_sales = best_selling_category(month_data)

    print(f"\n--- Sales Report for {month_name} ---")
    print(f"Total sales: ${total:,.2f}")
    print(f"Best-selling category: {best_cat}")
    print(f"Number of transactions: {len(month_data)}\n")

    # Optional graphs filtered for the month
    plot_category_bar(cat_sales)
    plot_category_pie(cat_sales)

# ----------------- Main -----------------
def main():
    # 6-month range (e.g., Jan to Jun of current year)
    today = datetime.today()
    start_date = today.replace(month=1, day=1)   # adjust if running mid-year
    end_date = start_date + timedelta(days=180)

    data = generate_sales_data(start_date, end_date, n_transactions=2500)

    # Summary
    revenue_by_month = total_revenue_per_month(data)
    best_cat, category_sales = best_selling_category(data)
    peak_month = peak_sales_month(revenue_by_month)
    avg_daily = average_sales_per_day(data)
    best_day, best_day_sales = day_with_highest_sales(data)

    print("\n===== Overall Summary =====")
    print(f"Total sales revenue: ${sum(d['total'] for d in data):,.2f}")
    print(f"Best-selling category: {best_cat}")
    print(f"Peak sales month: {peak_month}")
    print(f"Average sales per transaction: ${avg_daily:,.2f}")
    print(f"Highest single-day sales: {best_day} with ${best_day_sales:,.2f}")

    # Visualizations
    plot_sales_trends(data)
    plot_category_bar(category_sales)
    plot_category_pie(category_sales)
    plot_sales_histogram(data)

    # User interaction
    while True:
        month_input = input("\nEnter a month name for detailed analysis (or 'exit'): ").strip()
        if month_input.lower() == "exit":
            break
        if month_input.capitalize() in calendar.month_name:
            monthly_report(data, month_input)
        else:
            print("Please enter a valid month name (e.g., January).")

if __name__ == "__main__":
    main()
