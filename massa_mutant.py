from faker import Faker
fake = Faker()
print('INSERT INTO base_email_infobip_final() VALUES')
for i in range(60):
  email = fake.email()
  print("('"+email+"', '"+email+"' , '{\"num_trans\":\"10\",\"primeiro_nome\":\"Pedro\"}' , '"+str(fake.future_datetime())+"',  '1' , '1054794' , 'na' ,  'email', 0),")
  