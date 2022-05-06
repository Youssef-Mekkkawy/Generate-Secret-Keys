from Generator import Generator

generator = Generator()

""" # Secret_Key  """

secret_key_With_details  = generator.Secret_Key(Length = 48, Number_of_Each_Separated = [12,6,6,24], Separated = "=+=")
print(f"Secret key With 4 Separation is: {secret_key_With_details}")
############################################################################
secret_key_With_details  = generator.Secret_Key(Length = 36, Number_of_Each_Separated = [8,4,4,4,16], Separated = "-")
print(f"Secret key With 5 Separation is: {secret_key_With_details}")
############################################################################
secret_key_With_details  = generator.Secret_Key()
print(f"Secret key With Details is: {secret_key_With_details}")
############################################################################
secret_key_Without_details  = generator.Secret_Key(Out_Put_ID_Only = True)
print(f"Secret key Without Details is: {secret_key_Without_details}")
############################################################################
secret_key_With_Separated = generator.Secret_Key(Separated = "-")
print(f"Secret key Wiht Separated is: {secret_key_With_Separated}")
############################################################################

""" Password  """
Password = generator.Password()
print(f"Password is: {Password}")
############################################################################
Password_With_Special_Chara = generator.Password(Special_Chara = "\\|")
print(f"Secret key with Special_Chara is: {Password_With_Special_Chara}")