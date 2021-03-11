from faker import Faker
fake = Faker()
print('INSERT INTO base_email_infobip_final() VALUES')
for i in range(60):
  email = fake.email()
  print("('"+fake.msisdn()+"','InfoSMS','{\"nome\":\""+fake.name()+"\",\"saldo\":\"43.65\"}','"+str(fake.future_datetime())+"','1','1234','na','sms',0),")