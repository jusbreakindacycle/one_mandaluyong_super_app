import json
import csv
import random
import uuid
from datetime import datetime, timedelta
from faker import Faker

fake = Faker(["en_PH"])
Faker.seed(42)
random.seed(42)

FIRST_NAMES_M = [
    "Juan", "Jose", "Antonio", "Mark", "John", "Carlo", "Miguel", "Rafael",
    "Angelo", "Christian", "Paolo", "Ramon", "Ricardo", "Ronnel", "Ferdinand",
    "Eduardo", "Manuel", "Renato", "Danilo", "Arnel", "Bryan", "Kevin",
    "Nathaniel", "Vincent", "Julius", "Marlon", "Reynaldo", "Alvin", "Noel",
    "Emmanuel",
]
FIRST_NAMES_F = [
    "Maria", "Ana", "Grace", "Angelica", "Jasmin", "Cristina", "Josephine",
    "Michelle", "Rowena", "Liza", "Karen", "Jennylyn", "Regina", "Charmaine",
    "Ma. Theresa", "Cherry", "Divina", "Precious", "Angel", "Kristine",
    "Katherine", "Marianne", "Lourdes", "Corazon", "Fe", "Erlinda", "Perla",
    "Jocelyn", "Marites", "Vilma",
]
LAST_NAMES = [
    "Santos", "Reyes", "Cruz", "Bautista", "Ocampo", "Garcia", "Mendoza",
    "Torres", "Del Rosario", "Aquino", "Flores", "Ramos", "Villanueva",
    "Castillo", "Domingo", "Salazar", "Marquez", "Gonzales", "Pascual",
    "Fernandez", "Aguilar", "Navarro", "Rivera", "Dela Cruz", "Tolentino",
    "Manalo", "Bermudez", "Alonzo", "Custodio", "Espiritu", "Lazaro",
    "Panganiban", "Robles", "Sarmiento", "Uy", "Tan", "Sy", "Lim", "Chua",
]

def filipino_name():
    sex = random.choice(["M", "F"])
    first = random.choice(FIRST_NAMES_M if sex == "M" else FIRST_NAMES_F)
    last = random.choice(LAST_NAMES)
    middle_initial = random.choice(LAST_NAMES)[0]
    return f"{first} {middle_initial}. {last}", sex

BUSINESS_SUFFIXES = ["Enterprises", "Trading", "Services", "Corp.", "General Merchandise", "Store", "Food House"]

def filipino_business_name():
    owner_surname = random.choice(LAST_NAMES)
    style = random.choice(["surname_biz", "generic"])
    if style == "surname_biz":
        return f"{owner_surname} {random.choice(BUSINESS_SUFFIXES)}"
    else:
        adjectives = ["Mabuhay", "Bayanihan", "Ligaya", "Masaya", "Malinis", "Tahanan", "Pag-Asa", "Bagong"]
        nouns = ["Trading", "Enterprises", "Foods", "Services", "General Merchandise"]
        return f"{random.choice(adjectives)} {random.choice(nouns)}"

# Safe synthetic email domains, reserved for documentation/example use under
# RFC 2606 — guaranteed to never resolve to a real inbox, unlike real
# providers (gmail.com, yahoo.com, etc.) combined with random usernames.
SAFE_EMAIL_DOMAINS = ["example.com", "example.org", "example.net"]

def safe_email(full_name):
    # Derive the username from the same Filipino name used for the record,
    # instead of a fresh fake.user_name() call (which uses Faker's default
    # locale and produces American-pattern usernames like "fjohnson" or
    # "lisa02" stapled onto Filipino citizen names).
    first_last = full_name.replace(".", "").split()
    first = first_last[0].lower()
    last = first_last[-1].lower()
    suffix = random.choice(["", str(random.randint(1, 99))])
    username = f"{first}.{last}{suffix}"
    return f"{username}@{random.choice(SAFE_EMAIL_DOMAINS)}"

# Reserved documentation IP ranges under RFC 5737 — guaranteed to never
# route to a real host, unlike fake.ipv4_public() which can generate real,
# live, currently-allocated public addresses.
RESERVED_IP_BLOCKS = ["192.0.2.", "198.51.100.", "203.0.113."]

def safe_ipv4():
    return f"{random.choice(RESERVED_IP_BLOCKS)}{random.randint(1, 254)}"

# Real Mandaluyong barangays (public knowledge, not personal data)
BARANGAYS = [
    "Addition Hills", "Bagong Silang", "Barangka Drive", "Barangka Ibaba",
    "Barangka Ilaya", "Barangka Itaas", "Buayang Bato", "Burol", "Daang Bakal",
    "Hagdang Bato Itaas", "Hagdang Bato Libis", "Harapin Ang Bukas",
    "Highway Hills", "Hulo", "Mabini-J. Rizal", "Malamig", "Mauway",
    "Namayan", "New Zaniga", "Old Zaniga", "Pag-asa", "Plainview",
    "Pleasant Hills", "Poblacion", "San Jose", "Vergara", "Wack-Wack Greenhills",
]

BUSINESS_TYPES = [
    "Sari-Sari Store", "Restaurant/Eatery", "Retail Trading", "Beauty Salon/Spa",
    "Internet Cafe", "Auto Repair Shop", "Bakery", "Pharmacy", "Grocery Store",
    "Laundry Shop", "Tailoring Shop", "Photocopy/Printing Services",
    "Real Estate Services", "IT/Software Services", "Food Cart/Kiosk",
]

PERMIT_TYPES = [
    "New Business Permit", "Business Permit Renewal", "Barangay Clearance",
    "Building Permit", "Sanitary Permit", "Occupancy Permit",
    "Locational Clearance", "Fire Safety Inspection Certificate",
]

PERMIT_STATUSES = ["Pending Review", "Under Evaluation", "Approved", "Released", "Denied", "Expired"]

PAYMENT_METHODS = ["GCash", "Maya", "Credit Card", "Debit Card", "Over-the-Counter", "Bank Transfer"]
PAYMENT_STATUSES = ["Completed", "Pending", "Failed", "Refunded"]

AUDIT_ACTIONS = [
    "LOGIN", "LOGOUT", "RECORD_CREATED", "RECORD_UPDATED", "RECORD_VIEWED",
    "PERMIT_STATUS_CHANGED", "PAYMENT_INITIATED", "PAYMENT_CONFIRMED",
    "DOCUMENT_UPLOADED", "DOCUMENT_DOWNLOADED", "PERMISSION_DENIED",
]

MODULES = [
    "citizen-identity", "business-registration", "payments", "digital-documents",
    "appointments", "case-management",
]

def random_date(start_days_ago=365, end_days_ago=0):
    start = datetime.now() - timedelta(days=start_days_ago)
    end = datetime.now() - timedelta(days=end_days_ago)
    delta = end - start
    random_seconds = random.randint(0, int(delta.total_seconds()))
    return start + timedelta(seconds=random_seconds)

def make_ref(prefix):
    return f"{prefix}-{datetime.now().year}-{uuid.uuid4().hex[:8].upper()}"

# ---------- 1. Citizen Profiles (fictional) ----------
citizens = []
for i in range(1, 521):
    dob = fake.date_of_birth(minimum_age=18, maximum_age=75)
    name, sex = filipino_name()
    citizens.append({
        "citizen_id": f"CIT-{i:06d}",
        "full_name": name,
        "date_of_birth": dob.isoformat(),
        "sex": "Male" if sex == "M" else "Female",
        "civil_status": random.choice(["Single", "Married", "Widowed", "Separated"]),
        "barangay": random.choice(BARANGAYS),
        "mobile_number": fake.numerify("09#########"),
        "email": safe_email(name),
        "registered_date": random_date(400, 30).isoformat(timespec="seconds"),
        "account_status": random.choices(["Active", "Inactive", "Pending Verification"], weights=[85, 10, 5])[0],
    })

# ---------- 2. Business Permit Applications ----------
permits = []
for i in range(1, 541):
    citizen = random.choice(citizens)
    filed = random_date(300, 1)
    status = random.choice(PERMIT_STATUSES)
    permits.append({
        "permit_id": make_ref("PERMIT"),
        "citizen_id": citizen["citizen_id"],
        "applicant_name": citizen["full_name"],
        "permit_type": random.choice(PERMIT_TYPES),
        "business_name": filipino_business_name() if random.random() > 0.3 else "",
        "business_type": random.choice(BUSINESS_TYPES),
        "barangay": citizen["barangay"],
        "date_filed": filed.isoformat(timespec="seconds"),
        "status": status,
        "date_released": (filed + timedelta(days=random.randint(1, 15))).isoformat(timespec="seconds") if status in ("Approved", "Released") else "",
        "processing_days": random.randint(1, 20),
        "ra_11032_compliant": random.choices([True, False], weights=[88, 12])[0],
    })

# ---------- 3. Payment Transactions ----------
payments = []
for i in range(1, 531):
    permit = random.choice(permits)
    txn_date = datetime.fromisoformat(permit["date_filed"]) + timedelta(hours=random.randint(1, 48))
    payments.append({
        "payment_id": make_ref("PAY"),
        "permit_id": permit["permit_id"],
        "citizen_id": permit["citizen_id"],
        "amount_php": round(random.uniform(150, 8500), 2),
        "payment_method": random.choice(PAYMENT_METHODS),
        "status": random.choices(PAYMENT_STATUSES, weights=[85, 8, 5, 2])[0],
        "transaction_date": txn_date.isoformat(timespec="seconds"),
        "reference_number": fake.numerify("REF#############"),
    })

# ---------- 4. Audit / Activity Logs ----------
audit_logs = []
for i in range(1, 561):
    citizen = random.choice(citizens)
    action = random.choice(AUDIT_ACTIONS)
    audit_logs.append({
        "log_id": make_ref("LOG"),
        "timestamp": random_date(200, 0).isoformat(timespec="seconds"),
        "actor_id": citizen["citizen_id"],
        "actor_type": random.choices(["Citizen", "Department Staff", "System"], weights=[70, 25, 5])[0],
        "action": action,
        "module": random.choice(MODULES),
        "ip_address": safe_ipv4(),
        "result": random.choices(["Success", "Failure"], weights=[95, 5])[0],
    })

# ---------- Write outputs ----------
datasets = {
    "citizens": citizens,
    "business_permits": permits,
    "payments": payments,
    "audit_logs": audit_logs,
}

import os
out_dir = os.path.dirname(os.path.abspath(__file__))
os.makedirs(out_dir, exist_ok=True)

for name, rows in datasets.items():
    # JSON
    with open(f"{out_dir}/{name}.json", "w", encoding="utf-8") as f:
        json.dump(rows, f, indent=2, ensure_ascii=False)
    # CSV
    with open(f"{out_dir}/{name}.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    print(f"{name}: {len(rows)} records")

total = sum(len(v) for v in datasets.values())
print(f"TOTAL: {total} records across {len(datasets)} datasets")
