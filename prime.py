import streamlit as st


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def show_result(number, is_prime):
    color = "#d4edda" if is_prime else "#f8d7da" 
    message = f"{number} is {'prime' if is_prime else 'not prime'}"
    st.markdown(f"<div style='background-color:{color};padding:10px;'>{message}</div>", unsafe_allow_html=True)


st.title("Prime Number Checker")


if st.button("Reset"):
    st.experimental_rerun()


option = st.selectbox("Check:", ["Single number", "List of numbers"])

if option == "Single number":
    
    number = st.number_input("Enter number", value=1, step=1)
    
    if st.button("Check"):
        show_result(number, is_prime(number))

else:
    
    numbers_input = st.text_area("Enter numbers and separate them by commas", "2, 3, 4, 5")
    
    if st.button("Check List"):
        numbers = [int(num.strip()) for num in numbers_input.split(",")]
        prime_count = 0
        
        
        for num in numbers:
            prime_status = is_prime(num)
            show_result(num, prime_status)
            prime_count += prime_status
        
        
        st.info(f"Out of {len(numbers)} numbers, {prime_count} are prime.")
