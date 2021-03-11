from faker import Faker
fake = Faker()
print('INSERT INTO base_email_infobip_final() VALUES')
for i in range(60):
  email = fake.email()
  print("('"+str(i)+"' ,'na','"+fake.msisdn()+"','{\"primeiro_nome\":\""+fake.name()+"\"}','"+str(fake.future_datetime())+"','1' ,'1058703','na','sms',0),")