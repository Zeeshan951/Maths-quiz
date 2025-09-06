def run_quiz():
    total_points = 0
    total_correct = 0
    total_wrong = 0

    calc_correct = 0
    calc_wrong = 0

    logic_correct = 0
    logic_wrong = 0

    print("📚 Welcome to the Full-Level Math & Logic Quiz!")
    print("You will now go through 3 levels:\n1) Easy (1 mark)\n2) Moderate (2 marks)\n3) Hard (5 marks)")
    input("Press Enter to begin...\n")

    # === EASY LEVEL (CALCULATION) ===
    print("\n🟢 EASY LEVEL (1 mark each)")

    print("\nQ1. What is 768 - 124 + 77?")
    print("1) 711\n2) 721\n3) 641\n4) 661")
    answer = int(input("Your answer: "))
    if answer == 2:
        print("✅ Correct!")
        calc_correct += 1
        total_points += 1
    else:
        print("❌ Wrong!")
        calc_wrong += 1

    print("\nQ2. Area of rectangle (length 12cm, width 5cm)?")
    print("1) 50\n2) 60\n3) 70\n4) 20")
    answer = int(input("Your answer: "))
    if answer == 2:
        print("✅ Correct!")
        calc_correct += 1
        total_points += 1
    else:
        print("❌ Wrong!")
        calc_wrong += 1

    print("\nQ3. What is the square root of 121/121?")
    print("1) 1\n2) 11\n3) 121\n4) 0")
    answer = int(input("Your answer: "))
    if answer == 1:
        print("✅ Correct!")
        calc_correct += 1
        total_points += 1
    else:
        print("❌ Wrong!")
        calc_wrong += 1

    # === MODERATE LEVEL (LOGIC) ===
    print("\n🟡 MODERATE LEVEL (2 marks each)")

    print("\nQ1. LCM of 4 and 6?")
    print("1) 6\n2) 12\n3) 24\n4) 18")
    answer = int(input("Your answer: "))
    if answer == 2:
        print("✅ Correct!")
        logic_correct += 1
        total_points += 2
    else:
        print("❌ Wrong!")
        logic_wrong += 1

    print("\nQ2. Complete the pattern: 2, 3, 5, 9, 17, __")
    print("1) 33\n2) 29\n3) 31\n4) 25")
    answer = int(input("Your answer: "))
    if answer == 1:
        print("✅ Correct!")
        logic_correct += 1
        total_points += 2
    else:
        print("❌ Wrong!")
        logic_wrong += 1

    print("\nQ3. Who gets nothing?")
    print("1) A\n2) C\n3) D\n4) None")
    answer = int(input("Your answer: "))
    if answer == 4:
        print("✅ Correct!")
        logic_correct += 1
        total_points += 2
    else:
        print("❌ Wrong!")
        logic_wrong += 1

    # === HARD LEVEL (LOGIC) ===
    print("\n🔴 HARD LEVEL (5 marks each)")

    print("\nQ1. What 3-digit number leaves remainder 1 when divided by 3, 4, 5?")
    print("1) 61\n2) 60\n3) 59\n4) 75")
    answer = int(input("Your answer: "))
    if answer == 1:
        print("✅ Correct!")
        logic_correct += 1
        total_points += 5
    else:
        print("❌ Wrong!")
        logic_wrong += 1

    print("\nQ2. How many lockers remain open after 100 toggles?")
    print("1) 10\n2) 9\n3) 12\n4) 11")
    answer = int(input("Your answer: "))
    if answer == 1:
        print("✅ Correct!")
        logic_correct += 1
        total_points += 5
    else:
        print("❌ Wrong!")
        logic_wrong += 1

    print("\nQ3. What 2-digit number is twice the sum of its digits?")
    print("1) 18\n2) 24\n3) 36\n4) 27")
    answer = int(input("Your answer: "))
    if answer == 1:
        print("✅ Correct!")
        logic_correct += 1
        total_points += 5
    else:
        print("❌ Wrong!")
        logic_wrong += 1

    # === SUMMARY REPORT ===
    total_correct = calc_correct + logic_correct
    total_wrong = calc_wrong + logic_wrong

    print("\n🎉 QUIZ COMPLETE! 🎉\n")
    print("------ 📊 FINAL REPORT 📊 ------")
    print(f"✅ Total correct answers: {total_correct}")
    print(f"❌ Total wrong answers: {total_wrong}")
    print(f"💯 Total score: {total_points} out of 24")

    print("\nSection-wise performance:")
    print(f"🟢 Easy (Calculation): {calc_correct} correct, {calc_wrong} wrong")
    print(f"🟡 Moderate & 🔴 Hard (Logic): {logic_correct} correct, {logic_wrong} wrong")

    # === FINAL FEEDBACK ===
    print("\n🧠 Analysis:")
    if calc_wrong > logic_wrong:
        print("🧮 You are weaker in CALCULATION. Practice basic math more.")
    elif logic_wrong > calc_wrong:
        print("🧠 You are weaker in LOGICAL REASONING. Practice puzzles and logic problems.")
    elif total_correct == 0:
        print("😓 All answers are wrong. Review both logic and calculation basics.")
    else:
        print("🔥 Great balance! Keep practicing to improve further.")

# === MAIN LOOP ===
while True:
    run_quiz()
    print("\n🔁 Do you want to:")
    print("1) Retest")
    print("2) Exit")
    choice = int(input("Enter your choice: "))
    if choice == 2:
        print("👋 Goodbye! Keep practicing.")        break
