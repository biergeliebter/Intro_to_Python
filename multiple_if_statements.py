tax=0
country = input('What country do you live in? ')

if country.lower() == 'canada':
    province = input('What province do you live in? ')
    if province.lower() == 'alberta':
        tax = 0.05
    elif province.lower() == 'nunavut':
        tax = 0.05
# if province.lower in('alberta','nunavut','yukon'):
#    tax = 0.05
    elif province.lower() == 'ontario':
        tax = 0.13
    else:
        tax = 0.15
else:
    tax = 0.0
print(tax)

