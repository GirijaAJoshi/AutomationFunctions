from am import ApplianceManager

am = ApplianceManager("10.100.100.10", "Admin","Admin1!")
print (am)
am.get_log_files()