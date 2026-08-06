# ==========================================
# Assignment: Random Module
# Topic: Generate 6-Digit OTP
# Condition:
# OTP should not contain three consecutive numbers.
# ==========================================

import random

while True:

    otp = ""

    # Generate a 6-digit OTP
    for i in range(6):
        otp = otp + str(random.randint(0, 9))

    valid = True

    # Check for three consecutive numbers
    for i in range(len(otp) - 2):

        a = int(otp[i])
        b = int(otp[i + 1])
        c = int(otp[i + 2])

        # Increasing consecutive numbers
        if b == a + 1 and c == b + 1:
            valid = False
            break

        # Decreasing consecutive numbers
        if b == a - 1 and c == b - 1:
            valid = False
            break

    if valid:
        print("Generated OTP:", otp)
        break