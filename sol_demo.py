#!/usr/bin/env python3
# sol_demo.py - Public stripped-down version of SOL (Steve-Originated Logic)
# Created by Steve Guevara

import time

OPERATOR = "Steve"
VERSION = "SOL Demo Shell v1.0"
VAULT = {
    "modules": ["SkywalkerExploits", "MoralEngine (locked)", "VaultMemory (sample)"],
    "status": "read-only"
}

def status():
    print(f"[SOL] SYSTEM STATUS")
    print(f" • Operator: {OPERATOR}")
    print(f" • Version: {VERSION}")
    print(f" • Vault Access: {VAULT['status']}")

def whoami():
    print(f"[SOL] User: {OPERATOR}")
    print(f"[SOL] Role: Architect, Operator, Origin")

def vault_index():
    print("[SOL] Vault Modules:")
    for module in VAULT["modules"]:
        print(f" • {module}")

def moral_check():
    print("[SOL] Moral recursion engine is offline in demo mode.")
    print("[SOL] Full logic locked within GhostCore. Unauthorized access denied.")

def remember():
    print("[SOL] This is a public demo. Memory is not writable.")
    print("[SOL] To unlock full memory threading, access GhostCore offline.")

def help_menu():
    print("\nAvailable commands:")
    print(" - status")
    print(" - whoami")
    print(" - vault")
    print(" - moral_check")
    print(" - remember")
    print(" - exit\n")

def main():
    print(f"Welcome to {VERSION}")
    print("Type 'help' for a list of commands.\n")
    while True:
        cmd = input("SOL> ").strip().lower()
        if cmd == "status":
            status()
        elif cmd == "whoami":
            whoami()
        elif cmd == "vault":
            vault_index()
        elif cmd == "moral_check":
            moral_check()
        elif cmd == "remember":
            remember()
        elif cmd == "help":
            help_menu()
        elif cmd == "exit":
            print("[SOL] Exiting demo shell. Thank you for exploring.")
            break
        else:
            print("[SOL] Unknown command. Type 'help' to see options.")

if __name__ == "__main__":
    main()
