def register_party(parties):
 
    party_name = input("Enter the name of the new party: ")
    reg_number = max(party['reg_number'] for party in parties) + 1
    member_count = int(input("Enter the number of members in the new party: "))

    if member_count < 1000:
        print(f"{party_name} does not have the required number of members to register.")
        return

    parties.append({
        "party_name": party_name,
        "reg_number": reg_number,
        "member_count": member_count
    })

    print(f"{party_name} has been successfully registered with the registration number {reg_number}.")