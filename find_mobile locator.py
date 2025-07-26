import phonenumbers
from phonenumbers import geocoder
import time, random

def start_phone_tracer(target):
    print(f"[+] PhoneTracer v2.1 - OSINT")
    print(f"[+] Target: {target}")
    print(f"[+] Initiating trace...")
    
    # Parse number
    p = phonenumbers.parse(target, None)
    
    # Get location
    r = geocoder.description_for_number(p, "en")
    
    print(f"[+] Location: {r}")
    print(f"[+] Trace complete")

# Call the function with a proper string
start_phone_tracer("+302821055061")
