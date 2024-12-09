import streamlit as st
import random

st.title("🎅 Prezenty Świąteczne Generator")

# Input for party guests
guest_list = st.text_area("Wprowadź imiona gości (każde na nowej linii):")

if st.button("Generuj prezenty"):
    if guest_list:
        # Convert input text to list of names
        guests = [name.strip() for name in guest_list.split('\n') if name.strip()]
        
        if len(guests) < 2:
            st.error("Please enter at least 2 names!")
        else:
            success = False
            max_attempts = 100  # Prevent infinite loops
            
            while not success and max_attempts > 0:
                # Create a copy of guests list for recipients
                recipients = guests.copy()
                assignments = {}
                valid_assignment = True
                
                for gifter in guests:
                    # Find valid recipient (not self and not already assigned)
                    possible_recipients = [r for r in recipients if r != gifter]
                    
                    if not possible_recipients:
                        valid_assignment = False
                        break
                    
                    recipient = random.choice(possible_recipients)
                    assignments[gifter] = recipient
                    recipients.remove(recipient)
                
                if valid_assignment and len(assignments) == len(guests):
                    success = True
                else:
                    max_attempts -= 1
            
            # Display results
            if success:
                st.success("Secret Santa assignments generated!")
                for gifter, recipient in assignments.items():
                    st.write(f"🎁 {gifter} will give a gift to {recipient}")
            else:
                st.error("Unable to generate valid assignments after multiple attempts. Please try again!")

# Add some instructions
st.markdown("""
---
### Jak używać:
1. Wprowadź imiona gości na nowej linii
2. Kliknij przycisk 'Generuj prezenty'
3. Każdy osoba zostanie losowo przypisana do osoby, która będzie dawać prezent
""")