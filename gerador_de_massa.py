from faker import Faker
fake = Faker()
print('INSERT INTO base_email_infobip_final() VALUES')
for i in range(60):
  print("('"+str(i)+"', '"+fake.email()+"', '{\"nome\":\""+fake.name()+"\",\"saldo\":\"0989\"}', '"+str(fake.future_datetime())+"', '1', '197813', 'na', 'email', 0),")
  #print("("+str(i)+", "+fake.email()+", '{'nome':'"+fake.name()+"','saldo':'0989'}', '2021-02-12 10:50:00', '1', '197813', 'na', 'email', 0)")
