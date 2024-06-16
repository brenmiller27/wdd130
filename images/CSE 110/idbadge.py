
First = 'Bren'
Last = 'Miller'
Email = 'bren.miller09@gmail.com'
Phone = '208-369-2445'
id_number = '83-23851'
Job_Title= 'Software Architect'
Hair= 'Brown'
Eyes= 'Blue'
Month= 'September'


print()
print("Please enter the following information:")
print()
First= input("First Name: ")
Last = input("Last Name: ")
Email= input("Email Address: ")
Phone= input("Phone: ")
id_number= input("ID#: ")
Job_Title= input("Job Title: ")



print()
print("\nThe ID Card is:")
print('----------------------------------')
print(f"{Last.upper()} , {First.capitalize()}")
print(Job_Title.title())
print()
print(Email.lower())
print(Phone)
print()
print(f"Hair: {Hair:15}   Eyes:{Eyes}")
print(f"Month: {Month:14}"  )
print("---------------------------------")


