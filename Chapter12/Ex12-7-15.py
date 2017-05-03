# Exercise 12.7.15

# Write a program that allows the user to enter a string. It then prints a table of the letters of the alphabet
# in alphabetical order which occur in the string together with the number of times each letter occurs.
# Case should be ignored.


def let_count_tab():
    st = input('Enter a sentence ').lower().replace(' ', '')
    let_dict = {}
    for n in st:
        let_dict[n] = st.count(n)
    for k in sorted(let_dict.keys()):
        print(k, let_dict[k])

let_count_tab()
