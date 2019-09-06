def parse_url_string(url):
    params = url.split('?')[1].split('&')
    car = {}
    for param in params:
        car[param.split('=')[0]] = param.split('=')[1]
    return car
    
model_x = parse_url_string('domain.com?referral=x&commission=20&package=gold&period=3&quantiy=1')

print model_x
print 'Referral: %s' % model_x['referral']
print 'Commission: %s' %model_x['commission']
print 'Package: %s' %model_x['package']
print 'Period: %s' %model_x['period']
print 'Quantity: %s' %model_x['quantity']
