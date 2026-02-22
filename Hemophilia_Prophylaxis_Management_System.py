# ============================================================
# CONSTANTS
# ============================================================

PRICE_PLASMA = 0.3
PRICE_RECOMBINANT = 0.4
VIALS = [2000, 1500, 1000, 500, 250]

# ============================================================
# GENERAL COUNTERS
# ============================================================

patient_count = 0
hemo_a_count = 0
hemo_b_count = 0

severe_count = 0
moderate_count = 0
mild_count = 0

inhibitor_a_count = 0
inhibitor_b_count = 0

prophylaxis_a_count = 0
prophylaxis_b_count = 0
moderate_prophylaxis_count = 0

plasma_a_count = 0
recom_a_count = 0
plasma_b_count = 0
recom_b_count = 0

total_iu_4_weeks = 0
total_cost_4_weeks = 0

total_f8_plasma = 0
total_f8_recom = 0
total_f9_plasma = 0
total_f9_recom = 0

total_vials_4_weeks = [0, 0, 0, 0, 0]

max_cost = -1
max_cost_data = {}

max_iu_a = -1
max_iu_a_data = {}

max_iu_b = -1
max_iu_b_data = {}

# ============================================================
# MAIN LOOP
# ============================================================

continue_status = "y"

while continue_status.lower() == "y":

    patient_count += 1
    print("\n------------------------------")
    print("PATIENT", patient_count)

    tr_id = input("TR ID: ")
    name = input("Name Surname: ")

    prot_num = int(input("Deficient factor (8/9): "))
    while prot_num not in [8, 9]:
        prot_num = int(input("Enter 8 or 9: "))

    f_level = float(input("Factor level (0-50): "))
    while not (0 <= f_level < 50):
        f_level = float(input("Enter between 0 and 50: "))

    antibody = float(input("Antibody (>=0): "))
    while antibody < 0:
        antibody = float(input("Enter >=0: "))

    # Severity
    if f_level < 1:
        severity = "Severe"
        severe_count += 1
    elif f_level <= 5:
        severity = "Moderate"
        moderate_count += 1
    else:
        severity = "Mild"
        mild_count += 1

    # Disease type
    if prot_num == 8:
        disease_type = "A"
        hemo_a_count += 1
    else:
        disease_type = "B"
        hemo_b_count += 1

    # Inhibitor
    has_inhibitor = antibody >= 5
    if has_inhibitor:
        if prot_num == 8:
            inhibitor_a_count += 1
        else:
            inhibitor_b_count += 1

    # Prophylaxis eligibility
    bleeding = 0
    if severity == "Moderate":
        bleeding = int(input("Bleeding episodes last year: "))
        while bleeding < 0:
            bleeding = int(input("Enter >=0: "))

    eligible = False
    if not has_inhibitor:
        if severity == "Severe" or (severity == "Moderate" and bleeding >= 36):
            eligible = True

    # =====================================================
    # IF PROPHYLAXIS
    # =====================================================

    if eligible:

        if severity == "Moderate":
            moderate_prophylaxis_count += 1

        weight = float(input("Weight (kg): "))
        while weight <= 0:
            weight = float(input("Enter >0: "))

        prod_type = input("Production type (P/R): ").upper()
        while prod_type not in ["P", "R"]:
            prod_type = input("Enter P or R: ").upper()

        if prot_num == 8:
            times_per_week = 3
            increase_factor = 2
        else:
            times_per_week = 2
            increase_factor = 1

        min_dose = (weight * (40 - f_level)) / increase_factor

        # Vial calculation
        remaining = min_dose
        vial_counts_single = [0, 0, 0, 0, 0]
        actual_single_dose = 0

        for i in range(len(VIALS)):
            vial_counts_single[i] = int(remaining // VIALS[i])
            remaining = remaining % VIALS[i]
            actual_single_dose += vial_counts_single[i] * VIALS[i]

        if remaining > 0:
            vial_counts_single[-1] += 1
            actual_single_dose += 250

        # 4 weeks totals
        dose_4_weeks = actual_single_dose * times_per_week * 4
        vial_counts_4_weeks = []
        for i in range(len(vial_counts_single)):
            vial_counts_4_weeks.append(vial_counts_single[i] * times_per_week * 4)
            total_vials_4_weeks[i] += vial_counts_4_weeks[i]

        unit_price = PRICE_PLASMA if prod_type == "P" else PRICE_RECOMBINANT
        cost_4_weeks = dose_4_weeks * unit_price

        total_iu_4_weeks += dose_4_weeks
        total_cost_4_weeks += cost_4_weeks

        # Update type totals
        if prot_num == 8:
            prophylaxis_a_count += 1
            if prod_type == "P":
                plasma_a_count += 1
                total_f8_plasma += dose_4_weeks
            else:
                recom_a_count += 1
                total_f8_recom += dose_4_weeks
        else:
            prophylaxis_b_count += 1
            if prod_type == "P":
                plasma_b_count += 1
                total_f9_plasma += dose_4_weeks
            else:
                recom_b_count += 1
                total_f9_recom += dose_4_weeks

        # MAX COST
        if cost_4_weeks > max_cost:
            max_cost = cost_4_weeks
            max_cost_data = {
                "id": tr_id,
                "name": name,
                "type": disease_type,
                "severity": severity,
                "weight": weight,
                "prod": prod_type,
                "iu": dose_4_weeks,
                "cost": cost_4_weeks
            }

        # MAX IU
        if prot_num == 8 and dose_4_weeks > max_iu_a:
            max_iu_a = dose_4_weeks
            max_iu_a_data = {
                "id": tr_id,
                "name": name,
                "severity": severity,
                "weight": weight,
                "prod": prod_type,
                "iu": dose_4_weeks,
                "cost": cost_4_weeks
            }

        if prot_num == 9 and dose_4_weeks > max_iu_b:
            max_iu_b = dose_4_weeks
            max_iu_b_data = {
                "id": tr_id,
                "name": name,
                "severity": severity,
                "weight": weight,
                "prod": prod_type,
                "iu": dose_4_weeks,
                "cost": cost_4_weeks
            }

    # =====================================================
    # INDIVIDUAL OUTPUT
    # =====================================================

    print("\nPatient:", tr_id, name)
    print("Type: Hemophilia", disease_type)
    print("Severity:", severity)
    print("Prophylaxis:", "Yes" if eligible else "No")

    if eligible:
        print("Factor:", "Factor-8" if prot_num == 8 else "Factor-9")
        print("Production:", "Plasma-derived" if prod_type == "P" else "Recombinant")
        print("Times per week:", times_per_week)
        print("Minimum required dose:", round(min_dose, 2), "IU")
        print("Actual single dose:", actual_single_dose, "IU")

        print("Single dose vial distribution:")
        for i in range(len(VIALS)):
            if vial_counts_single[i] > 0:
                print(VIALS[i], "IU x", vial_counts_single[i])

        print("4-week total IU:", dose_4_weeks)
        print("4-week vial distribution:")
        for i in range(len(VIALS)):
            if vial_counts_4_weeks[i] > 0:
                print(VIALS[i], "IU x", vial_counts_4_weeks[i])

        print("4-week cost: $", format(cost_4_weeks, ".2f"))

    continue_status = input("\nAnother patient? (y/n): ")

# ============================================================
# FINAL REPORT
# ============================================================

print("\n===================================================")
print("FINAL SYSTEM REPORT")
print("===================================================")

print("Total patients:", patient_count)
print("Hemophilia A:", hemo_a_count)
print("Hemophilia B:", hemo_b_count)

print("Severe:", severe_count, "(", format(severe_count/patient_count*100, ".2f"), "% )")
print("Moderate:", moderate_count, "(", format(moderate_count/patient_count*100, ".2f"), "% )")
print("Mild:", mild_count, "(", format(mild_count/patient_count*100, ".2f"), "% )")

if hemo_a_count > 0:
    print("Inhibitor A %:", format(inhibitor_a_count/hemo_a_count*100, ".2f"))

if hemo_b_count > 0:
    print("Inhibitor B %:", format(inhibitor_b_count/hemo_b_count*100, ".2f"))

if hemo_a_count > 0:
    print("Prophylaxis A %:", format(prophylaxis_a_count/hemo_a_count*100, ".2f"))

if hemo_b_count > 0:
    print("Prophylaxis B %:", format(prophylaxis_b_count/hemo_b_count*100, ".2f"))

if moderate_count > 0:
    print("Moderate prophylaxis %:",
          format(moderate_prophylaxis_count/moderate_count*100, ".2f"))

print("\nTotal Factor-8 Plasma IU:", total_f8_plasma)
print("Total Factor-8 Recombinant IU:", total_f8_recom)
print("Total Factor-9 Plasma IU:", total_f9_plasma)
print("Total Factor-9 Recombinant IU:", total_f9_recom)

print("\nTotal 4-week IU:", total_iu_4_weeks)
print("Total 4-week cost: $", format(total_cost_4_weeks, ".2f"))
print("Total 1-year cost: $", format(total_cost_4_weeks * 13, ".2f"))

if patient_count > 0:
    print("Average annual IU per patient:",
          format((total_iu_4_weeks * 13) / patient_count, ".2f"))
    print("Average annual cost per patient: $",
          format((total_cost_4_weeks * 13) / patient_count, ".2f"))

print("\nHighest Cost Patient:")
print(max_cost_data)

print("\nHighest IU Hemophilia A:")
print(max_iu_a_data)

print("\nHighest IU Hemophilia B:")
print(max_iu_b_data)

print("===================================================")