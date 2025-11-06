import pandas as pd
import sqlite3

# Homework 1:
# Using chinook.db write pandas code.
# Customer Purchases Analysis:
# 1. Find the total amount spent by each customer on purchases (considering invoices).

conn = sqlite3.connect("chinook.db")

invoices = pd.read_sql_query("SELECT * FROM Invoice;", conn)
customers = pd.read_sql_query("SELECT * FROM Customer;", conn)

customer_purchases = pd.merge(customers, invoices, on="CustomerId")

total_spent = (
    customer_purchases.groupby(["CustomerId", "FirstName", "LastName"])["Total"]
    .sum()
    .reset_index()
    .sort_values(by="Total", ascending=False)
)

print(total_spent.head(10))

conn.close()

# 2. Identify the top 5 customers with the highest total purchase amounts.
conn = sqlite3.connect("chinook.db")

invoices = pd.read_sql_query("SELECT * FROM Invoice;", conn)
customers = pd.read_sql_query("SELECT * FROM Customer;", conn)

customer_purchases = pd.merge(customers, invoices, on="CustomerId")

total_spent = (
    customer_purchases.groupby(["CustomerId", "FirstName", "LastName"])["Total"]
    .sum()
    .reset_index()
    .sort_values(by="Total", ascending=False)
)

top_5_customers = total_spent.head(5)

print(top_5_customers)

conn.close()

# 3. Display the customer ID, name, and the total amount spent for the top 5 customers.
conn = sqlite3.connect("chinook.db")

invoices = pd.read_sql_query("SELECT * FROM Invoice;", conn)
customers = pd.read_sql_query("SELECT * FROM Customer;", conn)

merged = pd.merge(customers, invoices, on="CustomerId")

customer_spending = (
    merged.groupby(["CustomerId", "FirstName", "LastName"])["Total"]
    .sum()
    .reset_index()
)

customer_spending["FullName"] = customer_spending["FirstName"] + " " + customer_spending["LastName"]

top_5 = customer_spending.sort_values(by="Total", ascending=False).head(5)

top_5 = top_5[["CustomerId", "FullName", "Total"]]

print(top_5)
conn.close()

# Album vs. Individual Track Purchases:
# 1. Determine the percentage of customers who prefer to buy individual tracks instead of full albums.
conn = sqlite3.connect("chinook.db")

invoices = pd.read_sql_query("SELECT * FROM Invoice;", conn)
invoice_lines = pd.read_sql_query("SELECT * FROM InvoiceLine;", conn)
tracks = pd.read_sql_query("SELECT TrackId, AlbumId FROM Track;", conn)

invoice_details = pd.merge(invoice_lines, tracks, on="TrackId")

invoice_summary = invoice_details.groupby("InvoiceId").agg({
    "AlbumId": "nunique",
    "TrackId": "count"
}).reset_index()

invoice_summary["PurchaseType"] = invoice_summary.apply(
    lambda x: "Individual Track" if x["AlbumId"] > 1 else "Full Album",
    axis=1
)

invoice_summary = pd.merge(invoice_summary, invoices[["InvoiceId", "CustomerId"]], on="InvoiceId")

customer_preference = (
    invoice_summary.groupby("CustomerId")["PurchaseType"]
    .agg(lambda x: x.value_counts().idxmax())
    .reset_index()
)

individual_percent = (
    (customer_preference["PurchaseType"] == "Individual Track").sum()
    / len(customer_preference)
    * 100
)

print(f"Percentage of customers who prefer individual tracks: {individual_percent:.2f}%")
conn.close()

# 2. A customer is considered to prefer individual tracks if they have purchased only a subset of tracks from an album.
conn = sqlite3.connect("chinook.db")

invoice_lines = pd.read_sql_query("SELECT * FROM InvoiceLine;", conn)
invoices = pd.read_sql_query("SELECT * FROM Invoice;", conn)
tracks = pd.read_sql_query("SELECT TrackId, AlbumId FROM Track;", conn)

data = invoice_lines.merge(tracks, on="TrackId").merge(invoices[["InvoiceId", "CustomerId"]], on="InvoiceId")

album_track_counts = tracks.groupby("AlbumId")["TrackId"].count().reset_index()
album_track_counts.rename(columns={"TrackId": "TotalTracks"}, inplace=True)

customer_album_purchases = (
    data.groupby(["CustomerId", "AlbumId"])["TrackId"]
    .nunique()
    .reset_index()
    .rename(columns={"TrackId": "TracksPurchased"})
)

customer_album_purchases = customer_album_purchases.merge(album_track_counts, on="AlbumId")

customer_album_purchases["SubsetPurchase"] = customer_album_purchases["TracksPurchased"] < customer_album_purchases["TotalTracks"]

customers_preferring_tracks = (
    customer_album_purchases.groupby("CustomerId")["SubsetPurchase"]
    .any()
    .reset_index()
)

percentage_individual_pref = (
    customers_preferring_tracks["SubsetPurchase"].sum() / len(customers_preferring_tracks) * 100
)

print(f"Percentage of customers who prefer individual tracks: {percentage_individual_pref:.2f}%")
conn.close()

# 3. Provide a summary of the percentage of customers who fall into each category (individual tracks vs. full albums).
conn = sqlite3.connect("chinook.db")

invoice_lines = pd.read_sql_query("SELECT * FROM InvoiceLine;", conn)
invoices = pd.read_sql_query("SELECT * FROM Invoice;", conn)
tracks = pd.read_sql_query("SELECT TrackId, AlbumId FROM Track;", conn)

data = invoice_lines.merge(tracks, on="TrackId").merge(
    invoices[["InvoiceId", "CustomerId"]], on="InvoiceId"
)

album_track_counts = tracks.groupby("AlbumId")["TrackId"].count().reset_index()
album_track_counts.rename(columns={"TrackId": "TotalTracks"}, inplace=True)

customer_album_purchases = (
    data.groupby(["CustomerId", "AlbumId"])["TrackId"]
    .nunique()
    .reset_index()
    .rename(columns={"TrackId": "TracksPurchased"})
)

customer_album_purchases = customer_album_purchases.merge(album_track_counts, on="AlbumId")

customer_album_purchases["SubsetPurchase"] = (
    customer_album_purchases["TracksPurchased"] < customer_album_purchases["TotalTracks"]
)

customer_preference = (
    customer_album_purchases.groupby("CustomerId")["SubsetPurchase"]
    .any()
    .reset_index()
)

customer_preference["Preference"] = customer_preference["SubsetPurchase"].apply(
    lambda x: "Individual Tracks" if x else "Full Albums"
)

summary = (
    customer_preference["Preference"]
    .value_counts(normalize=True)
    .mul(100)
    .reset_index()
    .rename(columns={"index": "Preference", "Preference": "Percentage"})
)

print(summary)
conn.close()