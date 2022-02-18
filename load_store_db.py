from db import Database


# Populate parts table - Only run it once initially
db = Database("store.db")

db.insert("24in Monitor", "John Doe", "Best Buy", "120")
db.insert("16GB USB", "Kim Walls", "Radio Shack", "12")
db.insert("Pent Harddrive", "Samantha Spores", "Wal-mart", "50")