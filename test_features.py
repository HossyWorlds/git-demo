#!/usr/bin/env python3
from auth import authenticate_user

def test_all_features():
    print("=== Testing features in main branch ===")
    
    # Test Feature A
    print("\n1. Testing Feature A (Authentication):")
    if authenticate_user("admin", "password123"):
        print("   ✓ Authentication successful for admin")
    else:
        print("   ✗ Authentication failed")
    
    print("\n2. Feature B (Export) is NOT available in main branch")

if __name__ == "__main__":
    test_all_features()